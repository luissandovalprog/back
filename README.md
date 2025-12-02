1. Objetivos del Proyecto
El objetivo principal es demostrar la implementación de una aplicación Django funcional, segura y bien estructurada, cubriendo los siguientes puntos clave:

Modelado de Dominio: Creación de modelos Autor y Libro con una relación ForeignKey (1-N).

Autenticación Personalizada: Implementación de un CustomUser que hereda de AbstractUser para incluir un campo rol.

Control de Acceso (Roles):

Bibliotecario: Acceso total al CRUD (Crear, Leer, Actualizar, Eliminar) de Autores y Libros.

Lector: Acceso de solo lectura (ver listas y detalles).

CRUD Completo: Uso de Vistas Basadas en Clases (CBV) para gestionar las entidades.

Seguridad: Implementación de login_required, UserPassesTestMixin (decoradores de roles) y protección CSRF en todos los formularios.

Configuración Profesional: Uso de python-dotenv para gestionar secretos (SECRET_KEY, Base de Datos) fuera del código fuente.

Base de Datos: Configuración del proyecto para operar sobre MariaDB.

            _________________________________________________________________________-

Framework: Django 4.2+

Base de Datos: MariaDB (usando conector mysqlclient)

Gestión de Entorno: python-dotenv (para settings.py y .env)

Frontend: Bootstrap 5 (para plantillas)

2. Arquitectura y Modelo de Dominio
El proyecto se estructura en dos aplicaciones principales: usuarios y catalogo.

App usuarios
Modelo: CustomUser(AbstractUser)

Campo Adicional: rol = models.CharField(choices=Roles.choices, default=Roles.LECTOR)

Roles Definidos:

Bibliotecario: Acceso CRUD total.

Lector: Acceso de solo lectura (lista y detalle).

Control de Acceso: Se implementa a través de un Mixin personalizado (usuarios.decorators.BibliotecarioRequiredMixin) que valida si request.user.rol == 'Bibliotecario'.

App catalogo
Modelos:

Autor: nombre, apellido, biografia.

Libro: titulo, ano_publicacion, autor (ForeignKey a Autor).

Vistas: Se utilizan Vistas Basadas en Clases (CBV) para todo el CRUD (ListView, DetailView, CreateView, UpdateView, DeleteView).

Seguridad: Las vistas de C/U/D están protegidas por LoginRequiredMixin y BibliotecarioRequiredMixin.

            _______________________________________________________________________

4. Puesta en Marcha Rápida
Se asume un entorno virtual activado y git instalado.

1. Dependencias

    # Instalar dependencias de Python
    pip install -r requirements.txt

2. Base de Datos (MariaDB)
    
    ingrese a la terminal MySql Client (MariaDb).

        CREATE DATABASE biblioteca_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

        CREATE USER 'biblioteca_user'@'localhost' IDENTIFIED BY '123456789';

        GRANT ALL PRIVILEGES ON biblioteca_db.* TO 'biblioteca_user'@'localhost';

        FLUSH PRIVILEGES;

3. Variables de Entorno
    
    Cree un archivo .env en la raíz del proyecto. settings.py está configurado para leer estos valores.

        DB_NAME=biblioteca_db
        DB_USER=biblioteca_user
        DB_PASSWORD=123456789
        DB_HOST=127.0.0.1
        DB_PORT=3306

5. Inicialización y Escenario de Pruebas
Siga estos pasos para ejecutar la aplicación y probar la lógica de roles.

    1. Migrar e Iniciar

        python manage.py makemigrations

        python manage.py migrate
        
        python manage.py createsuperuser

        python manage.py runserver

    2. Escenario de Prueba: Rol "Bibliotecario"

        Este es el flujo para probar los permisos de administrador.
        
            Acceder al Admin: Vaya a http://127.0.0.1:8000/admin/

            Iniciar Sesión: Use las credenciales del superusuario creado.

            Asignar Rol:

                Vaya a la sección "Usuarios".

                Haga clic en su superusuario.

                En el campo "Rol", cambie el valor Lector (defecto) a Bibliotecario.

                Guarde los cambios.

            Probar CRUD:

                Vaya al sitio principal (ej. http://127.0.0.1:8000/autores/).

                Resultado Esperado: El usuario verá los botones "Crear Nuevo Autor", "Editar" y "Eliminar". El acceso a las vistas de C/U/D está permitido.

    3. Escenario de Prueba: Rol "Lector"

        Este es el flujo para probar los permisos restringidos de un usuario estándar.

            Cerrar Sesión: Salga de la cuenta de Administrador.

            Registro: Vaya a http://127.0.0.1:8000/cuentas/registro/.

            Crear Cuenta: Registre un nuevo usuario (ej. su nombre). Este usuario tendrá el rol Lector por defecto.

            Iniciar Sesión: Ingrese con la cuenta que creo.

            Probar Acceso:

                Vaya a http://127.0.0.1:8000/autores/.

                Resultado Esperado: El usuario no verá los botones "Crear", "Editar" o "Eliminar".

                Intente acceder manualmente a una URL protegida (ej. .../autores/nuevo/ o .../autores/1/editar/).

                Resultado Esperado: Será redirigido al home y recibirá un mensaje de "Acceso denegado".

            __________________________________________________________________________

Diagrama de Entidades y Responsabilidades (Esquema Textual)
Este esquema define las principales entidades del sistema, sus conexiones y el integrante del equipo responsable de su implementación y mantenimiento.

Equipo:

    Integrante 1: Luis Antonio Sandoval Sepulveda

1. Entidad: CustomUser (App: usuarios)

    Descripción: Modelo de usuario personalizado que gestiona la autenticación y los roles.

    Liderado por: Integrante 1

    Atributos Clave:

        username (string)

        email (string)

        password (hash)

        rol (string, Choices: 'Bibliotecario', 'Lector')

    Relaciones:

        (Ninguna relación directa con Autor o Libro en este modelo de dominio).

2. Entidad: Autor (App: catalogo)

    Descripción: Almacena la información biográfica de los autores.

    Liderado por: Integrante 1

    Atributos Clave:

        id (PK)

        nombre (string)

        apellido (string)

        biografia (text)

    Relaciones:

        Uno-a-Muchos (1:N) con Libro: Un Autor puede tener muchos Libros.

3. Entidad: Libro (App: catalogo)

    Descripción: Almacena la información de los libros individuales del catálogo.

    Liderado por: Integrante 1

    Atributos Clave:

        id (PK)

        titulo (string)

        ano_publicacion (integer)

        autor_id (ForeignKey a Autor)

    Relaciones:

        Muchos-a-Uno (N:1) con Autor: Un Libro pertenece exactamente a un Autor.