🔬 Laboratorio de Análisis Clínicos Minozzi: 
Este proyecto es una aplicación web desarrollada con Django bajo el patrón MVT (Modelo-Vista-Template), diseñada para gestionar la operativa básica de un laboratorio clínico.

✅ Guía de Pruebas (Orden sugerido)
Para evaluar el funcionamiento del sistema, se recomienda seguir estos pasos:
- Presentación: Explore la página de Inicio donde se presenta al staff profesional y las especialidades del laboratorio.
- Gestión de Pacientes:
    - Vaya a la sección "Pacientes".
    - Haga clic en el botón verde "Registrar Nuevo Paciente" y complete el formulario (Nombre, Apellido, DNI, etc.).
    - Verifique que el paciente aparezca en la lista desplegable.
- Configuración de Estudios:
    - Vaya a la sección "Estudios".
    - Utilice el botón "Nuevo Análisis" para agregar un estudio al catálogo (ej. "Perfil Lipídico", "$5000").
- Carga de Resultados:
    - Vaya a "Cargar Resultados".
    - Seleccione un paciente de la lista, el estudio realizado y suba un archivo de prueba en formato PDF.
- Búsqueda en BD:
    - Regrese a la sección de Pacientes.
    - Utilice la barra de búsqueda ingresando el DNI del paciente registrado para filtrar la tabla y acceder a sus detalles.

-Ingreso a Admin:
    - Usuario: admin
    - Contraseña: 1234567A.
