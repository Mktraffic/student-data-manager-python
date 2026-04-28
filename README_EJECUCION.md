# README — Ejecución en Visual Studio Code

Este README describe cómo preparar el entorno y ejecutar el cuadernillo `Electiva_IV_Lotero_Nino_Munoz.ipynb` desde Visual Studio Code (Windows).

## Requisitos
- Python 3.8 o superior
- Extensión **Python** para VS Code (Microsoft)
- Extensión **Jupyter** para VS Code (Microsoft)
- Abrir el workspace en VS Code en la carpeta raíz del proyecto (donde están `Electiva_IV_Lotero_Nino_Munoz.ipynb` y la carpeta `data`)

## Preparar entorno en VS Code (recomendado)
1. Abrir VS Code en la carpeta del proyecto.
2. Crear un entorno virtual desde la terminal integrada (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install jupyter
```

3. En VS Code: abrir la paleta (`Ctrl+Shift+P`) → `Python: Select Interpreter` → seleccionar el intérprete de `.venv`.
4. Instalar y habilitar las extensiones `Python` y `Jupyter` si no están instaladas.

## Abrir y ejecutar el cuadernillo en VS Code
1. Abrir `Electiva_IV_Lotero_Nino_Munoz.ipynb` (doble clic) en el editor de notebooks de VS Code.
2. Ejecutar la celda **Preparacion general** (define funciones y `RUTA_JSON`).
3. Ejecutar las celdas en orden con el botón `Run Cell` de cada celda o usar `Run All` desde la barra del notebook.
4. Para reiniciar y ejecutar todo desde cero: usar `Restart Kernel and Run All` en la barra superior.
5. Ejecutar una celda rápidamente con `Shift+Enter` cuando el foco esté en ella.

## Ejecutar el script `.py` desde VS Code
1. Abrir `Electiva_IV_Lotero_Niño_Muñoz.py` en el editor.
2. Hacer clic en `Run Python File in Terminal` o ejecutar en la terminal integrada:

```powershell
python "Electiva_IV_Lotero_Niño_Muñoz.py"
```

Si tienes problemas con caracteres en el nombre, renombra temporalmente a `Electiva_IV_Lotero_Nino_Munoz.py`.

## Ejecutar y guardar salidas sin abrir la UI de Jupyter
En la terminal integrada puedes ejecutar y sobrescribir el notebook con salidas:

```powershell
jupyter nbconvert --to notebook --execute Electiva_IV_Lotero_Nino_Munoz.ipynb --inplace
```

## Comprobaciones y errores comunes
- FileNotFoundError: abre VS Code en la raíz del proyecto para que `data/Unidad1_Reto.json` exista en la ruta relativa esperada.
- Intérprete incorrecto: si faltan librerías o las importaciones fallan, asegúrate de haber seleccionado el intérprete `.venv` en VS Code.
- Codificación: usar `utf-8` si editas archivos fuera de VS Code.

## Archivos clave
- `Electiva_IV_Lotero_Nino_Munoz.ipynb` — Cuadernillo principal.
- `Electiva_IV_Lotero_Nino_Munoz_respuestas.ipynb` — Notebook con respuestas ampliadas.
- `Electiva_IV_Lotero_Niño_Muñoz.py` — Script respaldo ejecutable.
- `data/Unidad1_Reto.json` — Datos usados por el cuadernillo.

## ¿Deseas que lo ejecute por ti desde aquí?
Puedo ejecutar el notebook (`nbconvert --execute`) y guardar las salidas en el `.ipynb`. ¿Quieres que lo haga ahora?