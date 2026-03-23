# Handoff de Desarrollo — Paquete de Handoff Principal

> Se activa cuando el usuario dice "iniciar desarrollo," "produce un paquete de handoff de desarrollo," "configura mi proyecto," o "conectar con Claude Code."
> Lee este archivo, consolida los outputs de todo el proceso de planificación de producto, y genera un paquete de handoff de desarrollo que puede usarse directamente en el CLI de Claude Code.

## Restricciones del Entorno y Estrategia de Handoff

**Hecho clave: Claude Chat / Cowork y Claude Code son entornos de ejecución separados — no puedes lanzar Claude Code desde dentro de Chat.**

La estrategia de handoff es por lo tanto: **Producir un paquete de handoff de desarrollo estructurado (un conjunto de archivos)** que el usuario descarga, coloca en su carpeta de proyecto, y puede iniciar todo el flujo de desarrollo con un solo prompt en Claude Code.

El método de handoff depende del entorno del usuario:

| Entorno del Usuario | Método de Handoff |
|--------------------|------------------|
| **Claude Chat (Web/App)** | Producir un archivo zip para descargar; el usuario extrae al directorio del proyecto luego abre Claude Code |
| **Claude Cowork (Desktop)** | Igual que arriba, pero puede escribir archivos directamente a una ruta local especificada por el usuario |
| **Ya en Claude Code** | Crear todos los archivos directamente en el directorio del proyecto (en este escenario, este skill probablemente se referencia desde CLAUDE.md) |

---

## Contenido del Paquete de Handoff de Desarrollo

Produce el siguiente conjunto de archivos, todos colocados en la raíz del proyecto:

```
[nombre-del-proyecto]/
├── .gitignore             # Exclusiones de control de versiones (.env, secretos, archivos de progreso, etc. — plantilla en references/07c-architecture-setup.md)
├── CLAUDE.md              # Memoria de proyecto de Claude Code: contexto de producto + guías de desarrollo
├── TASKS.md               # Desglose de funcionalidades + hitos por Fase + criterios de aceptación por Tarea
├── TICKETS.md             # Contenido de tickets: título, descripción, criterios de aceptación por ticket — PM puede crear tickets directamente
├── docs/
│   ├── PRD.md             # PRD completo (consolidado del formato de output de 04-develop.md)
│   ├── ARCHITECTURE.md    # Arquitectura técnica: estructura de directorios + esquema BD + endpoints API + arquitectura de seguridad
│   └── PRODUCT-SPEC.md    # Resumen de Spec de Producto (consolidado de 05-deliver.md → 4.6)
└── scripts/
    └── setup.sh           # Script de inicialización en un solo comando (crear directorios + instalar dependencias)
```

---

## 📄 Plantilla CLAUDE.md

CLAUDE.md es el archivo de memoria de proyecto de Claude Code — Claude Code lo lee automáticamente en cada inicio. Debe incluir:

```markdown
# [Nombre del Producto] — Guía del Proyecto

## Contexto del Producto

**Descripción en una línea**: [Titular del PR-FAQ]
**Usuarios Objetivo**: [Persona en una oración]
**JTBD Central**: [Cliente Objetivo] quiere [Job] en el contexto de [Contexto del Job]
**Aha Moment**: Cuando el usuario completa [acción], experimenta el valor central
**North Star Metric**: [Nombre de la métrica + definición]

## Stack Tecnológico

- **Frontend**: [Framework + versión]
- **Backend**: [Framework + versión]
- **Base de Datos**: [Tipo + versión]
- **Despliegue**: [Plataforma]
- **Gestor de Paquetes**: [Herramienta]

## Guías de Desarrollo

- Desarrollar en [lenguaje]
- Seguir [guía de estilo / reglas de lint]
- Formato de commit message: `[type]: [description]` (type: feat / fix / refactor / docs / test)
- Estrategia de ramas: [main / develop / feature-xxx]
- Cada funcionalidad debe referenciar su número de User Story (ver TASKS.md)

## Límites del MVP

**Imprescindibles (P0)**:
- [Funcionalidad 1]
- [Funcionalidad 2]
- [Funcionalidad 3]

**Explícitamente No Hacer**:
- [Exclusión 1] — Razón: [justificación]
- [Exclusión 2] — Razón: [justificación]

## Registro de Decisiones Clave

| Decisión | Elección | Justificación | Fecha |
|----------|---------|---------------|-------|
| [p.ej., Selección de base de datos] | [PostgreSQL] | [Necesita consultas relacionales + soporte JSON] | [Fecha] |

## Alertas de Riesgo (del Pre-mortem)

- ⚠️ [Riesgo 1]: [Medida preventiva]
- ⚠️ [Riesgo 2]: [Medida preventiva]

## Notas de Seguridad

> Lista completa de seguridad en `references/08-security-checklist.md`. Abajo están las decisiones clave de seguridad de este producto:

- Autenticación: [JWT / Session / OAuth]
- Política CORS: [Orígenes permitidos]
- Rate Limiting: [Resumen de estrategia]
- Datos sensibles: [Enfoque de manejo]

## Flujo de Trabajo de Desarrollo

Sigue el orden de Fases en `TASKS.md`. Después de completar cada Fase:
1. Verifica que todos los criterios de aceptación de las Tareas pasen
2. Pregunta al usuario si desea proceder a la siguiente Fase
3. Si surgen preguntas de arquitectura, consulta `docs/ARCHITECTURE.md`
```

---

## Flujo de Confirmación de Stack Tecnológico

Antes de producir el paquete de handoff, el stack tecnológico debe confirmarse. Si el usuario no lo ha especificado, pregunta en este orden:

### Obligatorio (Afecta todos los outputs)

```
1. ¿Qué tipo de aplicación es esta?
   □ App Web (navegador)
   □ App Móvil (iOS / Android / multiplataforma)
   □ App de Escritorio
   □ API / Servicio Backend
   □ Herramienta CLI
   □ Otro

2. ¿Tienes un stack tecnológico preferido?
   (Si no, recomendaré uno basado en las características del producto)
```

### Lógica de Recomendación (Cuando el usuario no ha especificado)

| Tipo de Aplicación | Stack Recomendado | Justificación |
|-------------------|-------------------|---------------|
| App Web (validación rápida de MVP) | Next.js + Tailwind + Supabase | Full-stack en uno, despliegue fácil, Auth integrado |
| App Web (lógica backend compleja) | React + Node.js/Express + PostgreSQL | Alta flexibilidad, ecosistema maduro |
| App Web (equipo Python) | React + FastAPI/Django + PostgreSQL | Ecosistema Python, Django tiene Admin integrado |
| App Móvil (multiplataforma) | React Native / Flutter | Un solo codebase cubre ambas plataformas |
| Servicio API | FastAPI / Express / Go | Ligero, alto rendimiento |

> Claude debe explicar la justificación al recomendar y recordar al usuario que puede cambiar la recomendación.

### Opcional (Seguimiento basado en necesidades del producto)

```
3. ¿Necesitas autenticación de usuarios? (Afecta selección de enfoque Auth)
4. ¿Algún requisito en tiempo real? (WebSocket / SSE)
5. ¿Necesitas subir/procesar archivos? (Afecta elección de almacenamiento)
6. ¿Dónde planeas desplegar? (Vercel / Railway / AWS / self-hosted)
```
