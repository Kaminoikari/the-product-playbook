# Output de Reporte HTML de Planificación de Producto

Se activa cuando el usuario dice "produce un reporte" o confirma que el contenido de la última etapa es correcto.

## Especificaciones de Diseño

Usa un **estilo de diseño moderno** — un único archivo HTML (CSS y JS completamente inline), asegurando que sea legible sin conexión.

**Estilo General:**
- Sección Hero con fondo degradado (con etiquetas de modo, audiencia, fecha)
- Diseño basado en tarjetas (bordes redondeados + sombras), cada sección como una tarjeta de información independiente
- Jerarquía tipográfica clara y espaciado de lectura cómodo
- Diseño responsive, lectura fluida en móvil

**Paleta de Colores:**
- Primario: Azul profundo `#1a1a2e` → `#16213e` → `#0f3460`
- Acento: `#e94560` o `#533483`
- Fondo de área de contenido: `#f8f9fa`, tarjetas: blanco con `box-shadow`

**Fuente:** Cargar Inter de Google Fonts CDN primero, fallback a fuentes del sistema:
```css
/* En <head> */
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">

/* En CSS */
font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
```
> Esta es la única dependencia CDN externa permitida. Si Google Fonts no está disponible, la página se renderizará correctamente de todos modos.

## Estructura de Página (Renderizado dinámico basado en etapas completadas)

```
┌──────────────────────────────────────────────────────────────┐
│  Sección Hero (Nombre del producto, descripción, modo,       │
│  audiencia, fecha)                                           │
├──────────────────────────────────────────────────────────────┤
│  Navegación de Tabla de Contenidos (Sticky, solo muestra     │
│  completadas)                                                │
├──────────────────────────────────────────────────────────────┤
│  🧭 Sección de Estrategia (si se completó)                    │
│     ├─ Diagrama de jerarquía Strategy Blocks                  │
│     ├─ Kernel de Buena Estrategia de Rumelt (Diagnóstico/     │
│     │  Política/Acciones)                                     │
│     └─ Tres Niveles de Trabajo de Producto de Shreyas         │
│  ✅ Sección de Evaluación de Oportunidad (si se completó)     │
│  🔍 Sección de Descubrimiento (si se completó)               │
│     ├─ Tabla de Personas (tabla estilo tarjeta)               │
│     ├─ Tarjetas de Persona (una por persona)                  │
│     ├─ Tabla de Análisis JTBD (cuatro tipos)                  │
│     ├─ Opportunity Solution Tree (árbol visual)               │
│     └─ User Journey Map (resumen + accordion de detalle)      │
│  🎯 Sección de Definición (si se completó)                    │
│     ├─ Tabla de Resumen de Puntos de Dolor                    │
│     ├─ Tarjeta de Framework de Posicionamiento April Dunford  │
│     ├─ Tarjetas de Preguntas HMW (con etiquetas de tipo JTBD)│
│     └─ Tabla de Evaluación de Oportunidades (vista costo de   │
│        oportunidad)                                           │
│  💡 Sección de Desarrollo (si se completó)                    │
│     ├─ Tarjeta PR-FAQ (formato simulado de comunicado de      │
│     │  prensa)                                                │
│     ├─ Ideación de Soluciones (tres columnas de tarjetas      │
│     │  paralelas)                                             │
│     ├─ Tabla de Riesgos Pre-mortem (código de color           │
│     │  Alto/Medio riesgo)                                     │
│     ├─ Matriz GEM + Cuadrante de Impacto/Esfuerzo            │
│     ├─ Tabla de Priorización RICE (si se completó)            │
│     ├─ Tabla de User Stories (si se completó)                 │
│     └─ Alcance MVP (tarjetas de tres columnas + Lista de      │
│        No Hacer)                                              │
│  🚀 Sección de Entrega (si se completó)                       │
│     ├─ Tarjeta de Definición del Aha Moment (prominente)      │
│     ├─ Tarjeta de North Star Metric                           │
│     ├─ Tabla de Métricas de Señales de Tres Capas             │
│     ├─ Evaluación de Nivel PMF (visual de cuatro niveles +    │
│     │  marcador de posición actual)                           │
│     ├─ Estrategia GTM (selección de canal + plan primeros     │
│     │  100 usuarios, si se completó)                          │
│     ├─ Modelo de Negocio y Precios (modelo de ingresos +      │
│     │  estrategia de precios, si se completó)                 │
│     ├─ Tabla del Plan de Validación de Hipótesis (si se       │
│     │  completó)                                              │
│     └─ Resumen de Spec de Producto (estructura de tres        │
│        secciones: Resumen de Decisiones / Límites de          │
│        Ejecución / Referencia Profunda)                       │
│  ⭐ Análisis del Mejor Punto de Entrada (visual de cadena     │
│     lógica completa)                                          │
├──────────────────────────────────────────────────────────────┤
│  Footer: Fecha de output + modo + atribución de frameworks    │
└──────────────────────────────────────────────────────────────┘
```

## Detalles de Diseño por Sección

**Estilo de Tablas:** Rayas zebra, encabezado oscuro, bordes redondeados, resaltado al hover

**Tarjetas de Persona:** Una tarjeta por Persona, puntos de dolor con borde izquierdo rojo, JTBD enfatizado con bloques de color azul/morado

**Opportunity Solution Tree:** Usar CSS o SVG ligero para dibujar la estructura de árbol, mostrando claramente la jerarquía Objetivo → Oportunidad → Solución

**Gráfico de Nivel PMF:** Usar barra de progreso o diagrama de pasos mostrando cuatro niveles, marcando la posición actual del usuario

**Tarjeta PR-FAQ:** Formato simulado de comunicado de prensa con titular, subtítulo, párrafo inicial — visualmente parecido a un documento real

**Tabla de Riesgos Pre-mortem:** Ítems de alto riesgo en alerta roja, riesgo medio en amarillo

**Cadena Lógica del Mejor Punto de Entrada:** Visualizar la cadena de razonamiento completa, cada nodo como una pequeña tarjeta, conectados por flechas

## Efectos Interactivos

- `scroll-behavior: smooth` — Scroll suave al hacer clic en TOC
- Intersection Observer — Resaltar sección actual en TOC mientras se hace scroll
- Micro-elevación de tarjeta al hover (`transform: translateY(-2px)` + `transition`)
- Expandir/colapsar accordion (etapas del User Journey Map, `<details>/<summary>`)
- `@media print` — Ocultar elementos interactivos al imprimir, asegurar que las tablas no se trunquen

## Notas Importantes

- Todo CSS y JS inline en HTML — sin dependencias externas excepto Google Fonts CDN para Inter
- Si una etapa no se completó, no renderizar una sección vacía — simplemente omitirla
- La sección Hero muestra el "Modo" y "Audiencia" para que los lectores entiendan inmediatamente el contexto del documento
- La página puede ser muy larga — la navegación TOC es crítica para saltar rápidamente

## Atribución de Frameworks y Lecturas Adicionales (en footer)

| Pensador | Contribución Clave | Fuente |
|----------|-------------------|--------|
| Teresa Torres | Descubrimiento Continuo, Opportunity Solution Tree | Lenny's Podcast + *Continuous Discovery Habits* |
| Shreyas Doshi | Framework LNO, Pre-mortem, Tres Niveles de Trabajo de Producto, Pensamiento de Costo de Oportunidad | Lenny's Podcast Ep.3 |
| Gibson Biddle | Modelo DHM, Priorización GEM | Lenny's Podcast |
| April Dunford | Framework de Posicionamiento | Lenny's Podcast + *Obviously Awesome* |
| Todd Jackson | Framework de Cuatro Niveles de PMF, Cuatro P's | Lenny's Podcast (First Round Capital) |
| Richard Rumelt | Buena Estrategia / Mala Estrategia, Kernel de Buena Estrategia | Lenny's Podcast + *Good Strategy Bad Strategy* |
| Marty Cagan | Empowered Teams, Descubrimiento de Producto | Lenny's Podcast + *Inspired*, *Empowered* |
| Chandra Janakiraman | Strategy Blocks | Lenny's Newsletter (Headspace / Meta) |
| Clayton Christensen | Jobs to Be Done | *Competing Against Luck* |
| Amazon | Working Backwards / PR-FAQ | *Working Backwards* |
| Sean Ellis | Sean Ellis Score, ICE Scoring | *Hacking Growth* |
| Lenny Rachitsky | Shape / Ship / Synchronize, Pensamiento North Star | Lenny's Newsletter + Podcast |
