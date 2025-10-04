## Ejecución Proyecto

**Resumen rápido:** clonar, crear/activar entorno (Python 3.12), instalar dependencias (requirements-minimal.txt), ejecutar el servidor y probar las rutas principales.

### Requisitos previos

- Git (para clonar el repositorio).

- Python 3.12 (instalar la versión 3.12.x).

- Si se tiene otras versiones, asegurarse de crear el virtualenv con el ejecutable de Python 3.12:
  
```
C:\Ruta\A\Python312\python.exe -m venv venv
```

- Microsoft Visual C++ Build Tools (Windows) — necesario para compilar algunos paquetes C:

- Abrir el instalador de Visual Studio Build Tools y seleccionar la carga de trabajo "Desarrollo para el escritorio con C++" (Desktop development with C++) y el Windows SDK si aparece.

- **Nota:** para evitar problemas con sincronización y permisos de OneDrive, se aconseja clonar el repo fuera de carpetas sincronizadas.


### Clonar y moverse a la rama correcta

```bash
# desde CMD o PowerShell
cd C:\ruta\donde\quieres\proyecto
git clone https://github.com/SantiBetancur/ARQUITECTURA_SFT_TALLER_1.git
cd P1_LocalMarket_Forked
```


### Crear y activar el entorno virtual (usar Python 3.12)

```bash
# Crear con el python 3.12:
python -m venv venv
```


### Activar (CMD):

```bash
venv\Scripts\activate
```


### (Otra opción) Activar PowerShell:

```bash
.\venv\Scripts\Activate.ps1
# Si PowerShell lanza error de ejecución, ejecutar (como administrador):
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Actualizar pip, setuptools y wheel

```bash
python -m pip install --upgrade pip setuptools wheel
```


### Muevete a LCM_US004 antes de instalar el archivo requirements-minimals.txt.

```bash
cd LCM_US004
```


### Instalar requerimientos

```bash
pip install -r requirements-minimal.txt
```

### Posible problema:

> Si se instala el requirements.txt completo y falla en paquetes como pydantic-core o mysqlclient:
> Error Microsoft Visual C++ 14.0 or greater is required → instalar Visual C++ Build Tools.



### Opcional (Intslación de mysqlclient): 

```bash
pip install mysqlclient
```

### Ejecutar servidor

```bash
# ubicarse en la carpeta que contiene manage.py (LCM_US004)
python manage.py runserver
```

### Acceso

```bash
Ingresa a http://127.0.0.1:8000/ desde un navegador web
```

### Errores frecuentes y soluciones rápidas

```bash
distutils.errors.DistutilsPlatformError: Microsoft Visual C++ 14.0 or greater is required
-> Instalar Visual C++ Build Tools (Seleccionar Desktop development with C++).

ERROR: Could not find a version that satisfies the requirement Pillow==10.2.0
-> Instalar una versión compatible o permitir una versión mayor (Pillow>=10.2.0) como en requirements-minimal.txt.

ImportError: cannot import name 'OpenAI' from 'openai'
-> Cambios en la librería openai entre versiones. Solución: actualizar código para usar la API 2.x
```


## Acceso a Wiki

A continuación se presenta el enlace a la wiki donde se presenta la documentación de todas las actividades propuestas en el taller.

**Link:** *https://github.com/SantiBetancur/ARQUITECTURA_SFT_TALLER_1/wiki*
