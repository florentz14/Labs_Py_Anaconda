try:
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
except ImportError as e:
    raise ImportError(
        'SQLAlchemy no está instalado. Instálalo con: pip install sqlalchemy'
    ) from e

import settings

# Crear motor y sesión globales
engine = create_engine(settings.DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def get_db():
    """Dependency de base de datos estilo FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    print('Database connection test:')
    with engine.connect() as connection:
        result = connection.execute(text('SELECT 1'))
        print(result.fetchall())
