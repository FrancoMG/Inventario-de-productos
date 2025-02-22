*** Cómo ejecutar la aplicación ***

1. Pre-requisitos:  
   - Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde la página oficial de Python (https://www.python.org/downloads/).
   - Instala las dependencias necesarias, como las librerías 'sqlite3' y 'colorama' (opcional), si no las tienes ya instaladas. Para instalar 'colorama', ejecuta el siguiente comando en tu terminal o consola:  

     * pip install colorama

2. Configuración inicial:  
   - Descarga o clona el archivo de código fuente del programa.
   - Coloca el archivo en una carpeta específica para facilitar su ejecución.

3. Ejecución del programa:
   - Abre tu editor de código favorito.
   - Usa la opción Abrir carpeta para seleccionar la carpeta donde se encuentra el archivo del programa.
   - Localiza el archivo principal del programa.
   - Presiona el botón de "Run" en la interfaz del editor.
   - El programa se ejecutará en la terminal integrada del editor.
  
4. Interacción con el programa:  
   - Una vez iniciado, el programa mostrará un menú con varias opciones, como registrar productos, mostrar productos, actualizar información, etc.
   - Ingresa el número correspondiente a la opción que deseas utilizar y sigue las instrucciones en pantalla.

5. Notas adicionales:  
   - Si no se encuentra una base de datos existente, el programa automáticamente creará una llamada 'Inventario.db'.
   - Asegúrate de cerrar correctamente el programa seleccionando la opción "Salir" del menú principal para evitar pérdidas de datos.
   - No puedes ingresar nombres de productos que se encuentren separados por espacios.

6. Problemas comunes:  
   - Si encuentras errores relacionados con dependencias, asegúrate de haber instalado `colorama` correctamente.




*** Descripción General ***

El programa gestiona un sistema de inventario de productos almacenados en una base de datos SQLite. Permite registrar, consultar, actualizar, eliminar y buscar productos, así como generar reportes sobre productos con bajo stock. La interfaz interactúa con el usuario a través de un menú en la terminal, utilizando la librería 'colorama' para mejorar la experiencia visual.

1. Funcionalidades Principales

1.1. Registrar Producto

Permite al usuario ingresar un nuevo producto al inventario. Solicita:

* Nombre del producto (texto obligatorio).
* Descripción del producto (texto obligatorio).
* Cantidad en stock (entero mayor que 0).
* Precio del producto (número mayor o igual a 0).
* Categoría del producto (texto opcional).

Se validan los campos ingresados para garantizar que sean válidos antes de registrar el producto en la base de datos.


1.2. Mostrar Productos

Lista todos los productos almacenados en la base de datos, mostrando:

* ID del producto.
* Nombre.
* Descripción.
* Cantidad.
* Precio.
* Categoría.

Si no hay productos registrados, informa al usuario.


1.3. Actualizar Producto

Permite actualizar la cantidad en stock de un producto existente. Solicita:

* ID del producto.
* Nueva cantidad (entero mayor o igual a 0).

Si el ID proporcionado no existe, informa al usuario. También permite abortar la operación si el usuario decide no continuar.


1.4. Eliminar Producto

Elimina un producto del inventario. Solicita:

* ID del producto a eliminar.

Si el ID proporcionado no existe, informa al usuario. También permite abortar la operación si el usuario decide no continuar.


1.5. Buscar Producto

Permite buscar un producto (o varios) por su ID, nombre o categoría. Muestra la información completa de/los producto/s si existe:

* ID.
* Nombre.
* Descripción.
* Cantidad.
* Precio.
* Categoría.

Si alguno de los 3 datos no existe, informa al usuario.


1.6. Reportar Stock Bajo

Genera un informe de productos con stock inferior o igual a un límite definido por el usuario. Solicita:

* Límite de stock (entero mayor o igual a 0).

Muestra la cantidad de productos que cumplen con el criterio y su información detallada.


1.7. Salir

Termina la ejecución del programa.


2. Validaciones

El programa realiza diversas validaciones para garantizar la integridad de los datos:

* Comprueba que los campos obligatorios no estén vacíos.
* Verifica que los valores numéricos sean positivos o mayores que 0, según corresponda.
* Asegura que los datos ingresados sean del tipo adecuado (texto o números).


3. Tecnologías Utilizadas 

* SQLite3: Para la gestión de la base de datos.
* Colorama: Para estilizar los mensajes en la terminal.


4. Tabla de la Base de Datos

La base de datos contiene una tabla llamada Productos con las siguientes columnas:

* Id (INTEGER, clave primaria, auto_incremental).
* Nombre (TEXT, obligatorio).
* Descripción (TEXT).
* Cantidad (INTEGER, obligatorio).
* Precio (REAL, obligatorio).
* Categoría (TEXT).


5. Flujo del Programa

* Inicio: Se verifica o crea la base de datos con su tabla correspondiente.
* Menú Principal: Presenta las opciones descritas anteriormente.
* Interacción con el Usuario: Según la opción seleccionada, se ejecuta la funcionalidad correspondiente.
* Cierre: Se cierra la conexión con la base de datos y finaliza el programa.

