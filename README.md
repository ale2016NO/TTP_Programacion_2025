# TTP_Programacion_2025 – Plataforma de Gestión de Stock

Este proyecto consiste en una plataforma web desarrollada con Python y Flask para gestionar el stock de productos, integrando autenticación de usuarios, carga de productos y un sistema básico de predicción de demanda.

## 🔧 Tecnologías utilizadas

- Python 3
- Flask
- HTML / Jinja2
- Replit (como entorno de despliegue)
- GitHub (control de versiones)

## 🚀 Funcionalidades principales

- Login de usuarios (admin / viewer)
- Dashboard con listado de productos
- Carga y modificación de productos
- API REST para agregar productos vía JSON (`/api/add_product`)
- Visualización simple de predicción de stock (versión simulada)

## 📂 Estructura del proyecto

```
├── app.py             # Lógica de la app Flask
├── data.json          # Archivo de datos persistente
├── templates/         # HTML de login y dashboard
├── test_api.html      # Formulario para probar la API
├── README.md          # Este archivo
```

## 🧪 Pruebas realizadas

- Funcionalidad general
- API test con Postman / formulario HTML
- Control de sesiones
- Simulación de predicción de demanda

## ✅ Cómo ejecutarlo

1. Cloná el repo o importalo desde Replit
2. Asegurate de tener `Flask` instalado
3. Ejecutá con:
   ```
   python app.py
   ```
4. Accedé desde el navegador a `http://localhost:5000/`

## 🔗 Recursos

- [Replit en vivo (si está activo)](https://replit.com/@rubenalejandron/stock-predictor-app-1)
- [Repositorio original en GitHub](https://github.com/ale2016NO/TTP_Programacion_2025)
