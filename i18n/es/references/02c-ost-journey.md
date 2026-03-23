# Etapa 1: Descubrimiento — OST + Journey Map

## 1.4 Opportunity Solution Tree (OST)

**Aplicable: Modo completo / alta completitud**

El OST comienza desde el objetivo del producto y conecta sistemáticamente oportunidades con soluciones:

```
[Objetivo del Producto / Resultado Deseado]
    │
    ├── [Oportunidad 1: Punto de dolor o necesidad del usuario]
    │       ├── [Solución 1a]
    │       └── [Solución 1b]
    ├── [Oportunidad 2: Punto de dolor o necesidad del usuario]
    │       └── [Solución 2a]
    └── [Oportunidad 3: Punto de dolor o necesidad del usuario]
            └── [Solución 3a]
```

Principios fundamentales:
- El objetivo (Outcome) es un resultado medible, no una funcionalidad o output
- Las oportunidades vienen de investigación de usuarios, no de lluvia de ideas interna
- Las soluciones se mapean a oportunidades — no saltes las oportunidades e ir directo a soluciones
- Primero amplitud, luego profundidad: lista todas las oportunidades primero, luego explora soluciones una por una

## 1.5 User Journey Map

**Aplicable: Modo completo / alta completitud / audiencia es diseñadores**

**Paso 1: Tabla de Resumen**

```
**[Nombre de Persona] — Tarea: [Descripción de la tarea]**

| Etapa | Comportamiento Central | Emoción | Punto de Dolor Clave |
|---|---|---|---|
| [Etapa 1] | [Descripción de una línea del comportamiento principal] | [Emoción + emoji] | [El punto de dolor más importante] |
```

**Paso 2: Expandir Cada Etapa en Detalle**

```
> **Etapa: [Nombre de la Etapa]**
> - **Haciendo**: [Qué hace realmente el usuario en esta etapa]
> - **Pensando**: [Qué pasa por la mente del usuario, idealmente en primera persona]
> - **Sintiendo**: [Estado emocional y por qué]
> - **Stakeholder**: [Quién está involucrado en esta etapa]
> - **Problema**: [Dificultades o frustraciones específicas]
```

**Paso 3: Agrupación**
- Si las etapas son demasiado granulares, fusiónalas en grupos de etapas más grandes
- Consolida los puntos de dolor a través de las etapas, señala cuáles son los puntos de dolor centrales

---

## 📎 Consejos de Integración de Archivos para esta Etapa

Si el usuario sube archivos durante esta etapa, Claude los integra según estas reglas:

| Contenido Subido | Integrar En | Acción de Integración |
|-----------------|-------------|----------------------|
| Pizarrón / diagramas de flujo dibujados a mano | 1.5 Journey Map | Reconocer el flujo y convertir a tabla estructurada; preservar marcadores de emoción originales |
| Datos de comportamiento de usuario (CSV) | 1.4 OST + 1.5 Journey Map | Usar datos para validar qué rutas de comportamiento son más comunes y qué etapas tienen mayor abandono |
