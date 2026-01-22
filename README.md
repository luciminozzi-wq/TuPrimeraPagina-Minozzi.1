# Laboratorio de Análisis Clínicos Minozzi 🔬
**Proyecto Final - Curso de Python | Coderhouse**

## 👩‍💻 Alumna
* **Nombre:** Lucila Fernanda Minozzi

## 📖 Descripción del Proyecto
Este proyecto consiste en una plataforma web integral para la gestión de un **Laboratorio de Análisis Clínicos**. La aplicación permite administrar pacientes, gestionar el catálogo de estudios ofrecidos y cargar resultados de forma segura. 

La plataforma cuenta con un sistema de usuarios diferenciado, donde los usuarios registrados pueden acceder a funcionalidades protegidas, gestionar su perfil personal y realizar búsquedas avanzadas en la base de datos.

---

## 🛠️ Tecnologías Utilizadas
* **Python** (Lógica de programación)
* **Django** (Framework Web)
* **SQLite** (Base de datos)
* **Bootstrap** (Diseño y estilos)
* **HTML/CSS** (Estructura y plantillas)

---

## 🚀 Funcionalidades Principales (Checklist de Requisitos)

### 1. Gestión de Modelos (CRUD)
* **Pacientes:** Modelo principal con campos de texto, imagen (foto), fecha de nacimiento e **Integer con Unique=True (DNI)**.
* **Estudios:** Catálogo de análisis disponibles.
* **Resultados:** Relación entre pacientes y estudios con carga de archivos PDF/Imagen.

### 2. Secciones del Sitio
* **Home:** Vista de inicio con bienvenida.
* **About:** Página dedicada a la información del dueño/desarrollador (`/about`).
* **Buscador:** Filtrado de pacientes por DNI en tiempo real.

### 3. Sistema de Cuentas y Seguridad
* **Registro, Login y Logout:** Implementado para el manejo de sesiones.
* **Perfil de Usuario:** Cada usuario posee un avatar y biografía personalizable.
* **Cambio de Contraseña:** Sistema avanzado con validación de código de seguridad enviado por email.
* **Protección de Rutas:** Uso de `LoginRequiredMixin` y decoradores `@login_required` para asegurar que solo usuarios autenticados puedan editar o borrar registros.

---
-Ingreso a Admin:
    - Usuario: admin
    - Contraseña: 1234567A.
