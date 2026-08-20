from sqlmodel import SQLModel, create_engine, Session

# Usamos SQLite para desarrollo rápido y pruebas locales, compatible con la lógica de MySQL
sqlite_file_name = "voice_agent.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session