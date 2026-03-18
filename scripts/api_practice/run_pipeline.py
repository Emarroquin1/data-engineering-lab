import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_pipeline():

    logging.info("Iniciando pipeline")

    scripts = [
        os.path.join(BASE_DIR, "extract_products.py"),
        os.path.join(BASE_DIR, "transform_products.py"),
        os.path.join(BASE_DIR, "load_products_to_sql_lite.py")
    ]

    for script in scripts:
        logging.info(f"Ejecutando {script}")
        result = os.system(f"python {script}")

        if result != 0:
            logging.error(f"Error ejecutando {script}")
            return

    logging.info("Pipeline finalizado")

if __name__ == "__main__":
    run_pipeline()