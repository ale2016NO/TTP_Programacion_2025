# TTP_Programacion_2025 – Plataforma de Gestión de Stock

Este proyecto corresponde al Trabajo Práctico Final de la materia **Taller de Programación Avanzada** (Lic. en Tecnologías Digitales – UTN 2025).

## 🧠 Descripción

La plataforma permite gestionar productos en stock con funciones de:
- Login por usuario con rol (admin o viewer)
- Listado de productos desde backend simulado
- Filtros por categoría
- Predicción de demanda simulada (con Flask)
- Interfaz construida con TailwindCSS
- Backend en Python con Flask

## 🚀 Funcionalidades principales

| Rol     | Acciones disponibles                           |
|---------|------------------------------------------------|
| Admin   | Ver productos, filtrar, lanzar predicción      |
| Viewer  | Ver productos, filtrar                         |

## 🧪 Pruebas QA incluidas

- Casos de prueba por Sprint 1, 3 y 4
- Casos backend (Products y Filter Products)
- Reporte de bugs simulado
- Planificación semanal (Trello-style)
- Funcionalidad Recruitment

## 🔧 Cómo ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/ale2016NO/TTP_Programacion_2025.git
cd TTP_Programacion_2025

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar servidor Flask
python app.py
```

Acceder en `http://127.0.0.1:5000/`

## 🔐 Credenciales de prueba

| Usuario | Contraseña | Rol     |
|---------|------------|---------|
| admin   | admin123   | admin   |
| viewer  | viewer123  | viewer  |

## 📁 Estructura del proyecto

```
.
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── productos.json
└── README.md
```

## 📄 Licencia

Este proyecto es parte del Trabajo Práctico Final con fines académicos.
