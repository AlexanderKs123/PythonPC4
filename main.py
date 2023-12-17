from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TipoCambio(Base):
    __tablename__ = 'tipo_cambio'
    id = Column(Integer, primary_key=True)
    moneda_origen = Column(String)
    moneda_destino = Column(String)
    tasa_cambio = Column(Float)

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    direccion = Column(String)
    telefono = Column(String)

def config():
    engine = create_engine('sqlite:///app_database.db', echo=True)  # Cambia 'sqlite:///app_database.db' al motor de tu elección

    # Crea las tablas si no existen
    Base.metadata.create_all(bind=engine)

    # Ejemplo de cómo agregar registros a las tablas
    Session = sessionmaker(bind=engine)
    session = Session()

    # Agrega un tipo de cambio de ejemplo
    tipo_cambio_ejemplo = TipoCambio(moneda_origen='USD', moneda_destino='EUR', tasa_cambio=0.85)
    session.add(tipo_cambio_ejemplo)

    # Agrega un cliente de ejemplo
    cliente_ejemplo = Cliente(nombre='John Doe', direccion='123 Main St', telefono='555-1234')
    session.add(cliente_ejemplo)

    # Guarda los cambios
    session.commit()

    print("Configuración completa")

if __name__ == "__main__":
    config()