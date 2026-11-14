"""Sanitization helpers. Repository text is untrusted data, never instructions."""
from __future__ import annotations
import re
REDACTED = "[REDACTED]"
_PRIVATE_KEY_RE = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.DOTALL)
_ASSIGNMENT_RE = re.compile(r"(?i)\b(api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|secret[_-]?key|secret|password|passwd|pwd|private[_-]?key|aws_secret_access_key)\b(\s*[:=]\s*)([\"']?)([^\s\"',}\]]+)\3")
_URL_CRED_RE = re.compile(r"(://[^/\s:@]+:)([^@\s/]+)(@)")
_BEARER_RE = re.compile(r"(?i)\b(Bearer\s+)[A-Za-z0-9._\-+/=]{8,}")
_TOKEN_PATTERNS = [re.compile(r"\bAKIA[0-9A-Z]{16}\b"), re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"), re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"), re.compile(r"\bsk-[A-Za-z0-9_\-]{16,}\b"), re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}\b"), re.compile(r"\bAIza[0-9A-Za-z_\-]{20,}\b")]

def sanitize_text(text, max_length=None):
    if text is None:
        return ""
    out = str(text)
    out = _PRIVATE_KEY_RE.sub(REDACTED, out)
    out = _URL_CRED_RE.sub(r"\1" + REDACTED + r"\3", out)
    out = _ASSIGNMENT_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}{REDACTED}", out)
    out = _BEARER_RE.sub(r"\1" + REDACTED, out)
    for pat in _TOKEN_PATTERNS:
        out = pat.sub(REDACTED, out)
    if max_length is not None and len(out) > max_length:
        out = out[: max_length - 1].rstrip() + "…"
    return out

def sanitize_label(text, max_length=60):
    out = sanitize_text(text).replace("\r", " ").replace("\n", " ")
    out = re.sub(r'["\[\]{}()<>#;|]', " ", out)
    out = re.sub(r"\s+", " ", out).strip()
    if len(out) > max_length:
        out = out[:max_length].rstrip()
    return out or "component"

def is_secret_path(path):
    p = path.replace("\\", "/").lower()
    name = p.rsplit("/", 1)[-1]
    if name in {".env.example", ".env.sample", ".env.template", ".env.dist"}:
        return False
    if name == ".env" or name.startswith(".env."):
        return True
    if name.endswith((".pem", ".key", ".p12", ".pfx", ".keystore")):
        return True
    if name in {"credentials", "credentials.json", "credentials.yaml", "credentials.yml", "id_rsa", "id_dsa", "id_ecdsa", "id_ed25519", ".netrc", ".npmrc", ".pypirc"}:
        return True
    if "secret" in name and name.endswith((".json", ".yaml", ".yml", ".txt", ".env")):
        return True
    return False

def slugify(text, fallback="component"):
    slug = re.sub(r"[^a-z0-9]+", "_", sanitize_text(text).lower()).strip("_")
    if not slug:
        slug = fallback
    if slug[0].isdigit():
        slug = f"c_{slug}"
    return slug
