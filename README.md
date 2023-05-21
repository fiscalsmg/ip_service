# Ejercicio 2 prueba python

## Servicio para consultar paises por ip

### Software requerido

- Python >= 3.9
- Docker
- Make
- Git

### A continuación se describe la manera de probar el proyecto

### Ejecución sin Docker

#### Ejecución de FastAPI app

```PowerShell
(venv) PS C:\...\ip_service> uvicorn app.main:app --reload
```

#### Ejecución de pytest y coverage

```PowerShell
(venv) PS C:\...\ip_service> pytest -vv --cov-config=app/.coveragerc --cov=app tests/
```

### Ejecución con Docker

La construcción y ejecución del contenedor Docker está automatizada. El siguiente par de comandos son suficientes para _levantar_ y _detener_ la aplicación FastAPI. Para más detalles, ver archivo `Makefile` y `Dockerfile` asociados.

```PowerShell
(venv) PS C:\...\ip_service> make run
(venv) PS C:\...\ip_service> make stop
```

### Consumir el servicio usando Docker

Puede consumir este servicio de dos maneras

1. Usando el swagger del servicio

`http://127.0.0.1/docs`

2. Hacer uso de un software de consumo de APIs, se recomienda el uso de Insomnia

`http://127.0.0.1/countries`
con el siguiente esquema para consumo del API
{
"ip": "109.104.145.255"
}
