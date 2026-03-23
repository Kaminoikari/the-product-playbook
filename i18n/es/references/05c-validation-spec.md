# Etapa 4: Entrega — Validación de Hipótesis + Resumen de Spec de Producto

## 4.5 Plan de Validación de Hipótesis

**Aplicable: Completitud media/alta / audiencia es científicos de datos/uno mismo**

```
| Hipótesis Central | Método de Validación | Momento de Validación | Criterio de Éxito | Si la hipótesis es incorrecta, vamos a... |
|-------------------|----------------------|----------------------|------------------|------------------------------------------|
| | Entrevistas a usuarios alpha / datos | | | |
```

Principios: Validación cualitativa (entrevistas de usuario, estudios de diario) + validación cuantitativa (datos) tienen igual peso; mantente alerta a tu propio sesgo de confirmación.

## 4.6 Resumen de Spec de Producto

El Resumen de Spec de Producto es el entregable final en todos los modos (el Modo Rápido produce un resumen de dirección de una página — estructura diferente pero mismo espíritu).
El Resumen de Spec de Producto tiene tres secciones, correspondientes a diferentes profundidades de lectura:

### Sección 1: Resumen de Decisiones (Legible en 30 segundos)

```
**Descripción en una línea**: [Titular del PR-FAQ]
**Para Quién**: [Persona objetivo en una oración]
**Valor Central**: [Job funcional JTBD + job emocional, en una oración]
**North Star Metric**: [Nombre de la métrica + definición]
**Nivel PMF Actual**: [Nivel 1-4 + explicación de una oración]
```

### Sección 2: Límites de Ejecución (Legible en 2 minutos)

```
**Declaración JTBD Central**: [Cliente Objetivo] + quiere [Job] + en el contexto de [Contexto del Job]
**Aha Moment**: Cuando el usuario completa [acción], experimenta el valor central. Meta: alcanzarlo dentro de [X].
**Imprescindibles del MVP**: [3-5 funcionalidades/capacidades más críticas]
**No Hacer (Deliberadamente excluido de esta versión)**: [Exclusiones explícitas + razones]
**Hipótesis Clave**: [2-3 hipótesis centrales que necesitan validación]
**Riesgos Principales del Pre-mortem**: [2-3 causas más probables de fracaso]
**Hero Metric**: [1-2 métricas de éxito más importantes + valores objetivo]
```

### Sección 3: Referencia Profunda (Consultar cuando sea necesario)

```
**Desglose JTBD**:
  - Job Funcional:
  - Job Emocional:
  - Job Social:
**Posicionamiento April Dunford**:
  - Alternativas competitivas reales:
  - Nuestros atributos únicos:
  - Valor central para usuarios objetivo:
  - Características del mercado objetivo:
  - Categoría de mercado:
**Pregunta HMW Central**: [De la etapa de Definición]
**Descripción de la Solución**: [Del resumen del PR-FAQ]
**Modelo de Negocio**: [Modelo de ingresos + estrategia de precios, si se completó]
**Estrategia GTM**: [Canal de adquisición inicial + estrategia de lanzamiento, si se completó]
```

Después de completar las tres secciones, Claude **debe agregar proactivamente las siguientes tres secciones** sin esperar a que el usuario las solicite:

---

### ⚠️ Registro de Riesgos

Consolida todos los riesgos identificados a lo largo del proceso de planificación (fuentes: Pre-mortem + Evaluación de Oportunidades + Validación de Hipótesis):

```
| Tipo de Riesgo | Descripción del Riesgo | Severidad (Alta/Media/Baja) | ¿Mitigación Implementada? |
|---------------|----------------------|---------------------------|--------------------------|
| Riesgo de mercado | | | |
| Riesgo de suposición de usuario | | | |
| Riesgo técnico | | | |
| Riesgo competitivo | | | |
| Riesgo de ejecución | | | |
```

---

### 🔍 Brechas y Puntos Ciegos

Claude identifica proactivamente los siguientes tipos de brechas basándose en todo el flujo de conversación:

```
| Tipo | Descripción | Siguiente Paso Recomendado |
|------|------------|---------------------------|
| Pasos no ejecutados | [Qué frameworks se omitieron y qué puntos ciegos puede causar] | |
| Datos insuficientes | [Qué decisiones están basadas en suposiciones en lugar de datos reales de usuarios] | |
| Saltos lógicos | [Dónde el razonamiento carece de evidencia intermedia] | |
| Hipótesis no validadas | [Lista de todas las hipótesis centrales sin método de validación aún] | |
| Definiciones poco claras | [Qué conceptos necesitan definición más precisa antes de la ejecución] | |
```

---

### 💡 Recomendaciones Adicionales

Claude proporciona 3-5 recomendaciones específicas y accionables basadas en las características del producto, etapa y riesgos conocidos:

```
1. [Máxima prioridad]: [Acción específica] — Justificación: [Por qué esto importa más]
2. [Segunda prioridad]: [Acción específica] — Justificación:
3. [Tercera prioridad]: [Acción específica] — Justificación:
...
```

Las recomendaciones pueden cubrir: métodos de validación con usuarios, ajustes de límites del MVP, estrategia competitiva, diseño de métricas, asignación de equipo, prioridades del próximo hito.

---

## 📎 Consejos de Integración de Archivos para esta Etapa

| Contenido Subido | Integrar En | Acción de Integración |
|-----------------|-------------|----------------------|
| Datos de comportamiento de usuario (CSV / Excel) | 4.2 North Star + 4.3 PMF | Usar datos reales de retención y engagement para evaluar nivel de PMF; calibrar línea base de North Star |
| Resultados de encuesta Sean Ellis | 4.3 PMF + 4.2 Señales de Tres Capas | Calcular Score directamente, llenar en Capa 3 |
