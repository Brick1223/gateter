# Gateter 🐾

Gateter es una pequeña red social para amantes de los gatos, donde cada usuario puede publicar mensajes cortos llamados “maullidos”.

---

## 🧠 Objetivo del proyecto

El objetivo es construir una aplicación web que permita a los usuarios registrarse, iniciar sesión, publicar maullidos, y ver perfiles de otros usuarios de forma sencilla y clara.

---

## ✨ Funcionalidades implementadas

1. **Registro e inicio de sesión**
   - Registro con nombre de usuario y contraseña.
   - Inicio de sesión para usuarios existentes.
   - Autenticación con sesiones de Django.
   
2. **Publicación de maullidos**
   - Usuarios logueados pueden publicar mensajes de hasta 140 caracteres.
   - Cada maullido se guarda en la base de datos y se muestra en el perfil del usuario.
   - Ordenación de maullidos de más reciente a más antiguo.

3. **Perfiles de usuario**
   - Perfiles públicos accesibles mediante `/usuarios/<nombre>`.
   - Si el perfil no existe, se muestra un mensaje claro de “usuario no encontrado”.
   - Los usuarios pueden añadir maullidos desde su propio perfil.

4. **Búsqueda de usuarios**
   - Formulario de búsqueda para encontrar otros usuarios por nombre de usuario.
   - Muestra resultados con avatar, nombre y enlace al perfil.

5. **Interfaz básica**
   - Estilo tipo “WhatsApp” para los maullidos.
   - Sidebar con información del usuario y lista de usuarios conectados.

---

## 🛠 Tecnologías utilizadas

- **Backend:** Python 3 + Django 4.x
- **Frontend:** HTML5, CSS3, JavaScript
- **Base de datos:** SQLite (por defecto de Django)
- **Librerías adicionales:**  
  - `django.contrib.auth` para autenticación y gestión de usuarios  
  - Formularios de Django (`forms.ModelForm` y `UserCreationForm`)  

---

## 📦 Instalación y ejecución local

1. Clonar el repositorio:

```bash
git clone https://github.com/Brick1223/gateter.git
cd gateter

    Crear un entorno virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

    Instalar dependencias:

pip install -r requirements.txt

    Aplicar migraciones:

python manage.py migrate

    Crear superusuario (opcional):

python manage.py createsuperuser

    Ejecutar el servidor de desarrollo:

python manage.py runserver

    Acceder a la aplicación en tu navegador:

http://127.0.0.1:8000/

⚙️ Decisiones técnicas

    Django se eligió por su rápida configuración y manejo integrado de autenticación.

    SQLite se utilizó para simplicidad y pruebas locales; fácil de migrar a otra base de datos.

    Se implementaron formularios y validaciones usando forms.ModelForm.

    La arquitectura está separada en templates, static (CSS/JS) y apps, siguiendo buenas prácticas.

    Los maullidos se ordenan automáticamente por fecha de creación (ordering = ['-created_at']).

🚀 Posibles mejoras

    Implementar validaciones y alertas en tiempo real usando JavaScript.

    Mejorar la responsividad del diseño para móviles.

    Añadir “likes” o comentarios a los maullidos.

    Implementar notificaciones en tiempo real cuando un usuario nuevo publica un maullido.

    Añadir pruebas automáticas (unit tests) para asegurar la funcionalidad.

Uso:

Registrarse o iniciar sesión.

Publicar maullidos desde tu perfil.

Ver los últimos maullidos en la página principal.

Buscar usuarios desde la barra de búsqueda.

Acceder a perfiles de otros usuarios y ver sus maullidos.


Estructura del proyecto:

gateter/
├── meows/                 # Aplicación principal
│   ├── templates/         # Plantillas HTML
│   ├── static/            # CSS y JS
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── gateter/               # Configuración del proyecto
├── manage.py
