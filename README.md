City-N-Bike
Sistema de gestión de movilidad urbana en bicicleta.

Plataforma desarrollada para la visualización de estaciones en tiempo real, gestión de perfiles de usuario, planes de membresía e historial de puntos de fidelización.

Tecnologias
Backend: Python / Flask

Frontend: HTML5, CSS3, JavaScript

Mapas: Leaflet.js

Base de datos: SQLite (SQLAlchemy)

Funcionalidades principales
Mapa interactivo: Visualización de estaciones y disponibilidad de bicicletas.

Registro y autenticacion: Manejo de sesiones y validación de usuarios.

Sistema de puntos: Seguimiento de puntos y niveles de usuario.

Panel de usuario: Acceso a perfil personal y selección de planes.

Despliegue local
Instalar dependencias:
pip install -r requirements.txt

Ejecutar la aplicación:
python app.py

Acceder en el navegador a http://127.0.0.1:5000.

Proyecto finalizado - Mayo 2025.

Validación de Formularios: El endpoint /registro implementa lógica de sanitización y verificación de datos duplicados (ID) antes de procesar el registro.

UI Dinámica: Navegación persistente (nav-bar) mediante eventos onclick que garantizan una experiencia fluida entre módulos.

UI/UX: Se requiere unificar las barras de navegación en un layout principal utilizando base.html y bloques de Jinja2 para evitar la repetición de código.
