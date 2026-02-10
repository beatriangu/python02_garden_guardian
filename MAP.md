🧭 MAP.md — Python Garden · Data Guard
Garden Guardian · Error Handling & Resilient Systems

Este documento es MI mapa de aprendizaje y diseño.
Explica cómo evoluciona mi forma de pensar los errores a lo largo del
módulo python02_data_guard.

No describe solo qué hace el código, sino por qué se diseña así.

🌱 Idea central del módulo

Pasar de:

❌ “mi programa se rompe si algo falla”
a
✅ “mi programa espera fallos y los gestiona”

Un sistema profesional:

detecta errores

los clasifica

los comunica

limpia recursos

continúa funcionando

El objetivo no es evitar errores, sino hacerlos manejables.

🟢 ex0 — Agricultural Data Validation Pipeline

Foco
→ Primer contacto real con errores.

Aprendo

try / except

ValueError implícito

Validación de datos externos (sensores / input)

Clave mental
👉 Los datos que vienen de fuera no son fiables.

Prepara para

No confiar ciegamente en input()

Empezar a pensar en fallos como algo normal

🟢 ex1 — Different Types of Problems

Foco
→ No todos los errores son iguales.

Aprendo

ValueError

ZeroDivisionError

FileNotFoundError

KeyError

Captura múltiple de excepciones

Clave mental
👉 Python clasifica los errores por su naturaleza.
👉 Capturar bien = entender el problema.

Depende de

try / except básico (ex0)

Prepara para

Diseñar errores con significado propio

🟢 ex2 — Making Your Own Error Types

Foco
→ Errores con significado de dominio.

Aprendo

Crear clases de excepción

Herencia entre errores

Captura por jerarquía

Clave mental
👉 No todo error es técnico.
👉 Algunos errores pertenecen al dominio del problema.

GardenError
 ├── PlantError
 └── WaterError


Depende de

Comprender tipos de error (ex1)

Prepara para

Sistemas grandes y organizados

🟢 ex3 — Finally Block: Always Clean Up

Foco
→ Pase lo que pase, se limpia.

Aprendo

finally

Limpieza garantizada

Gestión consciente de recursos

Clave mental
👉 El error puede ocurrir.
👉 La limpieza no puede fallar.

try
 ├── operación
except
 ├── gestión del error
finally
 └── limpieza SIEMPRE


Depende de

try / except sólido (ex0–ex2)

Prepara para

Programas que no dejan el sistema roto

🟢 ex4 — Raising Your Own Errors

Foco
→ Detectar estados inválidos a propósito.

Aprendo

raise

Separar:

detección del error

gestión del error

Mensajes claros y útiles

Clave mental
👉 No todo error viene de Python.
👉 A veces tu programa decide que algo está mal.

Depende de

Errores personalizados (ex2)

Prepara para

Sistemas con reglas claras y explícitas

🟢 ex5 — Garden Management System

Foco
→ Sistema completo y resiliente.

Integra

try / except

excepciones personalizadas

raise

finally

recuperación del sistema

Clave final
👉 El sistema:

falla

informa

se recupera

continúa

Arquitectura mental

GardenManager
 ├── add_plant()
 ├── water_plants()
 │    └── try / except / finally
 ├── check_plant_health()
 │    └── raise ValueError
 └── manejo global de GardenError

🧠 Visión global del módulo
ex0 → detectar errores
ex1 → clasificarlos
ex2 → nombrarlos
ex3 → limpiar siempre
ex4 → provocarlos bien
ex5 → integrarlo todo


No son ejercicios sueltos.
Es un entrenamiento de resiliencia.

🎯 Objetivo final

Ser capaz de explicar:

qué puede fallar

cómo se detecta

cómo se comunica

cómo se limpia

cómo el sistema sigue vivo

Este MAP refleja mi arquitectura mental del módulo
y mi forma de diseñar sistemas defensivos en Python.
