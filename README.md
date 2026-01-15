python02_garden_guardian 🌿🛡️

Proyecto de práctica en Python orientado a consolidar fundamentos, reforzar buenas prácticas y trabajar con una estructura clara por ejercicios.
El objetivo es avanzar de forma progresiva: entender el enunciado, implementar soluciones limpias y comprobar resultados mediante ejecución y pruebas.

🎯 Objetivos

Practicar Python de forma estructurada y progresiva.

Mejorar la calidad del código: claridad, orden y responsabilidades.

Trabajar la modularidad separando lógica y ejecución.

Ejecutar y verificar resultados con comandos simples.

Documentar el aprendizaje sin afectar a la entrega final.

🗂️ Estructura del repositorio

Cada ejercicio está en su propia carpeta (ex0/, ex1/, …) y contiene el archivo solicitado por el subject.

▶️ Cómo ejecutar

Desde la raíz del repositorio:

python3 ex0/ft_first_exception.py

✅ Ejercicios
EX0 — Agricultural Data Validation Pipeline

Archivo: ex0/ft_first_exception.py

Qué se practica

Conversión de entrada de texto a número usando int().

Manejo de errores con try/except para evitar que el programa se detenga.

Validación de rango (temperatura válida entre 0°C y 40°C).

Demostración de un programa robusto que continúa su ejecución.

Casos de prueba incluidos

Entrada válida: "25"

No numérica: "abc"

Fuera de rango alto: "100"

Fuera de rango bajo: "-50"

Resultado esperado

Mensajes claros de éxito o error por cada prueba.

El programa no crashea y finaliza correctamente.

El formato del output respeta el ejemplo del subject.

💡
El uso de excepciones permite detectar y gestionar entradas inválidas sin que el programa se detenga. Al capturar los errores con try/except, el programa informa del problema y continúa su ejecución de forma controlada.

EX1 — Different Types of Problems

Archivo: ex1/ft_different_errors.py

Qué se practica

Identificación de distintos tipos de errores en Python:

ValueError

ZeroDivisionError

FileNotFoundError

KeyError

Uso de bloques try/except para capturar errores específicos.

Captura de múltiples tipos de error con una sola cláusula except.

Qué demuestra el ejercicio

Que Python clasifica los errores según el tipo de problema ocurrido.

Que es posible reaccionar de forma distinta según el error detectado.

Que un programa robusto puede gestionar fallos sin detener su ejecución.

Resultado esperado

Un bloque de prueba por cada tipo de error.

Cada error se captura y se explica con un mensaje claro.

El programa continúa tras cada fallo y finaliza correctamente.

El output respeta el ejemplo del subject.

💡
Python define distintos tipos de errores porque cada uno representa un problema diferente durante la ejecución. Agrupar errores en una tupla permite tratarlos de forma conjunta cuando el comportamiento deseado es el mismo.

EX2 — Making Your Own Error Types

Archivo: ex2/ft_custom_errors.py

Qué se practica

Creación de excepciones personalizadas heredando de Exception.

Uso de herencia para organizar errores por dominio (GardenError como base).

Lanzamiento de errores personalizados con raise.

Captura de errores específicos y captura genérica a través de la clase base.

Qué demuestra el ejercicio

Que los errores personalizados expresan mejor el contexto del problema.

Que la herencia permite agrupar errores relacionados.

Que el programa sigue ejecutándose tras capturar los errores.

Resultado esperado

Se lanzan y capturan correctamente PlantError y WaterError.

Al capturar GardenError, se capturan también sus errores derivados.

El programa finaliza correctamente con mensajes claros.

El output sigue el ejemplo del subject.

💡
Las excepciones personalizadas se utilizan cuando los errores genéricos no describen bien el problema. La herencia permite capturar errores específicos o todos los relacionados con el dominio del huerto de forma flexible.

EX3 — Finally Block: Always Clean Up

Archivo: ex3/ft_finally_block.py

Qué se practica

Uso del bloque finally para garantizar acciones de limpieza.

Simulación de apertura y cierre de un sistema (riego).

Manejo de errores durante la ejecución.

Control del flujo mediante valores de retorno (True / False).

Qué demuestra el ejercicio

Que finally se ejecuta siempre, haya error o no.

Que la limpieza de recursos no debe depender del resultado del proceso.

Que se puede separar la lógica del sistema de la presentación de resultados.

Resultado esperado

El sistema de riego se abre antes del proceso.

Cada planta válida se riega correctamente.

Ante una planta inválida, se muestra un error claro.

El mensaje de cierre del sistema se imprime siempre.

El output respeta exactamente el ejemplo del subject.

💡
El bloque finally garantiza que las tareas de cierre o limpieza se ejecuten siempre, evitando estados inconsistentes y asegurando un comportamiento predecible.

EX4 — Raising Errors to Stop Invalid Flow

Archivo: ex4/ft_raise_errors.py

Qué se practica

Validación explícita de datos de entrada.

Uso de raise para lanzar errores cuando las reglas no se cumplen.

Detención del flujo normal ante datos inválidos.

Separación clara entre validación (lógica) y presentación (prints).

Qué demuestra el ejercicio

Que raise se usa para señalar errores que no deben permitir continuar.

Que los errores se producen en el lugar correcto (validación).

Que el control del flujo se gestiona desde la función de test.

Que el output puede respetarse exactamente.

Casos de prueba incluidos

Valores correctos → planta saludable.

Nombre vacío → error inmediato.

Nivel de agua fuera de rango → error claro.

Horas de sol fuera de rango → error específico.

Resultado esperado

Para valores válidos, mensaje de éxito.

Para valores inválidos, ValueError lanzado y capturado.

El programa no continúa con datos incorrectos.

El output coincide con el ejemplo del subject.

💡
Lanzar excepciones obliga a gestionar explícitamente los errores y evita que el sistema continúe en un estado inválido. Esto refuerza la robustez y la separación de responsabilidades.

EX5 — Garden Management System

Ejercicio de integración del módulo Garden Guardian

Este ejercicio combina y reutiliza todos los conceptos trabajados en EX0–EX4, aplicándolos en un sistema único y coherente.

Qué integra

Validación de datos → EX0 y EX4

Uso de raise → EX4

Excepciones personalizadas → EX2

Manejo de errores con try/except → EX1

Uso de finally → EX3

Separación de responsabilidades → hilo conductor del módulo

Uso de clases y estado (GardenManager) → evolución natural del diseño

Control estricto del output → aprendido desde EX0

Idea clave
EX5 transforma ejercicios aislados en un sistema completo, robusto y defendible.

💡
EX5 es un ejercicio de integración que reutiliza todos los conceptos del módulo (validación, raise, excepciones personalizadas, try/except y finally) para construir un sistema coherente que gestiona errores sin crashear y garantiza siempre un estado consistente.

📝 Notas personales

El repositorio puede incluir archivos como FAQ.txt con explicaciones conceptuales y reflexiones personales.
Estos archivos no forman parte de la entrega y se utilizan únicamente como apoyo para el aprendizaje y la preparación de la defensa.