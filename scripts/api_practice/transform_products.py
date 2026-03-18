import pandas as pd
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Iniciando transformación de productos")

input_path = "data/raw/api_practice/products.csv"
output_path = "data/processed/api_practice/products_processed.csv"

# Verificar que exista el archivo de entrada
if not os.path.exists(input_path):
    logging.error(f"No se encontró el archivo de entrada: {input_path}")
    raise FileNotFoundError(f"No existe el archivo {input_path}")

# Leer archivo raw
df = pd.read_csv(input_path)
logging.info(f"Archivo leído correctamente. Total registros: {len(df)}")

# Mostrar columnas disponibles
logging.info(f"Columnas disponibles: {list(df.columns)}")

# Seleccionar columnas útiles
columnas_utiles = [
    "id",
    "title",
    "category",
    "brand",
    "price",
    "discountPercentage",
    "rating",
    "stock"
]

df = df[columnas_utiles].copy()

# Renombrar columnas
df.rename(columns={
    "id": "product_id",
    "title": "product_name",
    "category": "category",
    "brand": "brand",
    "price": "price",
    "discountPercentage": "discount_percentage",
    "rating": "rating",
    "stock": "stock"
}, inplace=True)

# Limpiar nulos en brand
df["brand"] = df["brand"].fillna("Unknown")

#   metricas para contestar
#  ¿Cuánto dinero puedo generar?
#  ¿Cuánto dinero puedo generar?
#  ¿Cuál sería el precio real?


# Crear métricas
df["estimated_revenue"] = df["price"] * df["stock"]
df["discount_value"] = df["price"] * (df["discount_percentage"] / 100)
df["final_price"] = df["price"] - df["discount_value"]



# Redondear valores decimales
df["estimated_revenue"] = df["estimated_revenue"].round(2)
df["discount_value"] = df["discount_value"].round(2)
df["final_price"] = df["final_price"].round(2)

# Crear carpeta de salida si no existe
os.makedirs("data/processed/api_practice", exist_ok=True)

# Eliminar archivo de salida previo para guardar data nueva
if os.path.exists(output_path):
    os.remove(output_path)
    logging.info(f"Archivo existente eliminado: {output_path}")

# Guardar archivo transformado
df.to_csv(output_path, index=False)

logging.info(f"Transformación completada. Archivo guardado en: {output_path}")
logging.info("Vista previa de los datos transformados:")
logging.info(f"\n{df.head()}")