# Prompting en Habit Coach API

## Qué es prompting en este proyecto

Prompting es la forma en que la API organiza instrucciones para simular respuestas de un asistente de hábitos. En lugar de enviar texto suelto, cada endpoint construye un prompt con rol, contexto, instrucciones, formato esperado y restricciones.

En esta versión no se conecta una API externa de IA. Los prompts quedan preparados para una futura integración.

## Uso de roles

Los prompts asignan un rol claro al asistente. Por ejemplo:

```text
Actúa como Habit Coach API, un asistente especializado en crear planes de hábitos simples, realistas y sostenibles.
```

Esto ayuda a orientar el tono, el alcance y la responsabilidad de la respuesta.

## Uso de contexto del usuario

La API agrega datos enviados por el usuario al prompt:

- Objetivo personal.
- Nivel actual.
- Tiempo disponible.
- Hábitos completados.
- Hábitos no completados.
- Notas personales.

Con ese contexto, la respuesta simulada puede ser más personalizada y coherente.

## Respuestas estructuradas en JSON

Los prompts piden salidas con estructura clara, por ejemplo:

```json
{
  "habits": [],
  "weekly_plan": {},
  "recommendations": []
}
```

Este formato es útil porque una API debe devolver datos predecibles y fáciles de procesar.

## Mejora de un prompt básico

Un prompt básico suele ser ambiguo:

```text
Actúa como coach y dame hábitos
```

El endpoint `/improve-prompt` lo mejora agregando:

- Rol específico.
- Contexto del objetivo.
- Instrucciones numeradas.
- Formato de salida.
- Restricciones para evitar respuestas vagas.

## Ejemplo de prompt inicial

```text
Actúa como coach y dame hábitos
```

## Ejemplo de prompt mejorado

```text
Actúa como un coach de hábitos especializado en crear planes claros, realistas y medibles.

Contexto: el usuario necesita obtener una respuesta más estructurada y en formato JSON.
Prompt original a mejorar: Actúa como coach y dame hábitos

Instrucciones:
1. Propón hábitos pequeños y sostenibles.
2. Explica cada recomendación en una frase breve.
3. Organiza la respuesta por secciones.
4. Evita recomendaciones extremas o ambiguas.

Formato de salida esperado en JSON:
{
  "habits": [],
  "weekly_plan": {},
  "recommendations": []
}
```

## Justificación

El prompt mejorado es mejor porque reduce ambigüedad. Define quién responde, qué información debe considerar, cómo debe organizar la salida y qué restricciones debe respetar. Esto mejora la calidad de la respuesta y facilita su uso dentro de una API REST.

