# README — Instrucciones de ejecución del cuadernillo

Este documento explica cómo preparar el entorno y ejecutar el cuadernillo `Electiva_IV_Lotero_Nino_Munoz.ipynb` y el respaldo ejecutable `.py`.

## Requisitos
- Python 3.8 o superior
- pip
- Acceso a PowerShell (Windows)
- Estar en la raíz del proyecto (la carpeta que contiene `Electiva_IV_Lotero_Nino_Munoz.ipynb` y la carpeta `data`)

## Preparar entorno (recomendado)
En PowerShell, desde la raíz del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install jupyter
```

Si usas VS Code puedes crear/activar el entorno desde la paleta y seleccionar el intérprete.

## Ejecutar el cuadernillo en Jupyter
1. Lanzar Jupyter Lab o Notebook:

```powershell
jupyter lab
# o
jupyter notebook
```

2. Abrir `Electiva_IV_Lotero_Nino_Munoz.ipynb` desde la interfaz.
3. Orden recomendado de ejecución:
   - Ejecutar la celda **Preparacion general** (define funciones, utilidades y la ruta `RUTA_JSON`).
   - Ejecutar las celdas en orden (punto 1 → punto 5...), o usar `Kernel → Restart & Run All` para ejecutar todo desde cero.
4. Para ver sólo las respuestas desarrolladas, abrir `Electiva_IV_Lotero_Nino_Munoz_respuestas.ipynb`.

## Ejecutar y guardar salidas automáticamente
Para ejecutar todas las celdas y guardar las salidas en el mismo notebook (sin abrir UI):

```powershell
jupyter nbconvert --to notebook --execute Electiva_IV_Lotero_Nino_Munoz.ipynb --inplace
```

Esto ejecuta todas las celdas y persiste las salidas dentro del archivo `.ipynb`.

## Ejecutar el script Python (respaldo)
Si prefieres ejecutar el respaldo `.py` (si existe), desde la raíz:

```powershell
python "Electiva_IV_Lotero_Niño_Muñoz.py"
```

Asegúrate de usar el nombre exacto del archivo; PowerShell maneja caracteres especiales, pero si tienes problemas renómbralo temporalmente sin tildes.

## Archivos clave
- `Electiva_IV_Lotero_Nino_Munoz.ipynb` — Cuadernillo principal (celdas de enunciado, respuesta y código).
- `Electiva_IV_Lotero_Nino_Munoz_respuestas.ipynb` — Notebook con respuestas agregadas y ejemplos.
- `Electiva_IV_Lotero_Niño_Muñoz.py` — Versión script (respaldo ejecutable).
- `data/Unidad1_Reto.json` — Datos usados por el cuadernillo.

## Notas prácticas y errores comunes
- FileNotFoundError: ejecuta desde la raíz del proyecto para que `data/Unidad1_Reto.json` esté en la ruta relativa esperada.
- Problemas de codificación: los notebooks usan `utf-8`; abrir/guardar con `encoding="utf-8"` si editas con scripts.
- Si una celda lanza excepción, revisa primero la celda `Preparacion general` (definiciones y rutas).
- Para capturar salidas antes de entregar, usa `nbconvert --to notebook --execute --inplace` para incluir resultados en el `.ipynb`.

## ¿Quieres que lo ejecute por ti?
Puedo ejecutar el notebook aquí (crear y guardar las salidas) y devolverte el archivo actualizado. ¿Deseas que ejecute ahora `Electiva_IV_Lotero_Nino_Munoz.ipynb` y guarde las salidas en el notebook?