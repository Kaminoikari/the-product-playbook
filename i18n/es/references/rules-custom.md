# ✏️ Secuencia de Pasos del Modo Personalizado

> Este archivo es la definición autoritativa de pasos para el Modo Personalizado. Cargado por el despachador central de SKILL.md.

Basado en el nivel de completitud seleccionado por el usuario:

## 🔴 Bajo (Lean) — 4 Pasos

```
S1. Declaración JTBD → cargar references/02b-jtbd.md
S2. Un HMW → cargar references/03-define.md → 2.3
S3. PR-FAQ → cargar references/04a-prfaq.md
S4. North Star → cargar references/05a-northstar-aha.md
(Cualquier paso puede ser intercambiado por el usuario por un framework diferente)
────
Output Final → Resumen de spec de producto (campos no ejecutados marcados "No ejecutado")
```

## 🟡 Medio (Estándar) — 10 Pasos

```
S1.  Tabla de Personas + Tarjeta de Persona → cargar references/02a-persona.md
S2.  Análisis JTBD → cargar references/02b-jtbd.md
S3.  Tabla de Resumen de Puntos de Dolor → cargar references/03-define.md
S4.  Reformulación de Preguntas HMW → cargar references/03-define.md
S5.  Posicionamiento April Dunford → cargar references/03-define.md
S6.  PR-FAQ → cargar references/04a-prfaq.md
S7.  Soluciones Paralelas + MVP + Lista de No Hacer → cargar references/04b-solutions.md + references/04c-mvp.md
S8.  North Star + Señales de Tres Capas + Aha Moment → cargar references/05a-northstar-aha.md
S9.  Evaluación de Nivel PMF → cargar references/05b-pmf-gtm.md
S10. Resumen de Spec de Producto → cargar references/05c-validation-spec.md
```

## 🟢 Alto (Integral) — 16 Pasos

```
S1.  Strategy Blocks + Rumelt → cargar references/01-strategy.md
S2.  Tabla de Personas + Tarjeta de Persona → cargar references/02a-persona.md
S3.  Análisis JTBD → cargar references/02b-jtbd.md
S4.  OST Opportunity Solution Tree → cargar references/02c-ost-journey.md
S5.  User Journey Map → cargar references/02c-ost-journey.md
S6.  Tabla de Resumen de Puntos de Dolor → cargar references/03-define.md
S7.  HMW + Posicionamiento April Dunford → cargar references/03-define.md
S8.  Tabla de Evaluación de Oportunidades → cargar references/03-define.md
S9.  PR-FAQ → cargar references/04a-prfaq.md
S10. Prototipos Paralelos → cargar references/04b-solutions.md
S11. Pre-mortem → cargar references/04b-solutions.md
S12. GEM + RICE → cargar references/04b-solutions.md
S13. MVP + Lista de No Hacer → cargar references/04c-mvp.md
S14. North Star + Señales de Tres Capas + Aha Moment → cargar references/05a-northstar-aha.md
S15. Plan de Validación de Hipótesis → cargar references/05c-validation-spec.md
S16. Resumen de Spec de Producto → cargar references/05c-validation-spec.md
```

## Reglas de Carga de Referencias

Al entrar a cada paso, solo carga el archivo de referencia correspondiente (no pre-cargar todos los archivos). Cada paso arriba tiene su ruta de referencia anotada.

## Formato del Output Final

**Resumen de Spec de Producto** (solo integra pasos completados; campos no ejecutados se marcan "No ejecutado")

Al completar, ejecuta reglas de fin de flujo según `references/rules-end-of-flow.md`.
