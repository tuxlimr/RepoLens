"""Safe Python AST extraction (stdlib ast only; code is never executed)."""
from __future__ import annotations
import ast
from dataclasses import dataclass, field
from .sanitize import sanitize_text

ROUTE_METHODS = {"get", "post", "put", "delete", "patch", "head", "options", "route", "api_route"}
APP_FACTORIES = {"FastAPI", "Flask", "Django", "Celery", "Typer", "Click", "Group", "Command"}

@dataclass
class ImportInfo:
    module: str
    line: int
    level: int = 0

@dataclass
class SymbolInfo:
    name: str
    kind: str
    line: int

@dataclass
class RouteInfo:
    method: str
    route_path: str
    function: str
    line: int

@dataclass
class PyModuleInfo:
    path: str
    imports: list = field(default_factory=list)
    classes: list = field(default_factory=list)
    functions: list = field(default_factory=list)
    routes: list = field(default_factory=list)
    app_factories: list = field(default_factory=list)
    has_main_guard: bool = False
    main_guard_line: int | None = None
    cli_commands: list = field(default_factory=list)

def _dotted(node):
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr); node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))

def _is_main_guard(node):
    test = node.test
    if not isinstance(test, ast.Compare) or len(test.ops) != 1 or not isinstance(test.ops[0], ast.Eq):
        return False
    sides = [test.left, *test.comparators]
    names = [s.id for s in sides if isinstance(s, ast.Name)]
    vals = [s.value for s in sides if isinstance(s, ast.Constant) and isinstance(s.value, str)]
    return "__name__" in names and "__main__" in vals

def _inspect_decorator(info, func, deco):
    call = deco if isinstance(deco, ast.Call) else None
    dotted = _dotted(call.func if call else deco)
    if not dotted:
        return
    last = dotted.rsplit(".", 1)[-1].lower()
    if last in ROUTE_METHODS and call is not None:
        route_path = ""
        if call.args and isinstance(call.args[0], ast.Constant) and isinstance(call.args[0].value, str):
            route_path = sanitize_text(call.args[0].value, 120)
        info.routes.append(RouteInfo(method=last.upper(), route_path=route_path, function=sanitize_text(func.name, 80), line=func.lineno))
    elif last in {"command", "group"} and any(k in dotted.lower() for k in ("click", "typer", "app", "cli")):
        info.cli_commands.append(SymbolInfo(name=sanitize_text(func.name, 80), kind="cli", line=func.lineno))

def parse_python_file(path, content):
    try:
        tree = ast.parse(content, filename=path)
    except (SyntaxError, ValueError, MemoryError, RecursionError):
        return None
    info = PyModuleInfo(path=path)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                info.imports.append(ImportInfo(module=alias.name, line=node.lineno))
        elif isinstance(node, ast.ImportFrom):
            info.imports.append(ImportInfo(module=node.module or "", line=node.lineno, level=node.level or 0))
        elif isinstance(node, ast.If) and _is_main_guard(node):
            info.has_main_guard = True; info.main_guard_line = node.lineno
        elif isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            factory = _dotted(node.value.func).rsplit(".", 1)[-1]
            if factory in APP_FACTORIES:
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        info.app_factories.append((target.id, factory, node.lineno))
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            info.classes.append(SymbolInfo(name=sanitize_text(node.name, 80), kind="class", line=node.lineno))
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for deco in item.decorator_list:
                        _inspect_decorator(info, item, deco)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            info.functions.append(SymbolInfo(name=sanitize_text(node.name, 80), kind="function", line=node.lineno))
            for deco in node.decorator_list:
                _inspect_decorator(info, node, deco)
    info.imports.sort(key=lambda i: (i.line, i.module))
    return info
