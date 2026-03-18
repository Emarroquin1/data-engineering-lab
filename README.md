# 🧪 Data Engineering Lab

## 🎯 Objetivo del Proyecto

Este laboratorio tiene como objetivo practicar e implementar diferentes tipos de extracción de datos utilizados en Ingeniería de Datos.

Se busca simular escenarios reales donde un Data Engineer debe obtener información desde múltiples fuentes como:

- APIs
- Archivos CSV
- Bases de datos
- Archivos JSON
- Otras fuentes externas

Posteriormente estos datos son transformados, enriquecidos con métricas analíticas y cargados en una capa de persistencia para su análisis.

El proyecto funciona como un entorno de experimentación y aprendizaje práctico de pipelines ETL.

---

## 🏗️ Arquitectura General del Pipeline

El flujo general del laboratorio es:

Fuente de datos  
↓  
RAW Layer  
↓  
Processed Layer  
↓  
Database Layer

Cada tipo de extracción tendrá su propio pipeline dentro del proyecto.

---

## 🔌 Tipos de Extracción que se Practican

Este laboratorio está diseñado para probar múltiples estrategias de extracción:

### 📄 Extracción desde CSV

Permite simular ingestión de archivos batch.

Ejemplo:

data/raw/api_practice/products.csv

---

### 🌐 Extracción desde API

Permite practicar consumo de servicios REST y manejo de JSON.

Script asociado:

scripts/api_practice/extract_products.py

---

### 🗄️ Extracción desde Base de Datos

Permite practicar lectura y escritura hacia motores SQL.

Salida:

data/bd/api_practice/products.db

---

### 📦 Extracción desde JSON (simulada o futura)

Se pueden agregar notebooks o scripts para probar carga de estructuras semiestructuradas.

---

## ⚙️ Transformación de Datos

Script:

scripts/api_practice/transform_products.py

Responsabilidades:

- Limpieza de datos
- Validación de campos
- Creación de métricas analíticas como:
  - estimated_revenue
  - discount_value
  - final_price

Salida:

data/processed/api_practice/products_processed.csv

---

## 💾 Carga de Datos

Script:

scripts/api_practice/load_products_to_sql_lite.py

Responsabilidades:

- Crear base SQLite
- Crear tabla analítica
- Insertar dataset transformado

Salida:

data/bd/api_practice/products.db

---

## 📂 Estructura del Proyecto

DATA-ENGINEERING-LAB

data  
 ├── raw  
 │ └── api_practice  
 │ └── products.csv  
 │  
 ├── processed  
 │ └── api_practice  
 │ └── products_processed.csv  
 │  
 └── bd  
 └── api_practice  
 └── products.db

notebooks  
 └── logica_metricas_DummyJSON.txt

scripts  
 └── api_practice  
 ├── extract_products.py  
 ├── transform_products.py  
 └── load_products_to_sql_lite.py

README.md

---

## ▶️ Cómo Ejecutar un Pipeline

Desde la raíz del proyecto:

### 1️⃣ Extraer

python scripts/api_practice/extract_products.py

### 2️⃣ Transformar

python scripts/api_practice/transform_products.py

### 3️⃣ Cargar

python scripts/api_practice/load_products_to_sql_lite.py

---

## 🚀 Propósito Educativo

Este laboratorio permite desarrollar habilidades en:

- Diseño de pipelines ETL
- Manejo de múltiples fuentes de datos
- Creación de datasets analíticos
- Automatización con Python
- Organización profesional de proyectos de datos
