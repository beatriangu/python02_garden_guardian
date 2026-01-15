# python02_garden_guardian 🌿🛡️

Proyecto de práctica en Python orientado a consolidar fundamentos, reforzar buenas prácticas y trabajar con una estructura clara por ejercicios.  
El objetivo es avanzar de forma progresiva: entender el enunciado, implementar soluciones limpias y comprobar resultados mediante ejecución y pruebas.

---

## 🎯 Objetivos

- Practicar Python de forma estructurada y progresiva.
- Mejorar la calidad del código: claridad, orden y responsabilidades.
- Trabajar la modularidad separando lógica y ejecución.
- Ejecutar y verificar resultados con comandos simples.
- Documentar el aprendizaje sin afectar a la entrega final.

---

## 🗂️ Estructura del repositorio

Cada ejercicio está en su propia carpeta (`ex0/`, `ex1/`, …) y contiene el archivo solicitado por el subject.

---

## ▶️ Cómo ejecutar

Desde la raíz del repositorio:

```bash
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
El uso de excepciones permite detectar y gestionar entradas inválidas sin que el programa se detenga. Al capturar los errores con try/except, el programa puede informar del problema y continuar su ejecución de forma controlada, garantizando un comportamiento robusto.

EX1 — Different Types of Problems

Archivo: ex1/ft_different_errors.py

Qué se practica

Identificación de distintos tipos de errores en Python:

ValueError

ZeroDivisionError

FileNotFoundError

KeyError

Uso de bloques try/except para capturar errores específicos.

Demostración de que el programa continúa ejecutándose tras cada error.

Captura de múltiples tipos de error con una sola cláusula except.

Qué demuestra el ejercicio

Que Python clasifica los errores según el tipo de problema ocurrido.

Que es posible reaccionar de forma distinta según el error detectado.

Que varios errores pueden manejarse conjuntamente cuando el tratamiento es el mismo.

Que un programa robusto puede gestionar fallos sin detener su ejecución.

Resultado esperado

Se muestra un bloque de prueba por cada tipo de error.

Cada error se captura y se explica con un mensaje claro.

El programa continúa tras cada fallo y finaliza correctamente.

El formato del output respeta el ejemplo proporcionado en el subject.

💡 
Python tiene distintos tipos de errores porque cada uno representa un problema diferente durante la ejecución, lo que permite identificarlos y gestionarlos de forma adecuada. Es posible capturar varios tipos de error con un solo bloque except agrupándolos en una tupla, cuando todos requieren el mismo tratamiento.

### EX2 — Making Your Own Error Types  
**Archivo:** `ex2/ft_custom_errors.py`

**Qué se practica**
- Creación de excepciones personalizadas mediante clases que heredan de `Exception`.
- Uso de la herencia para organizar errores por dominio (`GardenError` como base).
- Lanzamiento de errores personalizados con `raise`.
- Captura de errores específicos y captura genérica a través de la clase base.

**Qué demuestra el ejercicio**
- Que los errores personalizados permiten expresar mejor el contexto del problema.
- Que la herencia facilita agrupar errores relacionados en una misma familia.
- Que es posible manejar errores de forma específica o general según la necesidad.
- Que el programa sigue ejecutándose tras capturar los errores.

**Resultado esperado**
- Se lanzan y capturan correctamente errores de tipo `PlantError` y `WaterError`.
- Al capturar `GardenError`, se capturan también sus errores derivados.
- El programa finaliza correctamente mostrando mensajes claros.
- El comportamiento y el output siguen el ejemplo proporcionado en el subject.

💡 
Las excepciones personalizadas se crean cuando los errores genéricos de Python no expresan bien el contexto del problema y queremos mensajes más claros y manejables dentro de un dominio (por ejemplo, errores del huerto). La herencia ayuda a organizarlas en “familias”: permite capturar errores específicos (PlantError, WaterError) o capturar todos los relacionados con el huerto con una sola excepción base (GardenError).


📝 Notas personales

El repositorio puede incluir archivos como FAQ.txt con explicaciones
conceptuales y reflexiones personales.
Estos archivos no forman parte de la entrega y se utilizan únicamente
como apoyo para el aprendizaje y la preparación de la defensa.