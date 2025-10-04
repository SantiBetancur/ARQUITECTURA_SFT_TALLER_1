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
git clone 
cd P1_LocalMarket_Forked
git checkout development
git pull origin development
```


## Acceso a Wiki

A continuación se presenta el enlace a la wiki donde se presenta la documentación de todas las actividades propuestas en el taller.

**Link:** *https://github.com/SantiBetancur/ARQUITECTURA_SFT_TALLER_1/wiki*
