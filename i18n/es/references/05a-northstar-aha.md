# Fase 4: Entrega — North Star + Aha Moment

## 4.1 Principios de Empowered Teams de Marty Cagan

**Aplicable cuando: alta completitud / audiencia del entregable es liderazgo o equipos cross-funcionales**

> 4.1 Empowered Teams solo se muestra cuando la audiencia del entregable es liderazgo o equipos cross-funcionales; de lo contrario se omite.

```
| Dimensión | Feature Team (Evitar) | Empowered Team (Meta) |
|-----------|----------------------|----------------------|
| Asignado | Lista de funcionalidades (Output) | Problema a resolver (Outcome) |
| Éxito definido como | Entregar funcionalidades a tiempo | Lograr métricas de usuario y negocio |
| Rol del PM | Recopilador de requisitos y project manager | Explorador de problemas y validador de soluciones |
| Rol de Ingenieros | Ejecutar especificaciones | Participar en exploración de problemas y diseño de soluciones |
```

> "El verdadero descubrimiento de producto se hace **junto con** ingenieros y diseñadores, no por el PM solo entregando trabajo terminado." — Marty Cagan

**Tres Responsabilidades del PM de Lenny:**
- **Shape**: Sintetizar insights de usuarios, datos e inteligencia de mercado para decidir qué construir
- **Ship**: Asegurar que un producto de alta calidad se lance a tiempo, sin sorpresas
- **Synchronize**: Mantener a todos los stakeholders alineados en visión, estrategia, metas y roadmap

## 4.2 Framework de Métricas de Éxito (North Star + Señales de Tres Capas)

Una North Star metric debe satisfacer:
- Refleja el valor real que los usuarios reciben (no una métrica vanidosa)
- Puede crecer continuamente (no tiene un techo natural)
- Alinea a todo el equipo alrededor de un solo objetivo

```
| Empresa | North Star Metric | Por Qué Esta Métrica |
|---------|-------------------|----------------------|
| Airbnb | Noches reservadas | Representa valor entregado tanto a anfitriones como a huéspedes |
| Spotify | Horas de escucha mensual | Representa usuarios genuinamente usando y disfrutando la música |
| Facebook | Ratio DAU / MAU | Representa visitas de retorno habituales |
| Slack | Mensajes enviados por semana | Representa equipos genuinamente colaborando |
| Salesforce | ACV de clientes activos (Valor de Contrato Anual) | Representa clientes derivando valor de negocio continuamente (B2B) |
```

**Tu North Star Metric:**
```
North Star Metric: [Un solo número que representa el valor central creado para los usuarios y el producto]
Definición: [Método de cálculo preciso]
Por qué esta métrica: [Explica por qué representa valor real para el usuario, no solo un resultado de negocio]
```

### 📝 Lista de Verificación de Calidad de North Star
- ✅ ¿Refleja el valor que los usuarios reciben? (No ingresos, no DAU)
- ✅ ¿Puede crecer continuamente? (No tiene un techo natural)
- ✅ ¿Todos en el equipo saben qué hacer cuando ven esta métrica?
- ✅ ¿Puede ser manipulada? (Si sí, se necesitan métricas de protección)
- ✅ Productos B2B: ¿Refleja valor a nivel organizacional, no solo de usuarios individuales?
- ❌ Problemas comunes: usar ingresos como North Star (los ingresos son un resultado, no un impulsor), métrica demasiado compuesta para actuar sobre ella

**Sistema de Señales de Tres Capas (debe lograrse en orden):**

```
| Capa | Tipo de Métrica | Definición | Objetivo B2C | Objetivo B2B |
|---|---|---|---|---|
| Capa 1 (Prerequisito) | Tasa de Éxito de Acción Central | ¿El usuario completó la acción central del producto? | 30–40%+ | 60–80%+ (usuarios más motivados) |
| Capa 2 (Proxy de Valor) | Tasa de Retención D14 / D28 | ¿Los usuarios siguen regresando? | Productos de consumo 15–20%+ | Retención de logos 90%+; Net Revenue Retention 100%+ |
| Capa 3 (Señal de Pasión) | Sean Ellis Score | "Si ya no pudieras usar este producto, ¿qué tan decepcionado estarías?" | 40%+ responde "muy decepcionado" | 40%+ responde "muy decepcionado" |
| Métricas de Protección | Prevenir sobre-optimización | Asegurar que otras dimensiones importantes no se perjudiquen | Depende del contexto | Depende del contexto |
```

Nota: La Capa 1 es prerequisito de la Capa 2. Si la tasa de éxito de la acción central es muy baja, los datos de retención son irrelevantes porque los usuarios nunca tuvieron la oportunidad de experimentar el valor del producto.

## 4.4 Diseño del Aha Moment

```
Definición del Aha Moment:
Cuando un usuario completa [comportamiento específico], ha experimentado el valor central de este producto.
Meta: Llevar a los usuarios a este momento dentro de [X minutos / X pasos] de entrar al producto.

Tasa de Alcance del Aha Moment: [% objetivo]
Barreras Actuales: [¿Qué impide que los usuarios alcancen el Aha Moment más rápido?]
Plan de Mejora: [¿Cómo eliminar las barreras?]
```

**Ejemplos:**
| Producto | Aha Moment | Objetivo de Tiempo |
|---------|-----------|-------------------|
| Slack | El equipo envía su mensaje número 2,000 | Primeras dos semanas |
| Dropbox | Primer archivo sincronizado a un segundo dispositivo | Dentro de 10 minutos del primer uso |
| Zoom | Primera conexión con un clic con video fluido | Primer uso |

### 📝 Lista de Verificación de Calidad del Aha Moment
- ✅ ¿Es un comportamiento específico y rastreable? (No "siente que el producto es útil")
- ✅ ¿Está directamente vinculado al job funcional del JTBD?
- ✅ ¿El objetivo de tiempo es razonable? (B2C debería ser dentro del primer uso; B2B puede ser dentro del período de prueba)
- ✅ ¿Se puede diseñar el onboarding para ayudar a los usuarios a alcanzarlo más rápido?
