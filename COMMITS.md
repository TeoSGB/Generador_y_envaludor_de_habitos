# Estrategia de commits

## Objetivo

La estrategia de commits del proyecto busca mantener un historial claro, profesional y fácil de revisar. Cada commit debe representar una intención concreta y verificable.

## Tipos de commits

### Commit inicial

Usado para crear la base del proyecto, estructura de carpetas y configuración mínima.

### Commit por endpoint

Cada endpoint importante puede agregarse en un commit propio para facilitar revisión y pruebas.

### Commit por modelos

Los modelos Pydantic deben agruparse cuando agregan contratos de entrada o salida relacionados.

### Commit por servicios

La lógica de negocio debe separarse de las rutas y puede confirmarse en commits específicos.

### Commit por prompts

Las plantillas de prompts deben versionarse porque explican la estrategia de prompting del proyecto.

### Commit por pruebas

Las pruebas automatizadas deben tener commits propios para evidenciar cobertura básica.

### Commit por documentación final

La documentación final debe agruparse en commits de documentación para dejar claro que no cambia la lógica de negocio.

## Lista sugerida de commits

1. `Initial FastAPI project setup`
2. `Add health check endpoint`
3. `Add habit plan generation endpoint`
4. `Add prompt templates`
5. `Add progress evaluation endpoint`
6. `Add prompt improvement endpoint`
7. `Add prompt examples endpoint`
8. `Improve request validations`
9. `Add error handling`
10. `Add pytest test suite`
11. `Update README documentation`
12. `Add prompting documentation`
13. `Add commits strategy documentation`

## Buenas prácticas aplicadas

- Usar mensajes cortos y descriptivos.
- Separar cambios de código, pruebas y documentación.
- Evitar commits gigantes con responsabilidades mezcladas.
- Confirmar cambios después de validar que las pruebas pasan.
- Mantener el historial útil para una evaluación técnica.

