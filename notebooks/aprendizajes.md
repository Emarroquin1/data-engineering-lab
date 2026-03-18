# Aprendizajes Clave

En esta sesión, cubrimos varios conceptos importantes de Python y la estructuración de proyectos de datos.

## 1. Ejecución de Scripts en Python con `if __name__ == "__main__"`

Aprendimos que el bloque `if __name__ == "__main__":` es una construcción fundamental en Python para controlar la ejecución del código.

- **`__name__`**: Es una variable especial que Python asigna a cada script.
- **Ejecución directa**: Si ejecutas un script directamente (ej. `python mi_script.py`), Python asigna el valor `__main__` a la variable `__name__`.
- **Importación como módulo**: Si importas el script desde otro archivo (ej. `import mi_script`), Python asigna el nombre del archivo (en este caso, `mi_script`) a la variable `__name__`.

**¿Por qué es útil?**
Permite crear código que puede ser ejecutado de forma independiente y, al mismo tiempo, ser importado y reutilizado en otros programas sin que se ejecute automáticamente.

## 2. Indentación para Definir Bloques de Código

A diferencia de otros lenguajes que usan llaves `{}` o palabras clave como `end`, Python utiliza la **indentación** (el espacio en blanco al inicio de una línea) para definir el alcance de los bloques de código.

- Un bloque de código (como una función, un `if`, o un bucle `for`) comienza después de dos puntos (`:`) y debe estar indentado.
- El bloque termina cuando la indentación vuelve al nivel anterior.

Esto obliga a escribir un código más limpio y legible.

## 3. Creación y Ejecución de un Pipeline de Datos

Creamos un script (`run_pipeline.py`) que orquesta la ejecución de varios scripts de Python en una secuencia específica. Este es un enfoque común para automatizar flujos de trabajo de datos.

Nuestro pipeline sigue los pasos:
1.  **Extract**: Extrae datos de una fuente (en nuestro caso, una API).
2.  **Transform**: Limpia, procesa y enriquece los datos crudos.
3.  **Load**: Carga los datos transformados a un destino (una base de datos SQLite).
