# 🔄 Secuencia de Pasos del Modo Revisión (12 Pasos + Output Final)

> Este archivo es la definición autoritativa de pasos para el Modo Revisión. Cargado por el despachador central de SKILL.md.

## Secuencia de Pasos

```
Fase 0: Análisis del Estado Actual
  S1.  Revisión del producto existente (resumen de datos de usuario + métricas centrales + problemas conocidos + estado de seguridad)
  S2.  Re-examinar JTBD de usuarios existentes (¿qué jobs se están haciendo bien? ¿cuáles no?)

Fase 1: Convergencia del Problema
  S3.  Recopilación de puntos de dolor de usuario (análisis de retención/churn + síntesis de feedback de usuarios + datos de comportamiento)
  S4.  Tabla de resumen de puntos de dolor → cargar references/03-define.md → 2.1
  S5.  Re-evaluación de posicionamiento → cargar references/03-define.md → 2.2 (enfoque: ¿el posicionamiento necesita ajuste?)
  S6.  Reformulación de preguntas HMW → cargar references/03-define.md → 2.3
  S7.  Tabla de evaluación de oportunidades → cargar references/03-define.md → 2.4

Fase 2: Diseño de Solución
  S8.  PR-FAQ → cargar references/04a-prfaq.md (describir la experiencia post-revisión)
  S9.  Pre-mortem → cargar references/04b-solutions.md → 3.3
  S10. Alcance MVP + Lista de No Hacer → cargar references/04c-mvp.md (enfoque: qué cambiar / qué no cambiar)

Fase 3: Validación
  S11. North Star + Aha Moment → cargar references/05a-northstar-aha.md (comparar métricas pre- vs. post-revisión)
  S12. Plan de validación de hipótesis → cargar references/05c-validation-spec.md
────
Output Final → Resumen de spec de producto (edición de revisión)
```

### Pre-paso S1: Carga de Contexto de Producto

Antes de entrar a S1, cargar `references/rules-context.md` y verificar `.product-context.md`:

- **Contexto completo disponible (Escenario 1)**: Auto-rellenar nivel de PMF, North Star, puntos de dolor conocidos, estado de seguridad, y las 3 entradas más recientes del Historial de Decisiones. La guía de S1 cambia a **modo delta**: "La última vez que evaluamos, tu nivel de PMF era [X] y tu North Star metric era [Y]. ¿Ha cambiado algo? ¿Cuáles son los últimos números de DAU/MAU y retención?" — El historial de decisiones y puntos de dolor recopilados previamente no necesitan re-recopilarse.
- **Sin contexto disponible (Escenario 2)**: Activar Context Bootstrap (`rules-context.md` Sección 4, Ronda 1 + 3), luego proceder a la recopilación estándar de datos de S1 abajo.
- **Contexto parcial (Escenario 3)**: Traer historial de cambios de features del Historial de Decisiones (saber qué módulos fueron cambiados y qué riesgos se identificaron), pero preguntar sobre estrategia general del producto y métricas (el trabajo anterior solo cubrió expansión de features y carece de una visión holística).

### Guía Estándar de S1

> El S1 del Modo Revisión pregunta proactivamente al usuario que proporcione datos del producto existente: DAU/MAU, tasas de retención, feedback clave de usuarios, decisiones de versiones anteriores, etc. Si el contexto ya pre-llenó algunas respuestas, confirmar en lugar de re-recopilar.
> S1 también recopila el estado de seguridad actual: mecanismos de autenticación/autorización existentes, vulnerabilidades de seguridad conocidas o deuda técnica, incidentes de seguridad recientes. Esta información afecta la evaluación de riesgos de la revisión y el Pre-mortem.

### Ruta Rápida

Cuando el usuario proporciona datos suficientes en S1 (incluyendo feedback de usuarios, métricas y puntos de dolor), S4–S7 (puntos de dolor → posicionamiento → HMW → evaluación de oportunidades) pueden producirse en un solo turno de conversación, requiriendo solo una confirmación en lugar de cuatro. Condición de activación: la lista de puntos de dolor recopilada en S3 ya tiene priorización clara y soporte de datos. Las reglas de Hard Gate permanecen sin cambios — el output de cada paso debe presentarse completamente; solo la cadencia de confirmación se acelera.

## Instrucciones de Carga de Referencias

| Paso | Archivo de Referencia |
|------|----------------------|
| S1–S3 | No se necesita referencia externa (guiar al usuario para proporcionar datos directamente) |
| S4–S7 | `references/03-define.md` |
| S8 | `references/04a-prfaq.md` |
| S9 | `references/04b-solutions.md` |
| S10 | `references/04c-mvp.md` |
| S11 | `references/05a-northstar-aha.md` |
| S12 + Output Final | `references/05c-validation-spec.md` |

## Formato del Output Final

**Resumen de Spec de Producto de Revisión**: Comparación antes/después + qué cambiar / qué no cambiar + métricas de éxito

Al completar, ejecuta reglas de fin de flujo según `references/rules-end-of-flow.md`.
