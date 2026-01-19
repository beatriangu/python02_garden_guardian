python02_garden_guardian 🌿🛡️

Proyecto de práctica en Python orientado a consolidar fundamentos, reforzar buenas prácticas y trabajar con una estructura clara por ejercicios.
El objetivo es avanzar de forma progresiva: entender el enunciado, implementar soluciones limpias y verificar resultados mediante ejecución y pruebas.

🎯 Objetivos

Practicar Python de forma estructurada y progresiva.

Mejorar la calidad del código: claridad, orden y separación de responsabilidades.

Reforzar la modularidad, separando lógica y ejecución.

Ejecutar y comprobar resultados con comandos simples.

Documentar el aprendizaje sin afectar a la entrega final.

🗂️ Estructura del repositorio

Cada ejercicio vive en su propia carpeta (ex0/, ex1/, …) e incluye el archivo solicitado por el subject.

▶️ Cómo ejecutar

Desde la raíz del repositorio:

python3 ex0/ft_first_exception.py

✅ Resumen del módulo

EX0–EX1 → errores capturados → programa robusto

EX2 → errores con significado de dominio (excepciones personalizadas)

EX3 → finally garantiza un estado consistente

EX4 → raise corta el flujo lógico, pero el programa solo se detiene si no se captura la excepción

EX5 → integración completa y coherente del módulo

En Python, lanzar una excepción con raise indica que el flujo normal no debe continuar, pero solo la ausencia de captura detiene el programa. El control real del flujo se gestiona con try/except.

✅ Detalle de ejercicios
EX0 — Agricultural Data Validation Pipeline

Archivo: ex0/ft_first_exception.py

Qué se practica

Conversión de entrada de texto a número con int().

Manejo de errores con try/except para evitar bloqueos.

Validación de rango (temperatura válida entre 0°C y 40°C).

Escritura de un programa robusto que continúa tras errores controlados.

Casos de prueba incluidos

Entrada válida: "25"

No numérica: "abc"

Fuera de rango alto: "100"

Fuera de rango bajo: "-50"

Resultado esperado

Mensajes claros de éxito o error por cada caso.

El programa no crashea y finaliza correctamente.

El output respeta el formato del subject.

💡 Idea clave: capturar excepciones permite gestionar entradas inválidas sin detener el programa y mantener el flujo controlado.

EX1 — Different Types of Problems

Archivo: ex1/ft_different_errors.py

Qué se practica

Identificación y manejo de errores típicos:

ValueError

ZeroDivisionError

FileNotFoundError

KeyError

Captura de errores específicos con except dedicado.

Captura conjunta con una tupla de errores cuando el tratamiento es el mismo.

Qué demuestra

Que Python clasifica fallos según el tipo de problema.

Que se puede reaccionar de forma distinta según el error.

Que un programa robusto puede continuar tras fallos controlados.

Resultado esperado

Un bloque de prueba por tipo de error.

Mensaje claro por cada captura.

El programa finaliza correctamente respetando el output del subject.

💡 Idea clave: agrupar errores en una tupla permite simplificar el código cuando el comportamiento esperado es idéntico.

EX2 — Making Your Own Error Types

Archivo: ex2/ft_custom_errors.py

Qué se practica

Creación de excepciones personalizadas heredando de Exception.

Herencia para organizar errores por dominio (GardenError como base).

Lanzamiento de errores con raise.

Captura específica (errores concretos) y genérica (clase base).

Qué demuestra

Que los errores personalizados expresan mejor el contexto.

Que la herencia permite capturar familias de errores con flexibilidad.

Resultado esperado

Se lanzan y capturan correctamente PlantError y WaterError.

Capturar GardenError captura también los errores derivados.

Mensajes claros y output alineado con el subject.

💡 Idea clave: las excepciones personalizadas mejoran la lectura y hacen el sistema más mantenible y defendible.

EX3 — Finally Block: Always Clean Up

Archivo: ex3/ft_finally_block.py

Qué se practica

Uso de finally para garantizar acciones de cierre/limpieza.

Simulación de apertura/cierre de un sistema (riego).

Manejo de errores durante el proceso.

Control del flujo mediante valores de retorno (True/False).

Qué demuestra

Que finally se ejecuta siempre, haya error o no.

Que la limpieza de recursos no debe depender del éxito del proceso.

Separación entre lógica y presentación.

Resultado esperado

El sistema de riego se abre antes del proceso.

Se riegan plantas válidas.

Ante una planta inválida, se muestra un error claro.

El cierre se imprime siempre.

Output exacto al ejemplo del subject.

💡 Idea clave: finally asegura consistencia y evita estados incoherentes.

EX4 — Raising Errors to Stop Invalid Flow

Archivo: ex4/ft_raise_errors.py

Qué se practica

Validación explícita de datos de entrada.

Uso de raise para marcar condiciones inválidas.

Detención del flujo normal ante datos incorrectos.

Separación clara entre validación (lógica) y print (presentación).

Qué demuestra

Que raise señala errores que no deben permitir continuar.

Que los errores se generan donde corresponde: en la validación.

Que el flujo se controla desde el test con try/except.

Que el output puede respetarse exactamente.

Casos de prueba incluidos

Valores correctos → planta saludable.

Nombre vacío → error inmediato.

Agua fuera de rango → error claro.

Sol fuera de rango → error específico.

Resultado esperado

Valores válidos → éxito.

Valores inválidos → ValueError lanzado y capturado.

El programa no avanza con datos incorrectos.

Output idéntico al subject.

💡 Idea clave: lanzar excepciones fuerza el tratamiento explícito de errores y refuerza robustez y separación de responsabilidades.

EX5 — Garden Management System

Ejercicio de integración del módulo Garden Guardian

Este ejercicio combina y reutiliza todos los conceptos trabajados en EX0–EX4, aplicándolos a un sistema único y coherente.

Qué integra

Validación de datos → EX0 y EX4

Uso de raise → EX4

Excepciones personalizadas → EX2

Manejo con try/except → EX1

finally para consistencia → EX3

Separación de responsabilidades → hilo conductor del módulo

Uso de clases y estado (GardenManager) → evolución natural del diseño

Control estricto del output → aprendido desde EX0

Idea clave: EX5 transforma ejercicios aislados en un sistema completo, robusto y defendible.

💡 Idea clave: integración real = diseño consistente + manejo de errores sin crashear + estado siempre controlado.

📝 Notas personales

El repositorio puede incluir archivos como FAQ.txt con explicaciones conceptuales y reflexiones personales.
Estos archivos no forman parte de la entrega y se usan únicamente como apoyo para el aprendizaje y la preparación de la defensa.