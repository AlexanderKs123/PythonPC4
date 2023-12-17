import requests
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TipoCambio(Base):
    __tablename__ = 'tipo_cambio'
    id = Column(Integer, primary_key=True)
    moneda_origen = Column(String)
    moneda_destino = Column(String)
    tasa_cambio = Column(Float)

def actualizar_tipo_cambio():
    # se obtiene datos de la API
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Crear un registro en la tabla tipo_cambio con los datos obtenidos de la API
        tipo_cambio = TipoCambio(
            moneda_origen=data['moneda_origen'],
            moneda_destino=data['moneda_destino'],
            tasa_cambio=float(data['tasa_cambio'])
        )

        engine = create_engine('sqlite:///app_database.db', echo=True)  
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(tipo_cambio)
        session.commit()

        print("Tipo de cambio actualizado exitosamente.")
    else:
        print("Error al obtener datos de la API.")

if __name__ == "__main__":
    actualizar_tipo_cambio()
