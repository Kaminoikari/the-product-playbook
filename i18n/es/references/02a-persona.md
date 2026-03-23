# Etapa 1: Descubrimiento — Construyendo Personas

## Hábitos de Descubrimiento Continuo (Teresa Torres)

Construye un hábito clave: **Habla con al menos un usuario objetivo cada semana.** El descubrimiento no es un ritual único — es un sistema continuo.

> "El descubrimiento de producto debería ser un hábito continuo, no una ceremonia única antes de que un proyecto comience." — Teresa Torres

## 1.1 Construir la Tabla de Personas

Las Personas no se segmentan por edad y género, sino por **propósito / tarea / motivación** para distinguir diferentes tipos de usuarios.

```
| Campo | Persona 1: [Apodo] | Persona 2: [Apodo] | Persona 3: [Apodo] |
|---|---|---|---|
| Propósito / Tarea / Motivación | | | |
| Tamaño (ESCALA) | | | |
| Problemas / Desafíos / Motivadores | | | |
| Enfoque Actual y Razón | | | |
| Frecuencia | | | |
| Fuentes de Información | | | |
| Barreras de Adopción / Ejecución | | | |
```

Explica la lógica de segmentación; verifica MECE (mutuamente excluyente, colectivamente exhaustivo); identifica el TA primario y secundario.

### 📝 Lista de Verificación de Calidad de Persona
- ✅ ¿La segmentación está basada en "propósito/tarea/motivación" en lugar de datos demográficos?
- ✅ ¿Las Personas son MECE (mutuamente excluyentes y colectivamente exhaustivas del mercado objetivo)?
- ✅ ¿El TA primario vs. secundario está claramente identificado?
- ✅ ¿Los "problemas/desafíos" de cada Persona están basados en observaciones reales o inferencias razonables?
- ✅ ¿El "enfoque actual y razón" es lo suficientemente específico para identificar soluciones alternativas?
- ❌ Problemas comunes: Segmentar por edad/género, diferencias mínimas entre Personas, puntos de dolor demasiado vagos

## 1.2 Construir Tarjetas de Persona

```
## [Apodo de Persona]: [Descripción de una línea]

**Info Básica**: Edad / Género / Ocupación / Ubicación / Rasgos de personalidad
**Contexto**: [Descripción de contexto relevante al producto]
**Metas / Tareas**: [Meta 1], [Meta 2]
**Enfoque Actual y Razón**: [Qué hacen actualmente y por qué]
**Fuentes de Información**: [Dónde obtienen información relevante]
**Barreras / Problemas / Desafíos / Frustraciones**: [Punto de dolor 1], [Punto de dolor 2], [Punto de dolor 3]
```

---

## 📎 Consejos de Integración de Archivos para esta Etapa

Si el usuario sube archivos durante esta etapa, Claude los integra según estas reglas:

| Contenido Subido | Integrar En | Acción de Integración |
|-----------------|-------------|----------------------|
| Transcripciones de entrevistas de usuario / transcripciones de audio | 1.1 Persona + 1.3 JTBD | Extraer: contexto del usuario → campos de Persona; puntos de dolor + enfoque actual → preguntas de profundización JTBD; reacciones emocionales → Jobs emocionales/sociales |
| Reporte de investigación de usuarios (PDF) | 1.1 + 1.2 + 1.3 | Extraer datos cuantitativos (proporciones de segmentos de usuarios) al tamaño de Persona; extraer insights cualitativos a JTBD |
