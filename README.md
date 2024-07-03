# My Flask API - SQL to Chia project 

Este es un proyecto básico para crear una API utilizando Flask, en proximas versiones se implementará las funcionaidaddes para la migración de la base de datos web 2 a web 3 en el marco de trabajo de Chia Coin.

## Desarrollador por: Mario x & Cristobal x

## Requisitos

- Python 3.6+
- Pip

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/my_flask_api.git
    cd my_flask_api
    ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install Flask
    ```

## Estructura del Proyecto

```
my_flask_api/
├── app/
│   ├── __init__.py
│   ├── routes.py
├── venv/
├── config.py
└── run.py
```

- `app/__init__.py`: Inicializa la aplicación Flask.
- `app/routes.py`: Define las rutas de la API.
- `config.py`: Contiene la configuración de la aplicación.
- `run.py`: Script para ejecutar la aplicación.

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
python run.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Rutas de la API

### `GET /api`

Devuelve un mensaje de bienvenida.

#### Respuesta

```json
{
  "message": "Hello, World!"
}
```

### `GET /api/users`

Devuelve una lista de usuarios.

#### Respuesta

```json
{
  "users": [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
  ]
}
```

## Configuración

La configuración de la aplicación se encuentra en `config.py`. Puedes modificar la `SECRET_KEY` y añadir otras configuraciones según tus necesidades.

```python
class Config:
    SECRET_KEY = 'supersecretkey'
    # Otras configuraciones
```

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.