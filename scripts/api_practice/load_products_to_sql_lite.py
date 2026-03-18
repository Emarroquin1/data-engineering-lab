import pandas as pd
import sqlite3
import logging
import os

#configuracion de logs de python
logging.basicConfig(
    level=logging.INFO,
     #como mostrar logs en pantalla asctime . la fecha de impresion del log, levelname el nivel del log (INFO,ERROR,WARNING), message el mensaje del log 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Iniciando carga de productos a SQLite")

input_path = "data/processed/api_practice/products_processed.csv"
db_path = "data/bd/api_practice/products.db"

os.makedirs("data/bd/api_practice", exist_ok=True)

# validar existencia archivo
if not os.path.exists(input_path):
    logging.error("No existe el archivo processed")
    raise FileNotFoundError(input_path)

# leer dataset
df = pd.read_csv(input_path)
logging.info(f"Dataset leído correctamente. Registros: {len(df)}")

if os.path.exists(db_path):
    os.remove(db_path)
    logging.info(f"Base de datos existente eliminada: {db_path}")

# conexión SQLite
conn = sqlite3.connect(db_path)

# cargar tabla
df.to_sql(
    name="products",
    con=conn,
    if_exists="replace",
    index=False
)

conn.close()

logging.info("Carga completada. Tabla products creada en SQLite")