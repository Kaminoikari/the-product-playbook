# Etapa 2: Definición — Convergencia del Problema

> **Nota: Qué pasos ejecutar por modo está definido autoritativamente por las "Secuencias de Pasos por Modo" en SKILL.md. Lo siguiente es solo de referencia.**

**Modo completo / alta completitud → Hacer todo (2.1 ~ 2.4)**
**Completitud media → 2.1 + 2.3 + 2.4**
**Modo rápido / baja completitud → Solo 2.3 (un HMW central)**

Antes de entrar a esta etapa, confirma las tres preguntas fundamentales del producto: ¿Para quién es? / ¿Por qué construirlo? / ¿Qué es?

## 2.1 Tabla de Resumen de Puntos de Dolor

Extrae puntos de dolor de todas las Personas y User Journey Maps:

```
| # | Descripción del Punto de Dolor | Persona de Origen | Aparece en Etapa | Nivel de Impacto (Alto/Medio/Bajo) | Frecuencia (Alta/Media/Baja) |
|---|---|---|---|---|---|
| P1 | | | | | |
| P2 | | | | | |
```

## 2.2 Framework de Posicionamiento de April Dunford

**Aplicable: Completitud media/alta / audiencia es ejecutivos/ventas/marketing**

El posicionamiento no es un eslogan — es decidir dónde compites y para quién:

```
| Elemento de Posicionamiento | Pregunta | Tu Respuesta |
|-----------------------------|----------|-------------|
| Alternativas Competitivas | Si tu producto no existiera, ¿qué usarían los usuarios? (La respuesta real, no quién crees que son tus competidores) | |
| Atributos Únicos | ¿Qué tienes que las alternativas competitivas no tienen? | |
| Valor para los Usuarios | ¿Qué valor tangible entregan estos atributos únicos a los usuarios? | |
| Características del Mercado Objetivo | ¿Qué usuarios se preocupan más por este valor? (Mientras más específico, mejor) | |
| Categoría de Mercado | ¿Qué marco de mercado posiciona mejor tu producto? (El marco determina los criterios competitivos) | |
```

Errores de posicionamiento más comunes:
- Tratar funcionalidades como posicionamiento ("¡Tenemos IA!" no es posicionamiento)
- Posicionamiento demasiado amplio — cubrir a todos significa no cubrir a nadie
- Usar a tus competidores percibidos como referencia en lugar de las alternativas reales del usuario

### 📝 Lista de Verificación de Calidad de Posicionamiento
- ✅ ¿Las "alternativas competitivas" son desde la perspectiva del usuario? (Lo que los usuarios realmente usan en su lugar, no quién crees que son tus competidores)
- ✅ ¿Los "atributos únicos" son cosas que las alternativas competitivas no pueden hacer o no hacen bien? (No cosas que ambos tienen)
- ✅ ¿El "valor para los usuarios" está expresado en lenguaje del usuario o del producto? ("Ahorra 2 horas" vs. "Automatización potenciada por IA")
- ✅ ¿El "mercado objetivo" es lo suficientemente específico para realmente encontrar a estas personas?
- ✅ ¿Los cinco elementos de posicionamiento son lógicamente consistentes?
- ❌ Problemas comunes: Desconexión entre atributos únicos y valor, categoría de mercado incorrecta llevando a ser juzgado por criterios equivocados

## 2.3 Reformulación de Problemas HMW (How Might We)

Transforma los puntos de dolor en preguntas HMW, combinando la perspectiva JTBD para confirmar el tipo de job detrás de cada HMW:

```
| Punto de Dolor # | Punto de Dolor | Tipo JTBD Correspondiente | Pregunta HMW |
|---|---|---|---|
| P1 | [Descripción del punto de dolor] | Funcional / Emocional / Social | ¿Cómo podríamos... |
| P2 | [Descripción del punto de dolor] | | ¿Cómo podríamos... |
```

Principio de granularidad HMW:
- Demasiado amplio ("Cómo hacer usuarios más felices") → Sin dirección
- Justo ("Cómo permitir que los usuarios completen la primera configuración en 60 segundos") → Con restricciones pero abierto
- Demasiado estrecho ("Cómo cambiar el color del botón") → Limita posibilidades

### 📝 Lista de Verificación de Calidad HMW
- ✅ ¿Tiene restricciones claras? (No completamente abierto)
- ✅ ¿Deja suficiente espacio para múltiples soluciones? (No apunta a una sola respuesta)
- ✅ ¿Puede mapearse directamente a un JTBD o punto de dolor?
- ✅ ¿El equipo puede empezar a generar soluciones al ver este HMW?
- ❌ Problemas comunes: Demasiado amplio (reformula la visión), demasiado estrecho (especifica la solución), múltiples problemas mezclados

**Ejemplos:**
- ❌ Demasiado amplio: "¿Cómo podríamos hacer que los usuarios estén más satisfechos?"
- ✅ Justo: "¿Cómo podríamos ayudar a los compradores de vivienda primerizos a calcular el monto de hipoteca que pueden pagar en 3 minutos?"
- ❌ Demasiado estrecho: "¿Cómo podríamos agregar una calculadora de hipoteca a la página principal?"

## 2.4 Tabla de Evaluación de Oportunidades

Prioriza las preguntas HMW:

```
| Pregunta HMW | Persona Afectada | Tamaño de Persona | Impacto al Usuario (1-5) | Valor de Negocio (1-5) | Factibilidad (1-5) | Total | Prioridad |
|---|---|---|---|---|---|---|---|
| | [Lista de Personas afectadas] | [Grande/Medio/Pequeño] | | | | | |
```

**Definiciones de Escala de Puntuación:**

| Puntuación | Impacto al Usuario | Valor de Negocio | Factibilidad |
|-----------|-------------------|-----------------|-------------|
| 1 | Inconveniencia menor para pocos usuarios | Retorno indirecto, a largo plazo como mucho | Requiere tecnología completamente nueva o I+D extensiva |
| 2 | Algunos usuarios encuentran ocasionalmente | Puede mover indirectamente algunas métricas | Requiere construcción significativa de nueva capacidad (3+ meses) |
| 3 | TA central lo encuentra regularmente | Impacto positivo en métricas clave | Requiere algo de desarrollo nuevo pero técnicamente factible (1-3 meses) |
| 4 | Muchos usuarios lo encuentran frecuentemente | Impulsa directamente crecimiento de usuarios o retención | Dentro de las capacidades del equipo actual, 2-4 semanas |
| 5 | Muchos usuarios no pueden completar tareas centrales diariamente | Impulsa directamente ingresos o impacta significativamente la North Star Metric | El equipo actual puede completar en dos semanas |

**Pensamiento de Costo de Oportunidad de Shreyas Doshi:**

No preguntes "¿Cuál es el ROI de esta funcionalidad?" En su lugar, pregunta:

> "Si invierto recursos en A, estoy renunciando a la oportunidad de invertir en B. ¿Estoy seguro de que A vale más la pena que B?"

El pensamiento de ROI evalúa si una sola oportunidad vale la pena; el pensamiento de costo de oportunidad te ayuda a tomar mejores decisiones entre todas las oportunidades.

**Recordatorio de Enfoque 0-a-1:** Después de completar la evaluación de oportunidades, se recomienda elegir **solo una pregunta HMW de máxima prioridad** como el núcleo del MVP. (Facebook: estudiantes universitarios → preparatorianos → todos; página de perfil → fotos → feed de noticias)

---

## 📎 Consejos de Integración de Archivos para esta Etapa

| Contenido Subido | Integrar En | Acción de Integración |
|-----------------|-------------|----------------------|
| Capturas de pantalla de competidores / reportes de análisis competitivo | 2.2 Posicionamiento | Llenar campos "alternativas competitivas" y "atributos únicos"; comparar diferenciación |
| Reportes de mercado (PDF) | 2.4 Evaluación de Oportunidades | Usar datos de mercado para validar tamaño de Persona y puntuaciones de valor de negocio |
| Datos de NPS / encuestas de satisfacción | 2.1 Resumen de Puntos de Dolor | Reemplazar niveles de impacto y frecuencias asumidos con puntuaciones reales |
| Resúmenes de soporte al cliente / tickets | 2.1 Resumen de Puntos de Dolor + 2.3 HMW | Contar frecuencia de puntos de dolor; convertir tickets de alta frecuencia directamente en preguntas HMW |
