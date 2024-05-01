# Aplicación de Determinación de Género y Análisis de Edades

Este repositorio contiene una aplicación simple en Python para determinar si un nombre de usuario es de género masculino o femenino, así como un script para analizar la distribución de edades a partir de un archivo CSV.

## Requisitos

- Python 3.x: Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- pip: El gestor de paquetes de Python. Generalmente se instala automáticamente con Python 3.


## Configuración del Entorno Virtual

Se recomienda usar entornos virtuales para evitar conflictos entre las dependencias de diferentes proyectos. Sigue estos pasos para crear y activar un entorno virtual:

```bash
# Instalar la herramienta virtualenv si no está instalada
pip install virtualenv

# Crear un nuevo entorno virtual
virtualenv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate
# o (Linux/macOS)
source venv/bin/activate
```

## Instalación de Dependencias
Para instalar las librerías necesarias, ejecuta el siguiente comando después de activar tu entorno virtual:

```bash
pip install pandas
```

```bash
pip install matplotlib
```

## Archivos y Uso

### app.py

Este archivo contiene una función `girl_or_boy(nombre_usuario)` que determina el género de un nombre de usuario. Para ejecutarlo, simplemente llama a la función con el nombre de usuario como argumento. Ejemplo:

```bash
from app import girl_or_boy

print(girl_or_boy("fabian"))  # Salida: ¡ITS A BOY!
```

### main.py

Este script carga datos desde un archivo CSV, calcula las edades a partir de fechas de nacimiento, filtra las personas mayores de 25 años, y muestra un gráfico de la frecuencia de estas edades.

Para ejecutarlo, simplemente corre el script:

```bash
python main.py
```

El gráfico generado se mostrará en una ventana aparte.