# Project structure: midudev/preguntas-entrevista-react

**Analysed commit:** `99d805f10ac5d3e0ad436a0458bc33f3596c9375`

**Commit reference:** [99d805f10ac5d3e0ad436a0458bc33f3596c9375](https://github.com/midudev/preguntas-entrevista-react/commit/99d805f10ac5d3e0ad436a0458bc33f3596c9375)

**Tree at this commit:** [midudev/preguntas-entrevista-react@99d805f10ac5](https://github.com/midudev/preguntas-entrevista-react/tree/99d805f10ac5d3e0ad436a0458bc33f3596c9375)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | midudev/preguntas-entrevista-react |
| Description | Preguntas típicas sobre React para entrevistas de trabajo ⚛️ |
| Stars | 7834 |
| Forks | 740 |
| Licence | MIT |
| Language | Astro |
| Default branch | main |
| Analysed commit | `99d805f10ac5d3e0ad436a0458bc33f3596c9375` |
| Retrieved at | 2026-11-14T19:13:45.244393+00:00 |
| Files in this snapshot | 609 |

## Directory tree

```text
.agents/  (137 files)
  skills/  (137 files)
    accessibility/  (2 files)
      … 2 files under this directory
    best-practices/  (1 files)
      … 1 files under this directory
    core-web-vitals/  (2 files)
      … 2 files under this directory
    frontend-design/  (2 files)
      … 2 files under this directory
    migrate-oxlint/  (1 files)
      … 1 files under this directory
    next-best-practices/  (20 files)
      … 20 files under this directory
    next-cache-components/  (1 files)
      … 1 files under this directory
    next-upgrade/  (1 files)
      … 1 files under this directory
    nodejs-backend-patterns/  (2 files)
      … 2 files under this directory
    nodejs-best-practices/  (1 files)
      … 1 files under this directory
    performance/  (1 files)
      … 1 files under this directory
    seo/  (1 files)
      … 1 files under this directory
    tailwind-css-patterns/  (9 files)
      … 9 files under this directory
    typescript-advanced-types/  (1 files)
      … 1 files under this directory
    vercel-composition-patterns/  (14 files)
      … 14 files under this directory
    vercel-react-best-practices/  (75 files)
      … 75 files under this directory
    web-design-guidelines/  (1 files)
      … 1 files under this directory
    web-quality-audit/  (2 files)
      … 2 files under this directory
.vscode/  (2 files)
  extensions.json
  settings.json
book/  (2 files)
  after.md
  before.md
manuscript/  (8 files)
  00-antes-de-empezar.md
  01-principiante.md
  02-intermedio.md
  03-experto.md
  04-errores-tipicos.md
  05-hasta-aqui.md
  Book.txt
  README.md
public/  (414 files)
  content/  (146 files)
    cant-perform-a-react-state-update-on-an-unmounted-component.json
    como-anadir-un-evento-a-un-componente-en-react.json
    como-crear-un-componente-en-react.json
    como-crear-un-hook-personalizado-custom-hook.json
    como-funciona-el-hook-use-form-status-y-que-aporta-junto-a-las-server-actions.json
    como-funciona-el-hook-use-ref.json
    como-funciona-react-memo-y-cuando-es-util.json
    como-mantener-los-componentes-puros-y-que-ventajas-tiene.json
    como-podemos-ejecutar-codigo-cuando-el-componente-se-desmonta-del-arbol.json
    como-podemos-ejecutar-codigo-cuando-el-componente-se-monta.json
    como-puedes-abortar-una-peticion-fetch-con-use-effect-en-react.json
    como-puedes-acceder-al-evento-nativo-del-navegador-en-react.json
    como-puedes-aplicar-clases-css-a-un-componente-en-react-y-por-que-no-se-puede-usar-class.json
    como-puedes-aplicar-estilos-en-linea-a-un-componente-en-react.json
    como-puedes-cancelar-una-peticion-a-una-api-en-use-effect-correctamente.json
    como-puedes-crear-un-server-side-rendering-con-react-desde-cero.json
    como-puedes-escribir-comentarios-en-react.json
    como-puedes-evitar-re-renders-innecesarios-al-usar-context.json
    como-puedes-exportar-multiples-componentes-de-un-mismo-archivo.json
    como-puedes-inicializar-un-proyecto-de-react-desde-cero.json
    como-puedes-mejorar-el-rendimiento-del-server-side-rendering-en-react-para-evitar-que-bloquee-el-hilo-principal.json
    como-puedes-prevenir-el-comportamiento-por-defecto-de-un-evento-en-react.json
    como-puedes-registrar-un-evento-en-la-fase-de-captura-en-react.json
    como-puedo-aplicar-estilos-de-forma-condicional-a-un-componente-en-react.json
    … 122 more files
  quiz/  (145 files)
    qa/  (145 files)
      … 145 files under this directory
  can-t-perform-a-react-state-update-on-an-unmounted-component.json
  cant-perform-a-react-state-update-on-an-unmounted-component.json
  como-anadir-un-evento-a-un-componente-en-react.json
  como-crear-un-componente-en-react.json
  como-crear-un-hook-personalizado-custom-hook.json
  como-funciona-el-hook-use-form-status-y-que-aporta-junto-a-las-server-actions.json
  como-funciona-el-hook-use-ref.json
  como-funciona-react-memo-y-cuando-es-util.json
  como-mantener-los-componentes-puros-y-que-ventajas-tiene.json
  como-podemos-ejecutar-codigo-cuando-el-componente-se-desmonta-del-arbol.json
  como-podemos-ejecutar-codigo-cuando-el-componente-se-monta.json
  como-puedes-abortar-una-peticion-fetch-con-use-effect-en-react.json
  como-puedes-acceder-al-evento-nativo-del-navegador-en-react.json
  como-puedes-aplicar-clases-css-a-un-componente-en-react-y-por-que-no-se-puede-usar-class.json
  como-puedes-aplicar-estilos-en-linea-a-un-componente-en-react.json
  como-puedes-cancelar-una-peticion-a-una-api-en-use-effect-correctamente.json
  como-puedes-crear-un-server-side-rendering-con-react-desde-cero.json
  como-puedes-escribir-comentarios-en-react.json
  como-puedes-exportar-multiples-componentes-de-un-mismo-archivo.json
  como-puedes-inicializar-un-proyecto-de-react-desde-cero.json
  como-puedes-mejorar-el-rendimiento-del-server-side-rendering-en-react-para-evitar-que-bloquee-el-hilo-principal.json
  como-puedes-prevenir-el-comportamiento-por-defecto-de-un-evento-en-react.json
  como-puedes-registrar-un-evento-en-la-fase-de-captura-en-react.json
  como-puedo-aplicar-estilos-de-forma-condicional-a-un-componente-en-react.json
  … 99 more files
scripts/  (3 files)
  exportBook.mjs
  lint.mjs
  markdownToJson.mjs
src/  (28 files)
  components/  (14 files)
    BookCover.astro
    ButtonRead.astro
    BuyBook.astro
    Card.astro
    Footer.astro
    Header.astro
    ListOfQuestions.astro
    Pill.astro
    Quiz.tsx
    ReactLogo.astro
    Seo.astro
    Stars.astro
    ThemeToggle.astro
    Title.astro
  layouts/  (1 files)
    BaseLayout.astro
  lib/  (4 files)
    code-blocks.ts
    github-stars.ts
    markdown.ts
    posts.ts
  pages/  (4 files)
    404.astro
    [post].astro
    index.astro
    questions.astro
  styles/  (3 files)
    article.css
    global.css
    highlight.css
  constants.ts
  env.d.ts
.gitignore
.markdownlint.json
.nvmrc
.oxlintrc.json
.prettierrc
CLAUDE.md
CONTRIBUTING.md
LICENSE
astro.config.mjs
package.json
pnpm-workspace.yaml
pull_request_template.md
skills-lock.json
tsconfig.json
vercel.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 1 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 415 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.ts package | library | Observed | Groups 1 file(s) under constants.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| env.d.ts package | library | Observed | Groups 1 file(s) under env.d.ts package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 4 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.agents/skills/vercel-composition-patterns/metadata.json` (config)
- `.agents/skills/vercel-react-best-practices/metadata.json` (config)
- `.markdownlint.json` (config)
- `.oxlintrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `public/can-t-perform-a-react-state-update-on-an-unmounted-component.json` (config)
- `public/cant-perform-a-react-state-update-on-an-unmounted-component.json` (config)
- `public/como-anadir-un-evento-a-un-componente-en-react.json` (config)
- `public/como-crear-un-componente-en-react.json` (config)
- `public/como-crear-un-hook-personalizado-custom-hook.json` (config)
- `public/como-funciona-el-hook-use-form-status-y-que-aporta-junto-a-las-server-actions.json` (config)
- `public/como-funciona-el-hook-use-ref.json` (config)
- `public/como-funciona-react-memo-y-cuando-es-util.json` (config)
- `public/como-mantener-los-componentes-puros-y-que-ventajas-tiene.json` (config)
- `public/como-podemos-ejecutar-codigo-cuando-el-componente-se-desmonta-del-arbol.json` (config)
- `public/como-podemos-ejecutar-codigo-cuando-el-componente-se-monta.json` (config)
- `public/como-puedes-abortar-una-peticion-fetch-con-use-effect-en-react.json` (config)
- `public/como-puedes-acceder-al-evento-nativo-del-navegador-en-react.json` (config)
- `public/como-puedes-aplicar-clases-css-a-un-componente-en-react-y-por-que-no-se-puede-usar-class.json` (config)
- `public/como-puedes-aplicar-estilos-en-linea-a-un-componente-en-react.json` (config)
- `public/como-puedes-cancelar-una-peticion-a-una-api-en-use-effect-correctamente.json` (config)
- `public/como-puedes-crear-un-server-side-rendering-con-react-desde-cero.json` (config)
- `public/como-puedes-escribir-comentarios-en-react.json` (config)
- `public/como-puedes-exportar-multiples-componentes-de-un-mismo-archivo.json` (config)
- `public/como-puedes-inicializar-un-proyecto-de-react-desde-cero.json` (config)
- `public/como-puedes-mejorar-el-rendimiento-del-server-side-rendering-en-react-para-evitar-que-bloquee-el-hilo-principal.json` (config)
- `public/como-puedes-prevenir-el-comportamiento-por-defecto-de-un-evento-en-react.json` (config)
- `public/como-puedes-registrar-un-evento-en-la-fase-de-captura-en-react.json` (config)
- `public/como-puedo-aplicar-estilos-de-forma-condicional-a-un-componente-en-react.json` (config)
- `public/como-puedo-importar-de-forma-dinamica-un-componente-en-react.json` (config)
- `public/como-puedo-inyectar-html-directamente-en-un-componente-de-react.json` (config)
- `public/como-puedo-pasar-un-parametro-a-una-funcion-que-maneja-un-evento-en-react.json` (config)
- `public/como-puedo-validar-el-tipo-de-mis-props.json` (config)
- `public/como-puedo-validar-las-propiedades-de-un-array-con-prop-types.json` (config)
- `public/como-puedo-validar-las-propiedades-de-un-objeto-con-prop-types.json` (config)
- `public/como-se-complementan-use-memo-use-callback-use-transition-y-use-deferred-value-para-optimizar-el-rendimiento.json` (config)
- `public/como-se-transforma-el-jsx.json` (config)
- `public/como-suscribirse-a-un-evento-en-use-effect.json` (config)
- `public/content/cant-perform-a-react-state-update-on-an-unmounted-component.json` (config)
- `public/content/como-anadir-un-evento-a-un-componente-en-react.json` (config)
- `public/content/como-crear-un-componente-en-react.json` (config)
- `public/content/como-crear-un-hook-personalizado-custom-hook.json` (config)
- `public/content/como-funciona-el-hook-use-form-status-y-que-aporta-junto-a-las-server-actions.json` (config)
- `public/content/como-funciona-el-hook-use-ref.json` (config)
- `public/content/como-funciona-react-memo-y-cuando-es-util.json` (config)
- `public/content/como-mantener-los-componentes-puros-y-que-ventajas-tiene.json` (config)
- `public/content/como-podemos-ejecutar-codigo-cuando-el-componente-se-desmonta-del-arbol.json` (config)
- `public/content/como-podemos-ejecutar-codigo-cuando-el-componente-se-monta.json` (config)
- `public/content/como-puedes-abortar-una-peticion-fetch-con-use-effect-en-react.json` (config)
- `public/content/como-puedes-acceder-al-evento-nativo-del-navegador-en-react.json` (config)
- `public/content/como-puedes-aplicar-clases-css-a-un-componente-en-react-y-por-que-no-se-puede-usar-class.json` (config)
- `public/content/como-puedes-aplicar-estilos-en-linea-a-un-componente-en-react.json` (config)
- `public/content/como-puedes-cancelar-una-peticion-a-una-api-en-use-effect-correctamente.json` (config)
- `public/content/como-puedes-crear-un-server-side-rendering-con-react-desde-cero.json` (config)
- `public/content/como-puedes-escribir-comentarios-en-react.json` (config)
- `public/content/como-puedes-evitar-re-renders-innecesarios-al-usar-context.json` (config)
- `public/content/como-puedes-exportar-multiples-componentes-de-un-mismo-archivo.json` (config)
- `public/content/como-puedes-inicializar-un-proyecto-de-react-desde-cero.json` (config)
- `public/content/como-puedes-mejorar-el-rendimiento-del-server-side-rendering-en-react-para-evitar-que-bloquee-el-hilo-principal.json` (config)
- `public/content/como-puedes-prevenir-el-comportamiento-por-defecto-de-un-evento-en-react.json` (config)
- `public/content/como-puedes-registrar-un-evento-en-la-fase-de-captura-en-react.json` (config)
- `public/content/como-puedo-aplicar-estilos-de-forma-condicional-a-un-componente-en-react.json` (config)
- `public/content/como-puedo-hacer-testing-de-un-componente.json` (config)
- `public/content/como-puedo-hacer-testing-de-un-hook.json` (config)
- `public/content/como-puedo-importar-de-forma-dinamica-un-componente-en-react.json` (config)
- `public/content/como-puedo-inyectar-html-directamente-en-un-componente-de-react.json` (config)
- `public/content/como-puedo-pasar-un-parametro-a-una-funcion-que-maneja-un-evento-en-react.json` (config)
- `public/content/como-puedo-validar-el-tipo-de-mis-props.json` (config)
- `public/content/como-puedo-validar-las-propiedades-de-un-array-con-prop-types.json` (config)
- `public/content/como-puedo-validar-las-propiedades-de-un-objeto-con-prop-types.json` (config)
- `public/content/como-se-complementan-use-memo-use-callback-use-transition-y-use-deferred-value-para-optimizar-el-rendimiento.json` (config)
- `public/content/como-se-puede-renderizar-un-context-desde-un-server-component.json` (config)
- `public/content/como-se-transforma-el-jsx.json` (config)
- `public/content/como-suscribirse-a-un-evento-en-use-effect.json` (config)
- `public/content/counter.json` (config)
- `public/content/cual-es-el-proposito-del-atributo-key-en-react-y-por-que-es-importante-usarlo-correctamente-al-renderizar-listas-de-elementos.json` (config)
- `public/content/cual-es-la-diferencia-entre-componente-y-elemento-en-react.json` (config)
- `public/content/cual-es-la-diferencia-entre-la-prop-action-y-el-atributo-form-action-en-react-next-js.json` (config)
- `public/content/cual-es-la-diferencia-entre-use-callback-y-use-memo.json` (config)
- `public/content/cuales-son-las-caracteristicas-principales-de-react.json` (config)
- `public/content/cuales-son-las-reglas-de-los-hooks-en-react.json` (config)
- `public/content/cuando-y-por-que-es-recomendable-importar-componentes-de-forma-dinamica.json` (config)
- `public/content/cuantos-use-effect-puede-tener-un-componente.json` (config)
- `public/content/en-react-19-se-necesita-todavia-forward-ref.json` (config)
- `public/content/es-buena-idea-usar-siempre-use-callback-para-optimizar-nuestros-componentes.json` (config)
- `public/content/es-buena-idea-usar-siempre-use-memo-para-optimizar-nuestros-componentes.json` (config)
- `public/content/es-react-una-biblioteca-o-un-framework-por-que.json` (config)
- `public/content/explica-casos-de-uso-del-hook-use-effect.json` (config)
- `public/content/index.json` (config)
- `public/content/para-que-sirve-add-transition-type.json` (config)
- `public/content/para-que-sirve-el-hook-use-action-state.json` (config)
- `public/content/para-que-sirve-el-hook-use-callback.json` (config)
- `public/content/para-que-sirve-el-hook-use-deferred-value.json` (config)
- `public/content/para-que-sirve-el-hook-use-imperative-handle.json` (config)
- `public/content/para-que-sirve-el-hook-use-insertion-effect.json` (config)
- `public/content/para-que-sirve-el-hook-use-memo.json` (config)
- `public/content/para-que-sirve-el-hook-use-sync-external-store.json` (config)
- `public/content/para-que-sirve-el-hook-use-transition-y-cuando-deberias-usarlo.json` (config)
- `public/content/para-que-sirve-el-metodo-clone-element-de-react.json` (config)
- `public/content/para-que-sirve-el-metodo-render-to-readable-stream.json` (config)
- `public/content/por-que-debemos-utilizar-una-funcion-para-actualizar-el-estado-de-react.json` (config)
- `public/content/por-que-es-recomendable-exportar-los-componentes-de-react-de-forma-nombrada.json` (config)
- `public/content/por-que-es-recomendable-usar-fragment-en-vez-de-un-div.json` (config)
- `public/content/por-que-no-podemos-usar-un-if-en-el-renderizado-de-un-componente.json` (config)
- `public/content/por-que-no-se-debe-mutar-el-estado-directamente-en-react.json` (config)
- `public/content/por-que-puede-ser-mala-idea-pasar-siempre-todas-las-props-de-un-objeto-a-un-componente.json` (config)
- `public/content/por-que-puede-ser-mala-practica-usar-el-index-como-key-en-un-listado-de-react.json` (config)
- `public/content/por-que-strict-mode-renderiza-dos-veces-la-aplicacion.json` (config)
- `public/content/puedes-poner-un-ejemplo-de-efectos-colaterales-en-react.json` (config)
- `public/content/que-cambia-en-las-transitions-independientes-de-react-19-3.json` (config)
- `public/content/que-diferencia-existe-entre-shadow-dom-y-virtual-dom.json` (config)
- `public/content/que-diferencia-hay-entre-componentes-controlados-y-no-controlados-que-ventajas-y-desventajas-tienen.json` (config)
- `public/content/que-diferencia-hay-entre-componentes-de-servidor-y-componentes-de-cliente-en-react-next-js.json` (config)
- `public/content/que-diferencia-hay-entre-props-y-state.json` (config)
- `public/content/que-diferencia-hay-entre-react-dom-render-create-root-y-hydrate-root.json` (config)
- `public/content/que-diferencia-hay-entre-render-to-static-node-stream-y-render-to-pipeable-stream.json` (config)
- `public/content/que-diferencia-hay-entre-use-effect-y-use-layout-effect.json` (config)
- `public/content/que-es-concurrent-react-y-que-problemas-resuelve.json` (config)
- `public/content/que-es-el-batching-de-actualizaciones-de-estado-en-react.json` (config)
- `public/content/que-es-el-binding.json` (config)
- `public/content/que-es-el-ciclo-de-vida-de-un-componente-en-react.json` (config)
- `public/content/que-es-el-componente-view-transition-en-react.json` (config)
- `public/content/que-es-el-compound-components-pattern.json` (config)
- `public/content/que-es-el-contexto-en-react-como-puedo-crearlo-y-consumirlo.json` (config)
- `public/content/que-es-el-estado-derivado-y-por-que-conviene-calcularlo-en-el-render.json` (config)
- `public/content/que-es-el-estado-en-react.json` (config)
- `public/content/que-es-el-hook-use-debug-value.json` (config)
- `public/content/que-es-el-hook-use-form-state-y-cuando-conviene-usarlo.json` (config)
- `public/content/que-es-el-profiler-en-react.json` (config)
- `public/content/que-es-el-react-compiler-y-que-ventajas-aporta.json` (config)
- `public/content/que-es-el-renderizado-condicional-en-react.json` (config)
- `public/content/que-es-el-renderizado-de-listas-en-react.json` (config)
- `public/content/que-es-el-server-side-rendering-y-que-ventajas-tiene.json` (config)
- `public/content/que-es-el-strict-mode-en-react.json` (config)
- `public/content/que-es-el-synthetic-event-en-react.json` (config)
- `public/content/que-es-el-virtual-dom.json` (config)
- `public/content/que-es-flush-sync-en-react.json` (config)
- `public/content/que-es-flux.json` (config)
- `public/content/que-es-jsx.json` (config)
- `public/content/que-es-la-composicion-de-componentes-y-por-que-react-la-prefiere-a-la-herencia.json` (config)
- `public/content/que-es-la-funcion-use-en-react-y-para-que-se-utiliza.json` (config)
- `public/content/que-es-la-hidratacion-hydration-en-react.json` (config)
- `public/content/que-es-la-reconciliacion-reconciliation-en-react.json` (config)
- `public/content/que-es-react-dom.json` (config)
- `public/content/que-es-react-fiber.json` (config)
- `public/content/que-es-react-lazy-y-como-se-combina-con-suspense.json` (config)
- `public/content/que-es-react.json` (config)
- `public/content/que-es-start-transition-y-en-que-se-diferencia-de-actualizar-el-estado-de-forma-normal.json` (config)
- `public/content/que-es-suspense-en-react-y-para-que-se-usa.json` (config)
- `public/content/que-es-un-componente.json` (config)
- `public/content/que-es-una-stale-closure-y-como-afecta-a-los-hooks.json` (config)
- `public/content/que-es-y-para-que-sirve-la-prop-children-en-react.json` (config)
- `public/content/que-hace-el-hook-use-effect.json` (config)
- `public/content/que-hace-el-hook-use-id.json` (config)
- `public/content/que-hace-el-hook-use-layout-effect.json` (config)
- `public/content/que-hace-el-hook-use-reducer.json` (config)
- `public/content/que-hace-el-hook-use-state.json` (config)
- `public/content/que-hace-la-api-browser-de-react-dom.json` (config)
- `public/content/que-java-script-necesito-para-aprender-react.json` (config)
- `public/content/que-problema-resuelve-el-hook-use-optimistic.json` (config)
- `public/content/que-problemas-crees-que-pueden-aparecer-en-una-aplicacion-al-querer-visualizar-listas-de-miles-millones-de-datos.json` (config)
- `public/content/que-provoca-un-re-render-en-un-componente-de-react.json` (config)
- `public/content/que-quiere-decir-warning-each-child-in-a-list-should-have-a-unique-key-prop.json` (config)
- `public/content/que-significa-exactamente-que-sea-declarativo.json` (config)
- `public/content/que-significa-la-expresion-subir-el-estado.json` (config)
- `public/content/que-solucion-es-implementarias-para-evitar-problemas-de-rendimiento-al-trabajar-con-listas-de-miles-millones-de-datos.json` (config)
- `public/content/que-son-las-forward-refs.json` (config)
- `public/content/que-son-las-fragment-refs-y-que-problemas-resuelven.json` (config)
- `public/content/que-son-las-props-en-react.json` (config)
- `public/content/que-son-las-refs-en-react.json` (config)
- `public/content/que-son-las-render-props.json` (config)
- `public/content/que-son-las-server-actions-y-como-se-usan-con-formularios-en-react.json` (config)
- `public/content/que-son-los-componentes-stateless.json` (config)
- `public/content/que-son-los-error-boundaries-en-react.json` (config)
- `public/content/que-son-los-fragments-en-react.json` (config)
- `public/content/que-son-los-high-order-components-hoc.json` (config)
- `public/content/que-son-los-hooks.json` (config)
- `public/content/que-son-los-portales-en-react.json` (config)
- `public/content/que-son-mejores-los-componentes-de-clase-o-los-componentes-funcionales.json` (config)
- `public/content/que-son-trusted-types-y-como-los-soporta-react-19-3.json` (config)
- `public/content/react-hook-use-xxx-is-called-conditionally-react-hooks-must-be-called-in-the-exact-same-order-in-every-component-render.json` (config)
- `public/content/se-puede-inicializar-un-estado-con-el-valor-de-una-prop-que-pasa-si-lo-haces-y-que-hay-que-tener-en-cuenta.json` (config)
- `public/content/solo-se-pueden-cargar-componentes-de-forma-dinamica-si-se-exportan-por-defecto.json` (config)
- `public/content/too-many-re-renders-react-limits-the-number-of-renders-to-prevent-an-infinite-loop.json` (config)
- `public/cual-es-el-proposito-del-atributo-key-en-react-y-por-que-es-importante-usarlo-correctamente-al-renderizar-listas-de-elementos.json` (config)
- `public/cual-es-la-diferencia-entre-componente-y-elemento-en-react.json` (config)
- `public/cual-es-la-diferencia-entre-la-prop-action-y-el-atributo-form-action-en-react-next-js.json` (config)
- `public/cual-es-la-diferencia-entre-use-callback-y-use-memo.json` (config)
- `public/cuales-son-las-caracteristicas-principales-de-react.json` (config)
- `public/cuales-son-las-reglas-de-los-hooks-en-react.json` (config)
- `public/cuando-y-por-que-es-recomendable-importar-componentes-de-forma-dinamica.json` (config)
- `public/cuantos-use-effect-puede-tener-un-componente.json` (config)
- `public/es-buena-idea-usar-siempre-use-callback-para-optimizar-nuestros-componentes.json` (config)
- `public/es-buena-idea-usar-siempre-use-memo-para-optimizar-nuestros-componentes.json` (config)
- `public/es-react-una-biblioteca-o-un-framework-por-que.json` (config)
- `public/explica-casos-de-uso-del-hook-use-effect.json` (config)
- `public/para-que-sirve-el-hook-use-action-state.json` (config)
- `public/para-que-sirve-el-hook-use-callback.json` (config)
- `public/para-que-sirve-el-hook-use-deferred-value.json` (config)
- `public/para-que-sirve-el-hook-use-imperative-handle.json` (config)
- `public/para-que-sirve-el-hook-use-insertion-effect.json` (config)
- `public/para-que-sirve-el-hook-use-memo.json` (config)
- `public/para-que-sirve-el-hook-use-sync-external-store.json` (config)
- `public/para-que-sirve-el-hook-use-transition-y-cuando-deberias-usarlo.json` (config)
- `public/para-que-sirve-el-metodo-clone-element-de-react.json` (config)
- `public/para-que-sirve-el-metodo-render-to-readable-stream.json` (config)
- `public/por-que-debemos-utilizar-una-funcion-para-actualizar-el-estado-de-react.json` (config)
- `public/por-que-es-recomendable-exportar-los-componentes-de-react-de-forma-nombrada.json` (config)
- `public/por-que-es-recomendable-usar-fragment-en-vez-de-un-div.json` (config)
- `public/por-que-no-podemos-usar-un-if-en-el-renderizado-de-un-componente.json` (config)
- `public/por-que-puede-ser-mala-idea-pasar-siempre-todas-las-props-de-un-objeto-a-un-componente.json` (config)
- `public/por-que-puede-ser-mala-practica-usar-el-index-como-key-en-un-listado-de-react.json` (config)
- `public/por-que-strict-mode-renderiza-dos-veces-la-aplicacion.json` (config)
- `public/puedes-poner-un-ejemplo-de-efectos-colaterales-en-react.json` (config)
- `public/que-diferencia-existe-entre-shadow-dom-y-virtual-dom.json` (config)
- `public/que-diferencia-hay-entre-componentes-controlados-y-no-controlados-que-ventajas-y-desventajas-tienen.json` (config)
- `public/que-diferencia-hay-entre-componentes-de-servidor-y-componentes-de-cliente-en-react-next-js.json` (config)
- `public/que-diferencia-hay-entre-props-y-state.json` (config)
- `public/que-diferencia-hay-entre-react-dom-render-create-root-y-hydrate-root.json` (config)
- `public/que-diferencia-hay-entre-render-to-static-node-stream-y-render-to-pipeable-stream.json` (config)
- `public/que-diferencia-hay-entre-use-effect-y-use-layout-effect.json` (config)
- `public/que-es-el-binding.json` (config)
- `public/que-es-el-ciclo-de-vida-de-un-componente-en-react.json` (config)
- `public/que-es-el-compound-components-pattern.json` (config)
- `public/que-es-el-contexto-en-react-como-puedo-crearlo-y-consumirlo.json` (config)
- `public/que-es-el-estado-en-react.json` (config)
- `public/que-es-el-hook-use-debug-value.json` (config)
- `public/que-es-el-hook-use-form-state-y-cuando-conviene-usarlo.json` (config)
- `public/que-es-el-profiler-en-react.json` (config)
- `public/que-es-el-renderizado-condicional-en-react.json` (config)
- `public/que-es-el-renderizado-de-listas-en-react.json` (config)
- `public/que-es-el-server-side-rendering-y-que-ventajas-tiene.json` (config)
- `public/que-es-el-strict-mode-en-react.json` (config)
- `public/que-es-el-synthetic-event-en-react.json` (config)
- `public/que-es-flush-sync-en-react.json` (config)
- `public/que-es-flux.json` (config)
- `public/que-es-jsx.json` (config)
- `public/que-es-la-funcion-use-en-react-y-para-que-se-utiliza.json` (config)
- `public/que-es-la-hidratacion-hydration-en-react.json` (config)
- `public/que-es-react-dom.json` (config)
- `public/que-es-react.json` (config)
- `public/que-es-un-componente.json` (config)
- `public/que-es-y-para-que-sirve-la-prop-children-en-react.json` (config)
- `public/que-hace-el-hook-use-effect.json` (config)
- `public/que-hace-el-hook-use-id.json` (config)
- `public/que-hace-el-hook-use-layout-effect.json` (config)
- `public/que-hace-el-hook-use-state.json` (config)
- `public/que-java-script-necesito-para-aprender-react.json` (config)
- `public/que-problema-resuelve-el-hook-use-optimistic.json` (config)
- `public/que-problemas-crees-que-pueden-aparecer-en-una-aplicacion-al-querer-visualizar-listas-de-miles-millones-de-datos.json` (config)
- `public/que-quiere-decir-warning-each-child-in-a-list-should-have-a-unique-key-prop.json` (config)
- `public/que-significa-exactamente-que-sea-declarativo.json` (config)
- `public/que-significa-la-expresion-subir-el-estado.json` (config)
- `public/que-solucion-es-implementarias-para-evitar-problemas-de-rendimiento-al-trabajar-con-listas-de-miles-millones-de-datos.json` (config)
- `public/que-son-las-forward-refs.json` (config)
- `public/que-son-las-props-en-react.json` (config)
- `public/que-son-las-refs-en-react.json` (config)
- `public/que-son-las-render-props.json` (config)
- `public/que-son-las-server-actions-y-como-se-usan-con-formularios-en-react.json` (config)
- `public/que-son-los-componentes-stateless.json` (config)
- `public/que-son-los-error-boundaries-en-react.json` (config)
- `public/que-son-los-fragments-en-react.json` (config)
- `public/que-son-los-high-order-components-hoc.json` (config)
- `public/que-son-los-hooks.json` (config)
- `public/que-son-los-portales-en-react.json` (config)
- `public/que-son-mejores-los-componentes-de-clase-o-los-componentes-funcionales.json` (config)
- `public/quiz/qa/can-t-perform-a-react-state-update-on-an-unmounted-component.json` (config)
- `public/quiz/qa/cant-perform-a-react-state-update-on-an-unmounted-component.json` (config)
- `public/quiz/qa/como-anadir-un-evento-a-un-componente-en-react.json` (config)
- `public/quiz/qa/como-crear-un-componente-en-react.json` (config)
- `public/quiz/qa/como-crear-un-hook-personalizado-custom-hook.json` (config)
- `public/quiz/qa/como-funciona-el-hook-use-form-status-y-que-aporta-junto-a-las-server-actions.json` (config)
- `public/quiz/qa/como-funciona-el-hook-use-ref.json` (config)
- `public/quiz/qa/como-funciona-react-memo-y-cuando-es-util.json` (config)
- `public/quiz/qa/como-mantener-los-componentes-puros-y-que-ventajas-tiene.json` (config)
- `public/quiz/qa/como-podemos-ejecutar-codigo-cuando-el-componente-se-desmonta-del-arbol.json` (config)
- `public/quiz/qa/como-podemos-ejecutar-codigo-cuando-el-componente-se-monta.json` (config)
- `public/quiz/qa/como-puedes-abortar-una-peticion-fetch-con-use-effect-en-react.json` (config)
- `public/quiz/qa/como-puedes-acceder-al-evento-nativo-del-navegador-en-react.json` (config)
- `public/quiz/qa/como-puedes-aplicar-clases-css-a-un-componente-en-react-y-por-que-no-se-puede-usar-class.json` (config)
- `public/quiz/qa/como-puedes-aplicar-estilos-en-linea-a-un-componente-en-react.json` (config)
- `public/quiz/qa/como-puedes-cancelar-una-peticion-a-una-api-en-use-effect-correctamente.json` (config)
- `public/quiz/qa/como-puedes-crear-un-server-side-rendering-con-react-desde-cero.json` (config)
- `public/quiz/qa/como-puedes-escribir-comentarios-en-react.json` (config)
- `public/quiz/qa/como-puedes-evitar-re-renders-innecesarios-al-usar-context.json` (config)
- `public/quiz/qa/como-puedes-exportar-multiples-componentes-de-un-mismo-archivo.json` (config)
- `public/quiz/qa/como-puedes-inicializar-un-proyecto-de-react-desde-cero.json` (config)
- `public/quiz/qa/como-puedes-mejorar-el-rendimiento-del-server-side-rendering-en-react-para-evitar-que-bloquee-el-hilo-principal.json` (config)
- `public/quiz/qa/como-puedes-prevenir-el-comportamiento-por-defecto-de-un-evento-en-react.json` (config)
- `public/quiz/qa/como-puedes-registrar-un-evento-en-la-fase-de-captura-en-react.json` (config)
- `public/quiz/qa/como-puedo-aplicar-estilos-de-forma-condicional-a-un-componente-en-react.json` (config)
- `public/quiz/qa/como-puedo-hacer-testing-de-un-componente.json` (config)
- `public/quiz/qa/como-puedo-hacer-testing-de-un-hook.json` (config)
- `public/quiz/qa/como-puedo-importar-de-forma-dinamica-un-componente-en-react.json` (config)
- `public/quiz/qa/como-puedo-inyectar-html-directamente-en-un-componente-de-react.json` (config)
- `public/quiz/qa/como-puedo-pasar-un-parametro-a-una-funcion-que-maneja-un-evento-en-react.json` (config)
- `public/quiz/qa/como-puedo-validar-el-tipo-de-mis-props.json` (config)
- `public/quiz/qa/como-puedo-validar-las-propiedades-de-un-array-con-prop-types.json` (config)
- `public/quiz/qa/como-puedo-validar-las-propiedades-de-un-objeto-con-prop-types.json` (config)
- `public/quiz/qa/como-se-complementan-use-memo-use-callback-use-transition-y-use-deferred-value-para-optimizar-el-rendimiento.json` (config)
- `public/quiz/qa/como-se-puede-renderizar-un-context-desde-un-server-component.json` (config)
- `public/quiz/qa/como-se-transforma-el-jsx.json` (config)
- `public/quiz/qa/como-suscribirse-a-un-evento-en-use-effect.json` (config)
- `public/quiz/qa/cual-es-el-proposito-del-atributo-key-en-react-y-por-que-es-importante-usarlo-correctamente-al-renderizar-listas-de-elementos.json` (config)
- `public/quiz/qa/cual-es-la-diferencia-entre-componente-y-elemento-en-react.json` (config)
- `public/quiz/qa/cual-es-la-diferencia-entre-la-prop-action-y-el-atributo-form-action-en-react-next-js.json` (config)
- `public/quiz/qa/cual-es-la-diferencia-entre-use-callback-y-use-memo.json` (config)
- `public/quiz/qa/cuales-son-las-caracteristicas-principales-de-react.json` (config)
- `public/quiz/qa/cuales-son-las-reglas-de-los-hooks-en-react.json` (config)
- `public/quiz/qa/cuando-y-por-que-es-recomendable-importar-componentes-de-forma-dinamica.json` (config)
- `public/quiz/qa/cuantos-use-effect-puede-tener-un-componente.json` (config)
- `public/quiz/qa/en-react-19-se-necesita-todavia-forward-ref.json` (config)
- `public/quiz/qa/es-buena-idea-usar-siempre-use-callback-para-optimizar-nuestros-componentes.json` (config)
- `public/quiz/qa/es-buena-idea-usar-siempre-use-memo-para-optimizar-nuestros-componentes.json` (config)
- `public/quiz/qa/es-react-una-biblioteca-o-un-framework-por-que.json` (config)
- `public/quiz/qa/explica-casos-de-uso-del-hook-use-effect.json` (config)
- `public/quiz/qa/para-que-sirve-add-transition-type.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-action-state.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-callback.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-deferred-value.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-imperative-handle.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-insertion-effect.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-memo.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-sync-external-store.json` (config)
- `public/quiz/qa/para-que-sirve-el-hook-use-transition-y-cuando-deberias-usarlo.json` (config)
- `public/quiz/qa/para-que-sirve-el-metodo-clone-element-de-react.json` (config)
- `public/quiz/qa/para-que-sirve-el-metodo-render-to-readable-stream.json` (config)
- `public/quiz/qa/por-que-debemos-utilizar-una-funcion-para-actualizar-el-estado-de-react.json` (config)
- `public/quiz/qa/por-que-es-recomendable-exportar-los-componentes-de-react-de-forma-nombrada.json` (config)
- `public/quiz/qa/por-que-es-recomendable-usar-fragment-en-vez-de-un-div.json` (config)
- `public/quiz/qa/por-que-no-podemos-usar-un-if-en-el-renderizado-de-un-componente.json` (config)
- `public/quiz/qa/por-que-no-se-debe-mutar-el-estado-directamente-en-react.json` (config)
- `public/quiz/qa/por-que-puede-ser-mala-idea-pasar-siempre-todas-las-props-de-un-objeto-a-un-componente.json` (config)
- `public/quiz/qa/por-que-puede-ser-mala-practica-usar-el-index-como-key-en-un-listado-de-react.json` (config)
- `public/quiz/qa/por-que-strict-mode-renderiza-dos-veces-la-aplicacion.json` (config)
- `public/quiz/qa/puedes-poner-un-ejemplo-de-efectos-colaterales-en-react.json` (config)
- `public/quiz/qa/que-cambia-en-las-transitions-independientes-de-react-19-3.json` (config)
- `public/quiz/qa/que-diferencia-existe-entre-shadow-dom-y-virtual-dom.json` (config)
- `public/quiz/qa/que-diferencia-hay-entre-componentes-controlados-y-no-controlados-que-ventajas-y-desventajas-tienen.json` (config)
- `public/quiz/qa/que-diferencia-hay-entre-componentes-de-servidor-y-componentes-de-cliente-en-react-next-js.json` (config)
- `public/quiz/qa/que-diferencia-hay-entre-props-y-state.json` (config)
- `public/quiz/qa/que-diferencia-hay-entre-react-dom-render-create-root-y-hydrate-root.json` (config)
- `public/quiz/qa/que-diferencia-hay-entre-render-to-static-node-stream-y-render-to-pipeable-stream.json` (config)
- `public/quiz/qa/que-diferencia-hay-entre-use-effect-y-use-layout-effect.json` (config)
- `public/quiz/qa/que-es-concurrent-react-y-que-problemas-resuelve.json` (config)
- `public/quiz/qa/que-es-el-batching-de-actualizaciones-de-estado-en-react.json` (config)
- `public/quiz/qa/que-es-el-binding.json` (config)
- `public/quiz/qa/que-es-el-ciclo-de-vida-de-un-componente-en-react.json` (config)
- `public/quiz/qa/que-es-el-componente-view-transition-en-react.json` (config)
- `public/quiz/qa/que-es-el-compound-components-pattern.json` (config)
- `public/quiz/qa/que-es-el-contexto-en-react-como-puedo-crearlo-y-consumirlo.json` (config)
- `public/quiz/qa/que-es-el-estado-derivado-y-por-que-conviene-calcularlo-en-el-render.json` (config)
- `public/quiz/qa/que-es-el-estado-en-react.json` (config)
- `public/quiz/qa/que-es-el-hook-use-debug-value.json` (config)
- `public/quiz/qa/que-es-el-hook-use-form-state-y-cuando-conviene-usarlo.json` (config)
- `public/quiz/qa/que-es-el-profiler-en-react.json` (config)
- `public/quiz/qa/que-es-el-react-compiler-y-que-ventajas-aporta.json` (config)
- `public/quiz/qa/que-es-el-renderizado-condicional-en-react.json` (config)
- `public/quiz/qa/que-es-el-renderizado-de-listas-en-react.json` (config)
- `public/quiz/qa/que-es-el-server-side-rendering-y-que-ventajas-tiene.json` (config)
- `public/quiz/qa/que-es-el-strict-mode-en-react.json` (config)
- `public/quiz/qa/que-es-el-synthetic-event-en-react.json` (config)
- `public/quiz/qa/que-es-el-virtual-dom.json` (config)
- `public/quiz/qa/que-es-flush-sync-en-react.json` (config)
- `public/quiz/qa/que-es-flux.json` (config)
- `public/quiz/qa/que-es-jsx.json` (config)
- `public/quiz/qa/que-es-la-composicion-de-componentes-y-por-que-react-la-prefiere-a-la-herencia.json` (config)
- `public/quiz/qa/que-es-la-funcion-use-en-react-y-para-que-se-utiliza.json` (config)
- `public/quiz/qa/que-es-la-hidratacion-hydration-en-react.json` (config)
- `public/quiz/qa/que-es-la-reconciliacion-reconciliation-en-react.json` (config)
- `public/quiz/qa/que-es-react-dom.json` (config)
- `public/quiz/qa/que-es-react-fiber.json` (config)
- `public/quiz/qa/que-es-react-lazy-y-como-se-combina-con-suspense.json` (config)
- `public/quiz/qa/que-es-react.json` (config)
- `public/quiz/qa/que-es-start-transition-y-en-que-se-diferencia-de-actualizar-el-estado-de-forma-normal.json` (config)
- `public/quiz/qa/que-es-suspense-en-react-y-para-que-se-usa.json` (config)
- `public/quiz/qa/que-es-un-componente.json` (config)
- `public/quiz/qa/que-es-una-stale-closure-y-como-afecta-a-los-hooks.json` (config)
- `public/quiz/qa/que-es-y-para-que-sirve-la-prop-children-en-react.json` (config)
- `public/quiz/qa/que-hace-el-hook-use-effect.json` (config)
- `public/quiz/qa/que-hace-el-hook-use-id.json` (config)
- `public/quiz/qa/que-hace-el-hook-use-layout-effect.json` (config)
- `public/quiz/qa/que-hace-el-hook-use-reducer.json` (config)
- `public/quiz/qa/que-hace-el-hook-use-state.json` (config)
- `public/quiz/qa/que-hace-la-api-browser-de-react-dom.json` (config)
- `public/quiz/qa/que-java-script-necesito-para-aprender-react.json` (config)
- `public/quiz/qa/que-problema-resuelve-el-hook-use-optimistic.json` (config)
- `public/quiz/qa/que-problemas-crees-que-pueden-aparecer-en-una-aplicacion-al-querer-visualizar-listas-de-miles-millones-de-datos.json` (config)
- `public/quiz/qa/que-provoca-un-re-render-en-un-componente-de-react.json` (config)
- `public/quiz/qa/que-quiere-decir-warning-each-child-in-a-list-should-have-a-unique-key-prop.json` (config)
- `public/quiz/qa/que-significa-exactamente-que-sea-declarativo.json` (config)
- `public/quiz/qa/que-significa-la-expresion-subir-el-estado.json` (config)
- `public/quiz/qa/que-solucion-es-implementarias-para-evitar-problemas-de-rendimiento-al-trabajar-con-listas-de-miles-millones-de-datos.json` (config)
- `public/quiz/qa/que-son-las-forward-refs.json` (config)
- `public/quiz/qa/que-son-las-fragment-refs-y-que-problemas-resuelven.json` (config)
- `public/quiz/qa/que-son-las-props-en-react.json` (config)
- `public/quiz/qa/que-son-las-refs-en-react.json` (config)
- `public/quiz/qa/que-son-las-render-props.json` (config)
- `public/quiz/qa/que-son-las-server-actions-y-como-se-usan-con-formularios-en-react.json` (config)
- `public/quiz/qa/que-son-los-componentes-stateless.json` (config)
- `public/quiz/qa/que-son-los-error-boundaries-en-react.json` (config)
- `public/quiz/qa/que-son-los-fragments-en-react.json` (config)
- `public/quiz/qa/que-son-los-high-order-components-hoc.json` (config)
- `public/quiz/qa/que-son-los-hooks.json` (config)
- `public/quiz/qa/que-son-los-portales-en-react.json` (config)
- `public/quiz/qa/que-son-mejores-los-componentes-de-clase-o-los-componentes-funcionales.json` (config)
- `public/quiz/qa/que-son-trusted-types-y-como-los-soporta-react-19-3.json` (config)
- `public/quiz/qa/react-hook-use-xxx-is-called-conditionally-react-hooks-must-be-called-in-the-exact-same-order-in-every-component-render.json` (config)
- `public/quiz/qa/se-puede-inicializar-un-estado-con-el-valor-de-una-prop-que-pasa-si-lo-haces-y-que-hay-que-tener-en-cuenta.json` (config)
- `public/quiz/qa/solo-se-pueden-cargar-componentes-de-forma-dinamica-si-se-exportan-por-defecto.json` (config)
- `public/quiz/qa/too-many-re-renders-react-limits-the-number-of-renders-to-prevent-an-infinite-loop.json` (config)
- `public/react-hook-use-xxx-is-called-conditionally-react-hooks-must-be-called-in-the-exact-same-order-in-every-component-render.json` (config)
- `public/se-puede-inicializar-un-estado-con-el-valor-de-una-prop-que-pasa-si-lo-haces-y-que-hay-que-tener-en-cuenta.json` (config)
- `public/solo-se-pueden-cargar-componentes-de-forma-dinamica-si-se-exportan-por-defecto.json` (config)
- `public/too-many-re-renders-react-limits-the-number-of-renders-to-prevent-an-infinite-loop.json` (config)
- `skills-lock.json` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `public` — 414 analysed file(s)
- `.agents` — 137 analysed file(s)
- `src` — 28 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `manuscript` — 8 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `book` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `99d805f10ac5d3e0ad436a0458bc33f3596c9375` is the revision these paths and observations refer to.
