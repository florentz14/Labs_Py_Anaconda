import os
from pathlib import Path

# Cargar .env si está instalado
try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=Path(__file__).parent / '.env')
except ImportError:
    pass

# Variables de configuración, con valores por defecto si no están en el entorno
API_KEY = os.environ.get('API_KEY', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# URL de base de datos para SQLAlchemy (SQLite3 por defecto)
DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'sqlite:///./data/sql/database.db'
)

def get_required_env(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise EnvironmentError(f"Environment variable '{key}' is required but not set")
    return value


if __name__ == '__main__':
    print('Settings loaded:')
    print('DATABASE_URL=', DATABASE_URL)
