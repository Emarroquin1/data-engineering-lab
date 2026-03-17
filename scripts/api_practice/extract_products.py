import requests
import logging
import pandas as pd

# configurar logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Iniciando proceso de extraccion para dummyjson")

url = "https://dummyjson.com/products"
response = requests.get(url)

#La f antes de la cadena de texto es para meter variables en una cadena string 
logging.info(f"API status: {response.status_code}")
data = response.json()
logging.info(f"Total de productos: {len(data['products'])}")
#definier la data de los productos en una variable para luego convertirla en un archivo excel
productos = data.get('products', [])
#convertir la data de la api en un archivo excel
df = pd.DataFrame(productos)
#guardar el archivo csv en la carpeta data/raw con el nombre products.csv
#index=False es para que no se guarde el indice del dataframe en el archivo excel
df.to_csv('data/raw/products.csv', index=False)
logging.info("Archivo products.csv creado exitosamente")