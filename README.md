# Taller Unidad I - Electiva IV (Python)

## 1. Descripcion del proyecto

Este proyecto contiene la solucion completa del Taller de la Unidad I de la asignatura Electiva IV - Gestion de Datos con Python.

El archivo principal implementa:

- Carga y procesamiento de datos desde un archivo JSON de estudiantes.
- Calculo de promedios por asignatura y por estudiante.
- Generacion de correos institucionales con reglas definidas.
- Desarrollo de los ejercicios 5.1 a 5.15 de cuadernillos (operadores, funciones, cadenas, listas, conjuntos y diccionarios).

## 2. Archivo principal

- Electiva_IV_Lotero_Niño_Muñoz.py

## 3. Requisitos

- Python 3.9 o superior.
- Sistema operativo con terminal (Windows, Linux o macOS).
- Para actividades 1 a 4: archivo data/Unidad1_Reto.json.

## 4. Estructura esperada de carpeta

Se recomienda la siguiente organizacion:

- Electiva_IV_Lotero_Niño_Muñoz.py
- data/
- data/Unidad1_Reto.json (requerido para actividades 1 a 4)
- README.md

## 5. Paso a paso para ejecutar

### Paso 1. Abrir terminal en la carpeta del proyecto

En Windows PowerShell:

```powershell
cd "C:\ruta\de\tu\proyecto\Electiva_IV"
```

En Linux o macOS:

```bash
cd "/ruta/de/tu/proyecto/Electiva_IV"
```

### Paso 2. Verificar version de Python

```powershell
python --version
```

Si el comando no funciona, usar:

```powershell
py --version
```

### Paso 3. Ejecutar el script

```powershell
python "Electiva_IV_Lotero_Niño_Muñoz.py"
```

Si se requiere usar el lanzador de Python en Windows:

```powershell
py "Electiva_IV_Lotero_Niño_Muñoz.py"
```

### Paso 4. Revisar salida en consola

El programa imprime:

- Encabezados por actividad y subactividad.
- Resultados de las actividades 5.1 a 5.15.
- Resultados de actividades 1 a 4 solo si existe el archivo data/Unidad1_Reto.json.

## 6. Comportamiento cuando no existe el JSON

Si el archivo data/Unidad1_Reto.json no existe, el programa muestra un mensaje indicando que se omiten las actividades 1 a 4 y continua con las actividades del cuadernillo (5.x).

## 7. Alcance funcional implementado

### Actividades principales

- Actividad 1: carga de archivo JSON.
- Actividad 2: promedio por asignatura.
- Actividad 3: promedio por estudiante en asignaturas no retiradas y ordenado por apellido.
- Actividad 4: generacion de correo institucional.

### Cuadernillos (Actividad 5)

- 5.1: validacion de vocal/consonante.
- 5.2: ecuacion cuadratica como funcion.
- 5.3: impresion de histograma.
- 5.4: ejemplos de metodos de cadena.
- 5.5: division y transformacion de frase.
- 5.6: fecha actual y extraccion de mes.
- 5.7: impresion formateada de empleados.
- 5.8: ejemplos de operaciones en listas.
- 5.9: deteccion de duplicados sin modificar lista.
- 5.10: eliminacion de duplicados.
- 5.11: diferencia entre set y frozenset.
- 5.12: ejemplos de operadores de conjuntos.
- 5.13: agrupacion de palabras por inicial.
- 5.14: conteo de vocales y consonantes.
- 5.15: conversion de cadena de clientes a diccionario anidado.

## 8. Nota de versionado

Existe un archivo .gitignore que ignora archivos con extension .md y .pdf. Esto significa que README.md puede existir localmente pero no sera agregado al repositorio si se inicializa Git con esa configuracion.
