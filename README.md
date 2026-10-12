# Seminario de Integración 🚀

**Universidad UTE**

**Facultad:** Escuela de tecnologias - UTE

**Carrera:** Desarrollo de software

**Autor:** Diego Calderòn

**Periodo Académico:** Octubre 2026 - Marzo 2027

## 📖 Descripción del Proyecto

Este repositorio contiene los apuntes, prácticas y proyectos desarrollados durante la materia de **Seminario de Integración**. El objetivo principal es repasar y unificar conocimientos de desarrollo backend y frontend moderno, creando aplicaciones web completas, escalables y eficientes.

## 🛠️ Tecnologías y Conceptos Clave

Durante este curso, trabajaremos con un stack tecnológico moderno que abarca desde la gestión del entorno hasta la interfaz de usuario:

### 🐍 Python
Es un lenguaje de programación de propósito general, de alto nivel y multiparadigma. Destaca por su sintaxis clara y legible. En este seminario, servirá como la base lógica para construir nuestros servicios del lado del servidor.

### ⚡ uv
Es un gestor de paquetes y entornos (virtual environments) para Python extremadamente rápido, escrito en Rust. Reemplaza herramientas tradicionales como `pip` o `virtualenv`, mejorando significativamente los tiempos de instalación y resolución de dependencias, lo que agiliza el flujo de desarrollo.

### 🚀 FastAPI
Es un framework web moderno y de alto rendimiento para construir APIs con Python, basado en la especificación estándar de Python para sugerencias de tipo (Type Hints). Sus principales ventajas son su velocidad (comparable a NodeJS y Go), validación automática de datos y generación de documentación interactiva (Swagger UI y ReDoc) por defecto.

### 🅰️ Angular
Es un framework de desarrollo frontend mantenido por Google, basado en TypeScript. Se utiliza para construir aplicaciones de una sola página (SPA - Single Page Applications) robustas y escalables. Utiliza una arquitectura basada en componentes, inyección de dependencias y un potente sistema de enrutamiento.

## ⚙️ Estructura del Repositorio

*(Puedes adaptar esta sección a medida que crees tus carpetas)*

```text
📦 seminario-integracion
 ┣ 📂 backend          # Proyecto FastAPI y dependencias gestionadas con uv
 ┣ 📂 frontend         # Proyecto Angular
 ┣ 📜 .gitignore       # Archivo de ignorados (generado previamente)
 ┗ 📜 README.md        # Documentación principal
```

## 🚀 Cómo empezar (Guía Rápida)

**Backend (Python + uv + FastAPI):**

1. Crear el entorno virtual: `uv venv`
2. Activar el entorno: `source .venv/bin/activate` (en Linux/Mac) o `.venv\Scripts\activate` (en Windows)
3. Instalar dependencias: `uv pip install fastapi uvicorn`
4. Ejecutar el servidor: `uvicorn main:app --reload`

**Frontend (Angular):**

1. Instalar dependencias: `npm install`
2. Ejecutar el servidor de desarrollo: `ng serve`