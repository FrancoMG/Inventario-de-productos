import sqlite3       #libreria de sqlite
from colorama import init, Fore, Back, Style        #libreria para poder personalizar la terminal con distintos estilos
init()

def baseD():
    conexion = sqlite3.connect("Inventario.db")            #conexion con la base de datos, en caso de no existir la crea
    cursor = conexion.cursor()        #se crea el cursor para poder realizar consultas a la base de datos
    cursor.execute("""CREATE TABLE IF NOT EXISTS Productos(
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre TEXT NOT NULL,
                    Descripcion TEXT,
                    Cantidad INTEGER NOT NULL,
                    Precio REAL NOT NULL,
                    Categoria TEXT)""")       #se crea la tabla en la base con sus respectivas columnas
    conexion.commit()         #se aplican los cambios hechos en la base de datos utilizando el commit
    conexion.close()          #se cierra la conexion con la base de datos
    
    
def registrar_producto():
    print(Fore.RED + "\n----- REGISTRO DE PRODUCTO -----" + Style.RESET_ALL)
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto: ")
    while nombre == "" or not nombre.isalpha():           #se verifica mientras el campo esta vacio o ingresa un dato que no sea una cadena de texto
        print(Fore.RED + Style.BRIGHT + "------------¡ERROR!------------\nEl nombre ingresado es inválido\n--------------------------------" + Style.RESET_ALL)
        nombre = input("Ingrese el nombre del producto: ")
            
    descripcion = input("Ingrese una descripción del producto: ")
    while descripcion == "" or not descripcion.isalpha():           #se verifica mientras el campo esta vacio o ingresa un dato que no sea una cadena de texto
        print(Fore.RED + Style.BRIGHT + "--------------¡ERROR!---------------\nLa descripción ingresada es inválida\n-------------------------------------" + Style.RESET_ALL)
        descripcion = input("Ingrese una descripción del producto: ")
        
    cantidad = input("Ingrese la cantidad del producto: ")
    while not cantidad.isdigit() or int(cantidad) <= 0:                    #se verifica mientras el campo esta vacio, si ingresa un dato no numerico o si el dato ingresado es menor o igual a 0
        print(Fore.RED + Style.BRIGHT + "-------------¡ERROR!-------------\nLa cantidad ingresada es inválida\n---------------------------------" + Style.RESET_ALL)
        cantidad = input("Ingrese la cantidad del producto: ")
    
    precio = input("Ingrese el precio del producto: ")
    while not precio.isdigit() or int(precio) < 0:            #se verifica mientras el campo esta vacio, si ingresa un dato no numerico o si el dato ingresado es menor a 0
        print(Fore.RED + Style.BRIGHT + "-------¡ERROR!-------\nEl precio es inválido\n---------------------" + Style.RESET_ALL)
        precio = input("Ingrese el precio del producto: ")
    
    categoria = input("Ingrese la categoria del producto: ")
    
    cursor.execute("INSERT INTO Productos(Nombre, Descripcion, Cantidad, Precio, Categoria) VALUES(?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))                     #se insertan los datos anteriores en la base de datos 
    conexion.commit()       #se aplican los cambios hechos en la tabla Productos utilizando el commit
    conexion.close()        #se cierra la conexion con la base de datos
    print(Fore.GREEN + Style.BRIGHT + "\n¡Producto registrado correctamente!" + Style.RESET_ALL)
    
    
def mostrar_productos():
    print(Fore.GREEN + "\n----- MOSTRAR PRODUCTOS -----" + Style.RESET_ALL)
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()
    if resultados:     #se verifica si existen valores dentro de la tabla Productos
        for registro in resultados:
            print(f"\nID: {registro[0]}\nNombre producto: {registro[1]}\nDescripción: {registro[2]}\nCantidad: {registro[3]}\nPrecio: {registro[4]}\nCategoría: {registro[5]}")
                        
    else:
        print(Fore.RED + Style.BRIGHT + "\nNo hay productos registrados" + Style.RESET_ALL)
        
    conexion.close()
        
        
def actualizar_producto():
    print(Fore.YELLOW + "\n----- ACTUALIZAR PRODUCTOS -----" + Style.RESET_ALL)
    terminado = False            #se crea una variable booleana para determinar cuando se termina de utilizar esta seccion del menu principal
    while terminado == False:                  #mientras la variable booleana sea falso, ejecuta el siguiente bloque de codigo 
        conexion = sqlite3.connect("Inventario.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Productos")
        resultados = cursor.fetchall()
        if resultados:                #se verifica si existen valores dentro de la tabla Productos
            id = input("Ingrese el ID del producto que desea actualizar: ")
            while not id.isdigit() or int(id) <= 0:           #se verifica mientras el dato no sea un dato numerico o si el dato ingresado es menor o igual a 0
                print(Fore.RED + Style.BRIGHT + "------------¡ERROR!------------\nEl dato ingresado es inválido\n-------------------------------" + Style.RESET_ALL)
                id = input("Ingrese el ID del producto que desea actualizar: ")
            cursor.execute("SELECT * FROM PRODUCTOS WHERE Id = ?", (id,))
            buscar_id = cursor.fetchone()
            if buscar_id:               #se verifica si existe el id del producto ingresado
                cursor.execute("SELECT Nombre FROM Productos WHERE Id = ?", (id,))
                nombreP = cursor.fetchone()
                respuesta = input(f"El producto a actualizar es {nombreP[0]}, ¿Desea continuar con este producto? (1 para si | 0 para no): ")
                while not respuesta.isdigit() or int(respuesta) < 0 or int(respuesta) > 1:              #se verifica mientras el campo este vacio, si ingresa un dato no numerico, si ingresa un valor menor a 0 o mayor a 1
                    print(Fore.RED + Style.BRIGHT + "------------¡ERROR!------------\nEl dato ingresado es inválido\n-------------------------------" + Style.RESET_ALL)
                    respuesta = input(f"El producto a actualizar es {nombreP[0]}, ¿Desea continuar con este producto? (1 para si | 0 para no): ")
                        
                if int(respuesta) == 1:             #si el usuario desea continuar con dicho producto
                    cantidad_nueva = input("Ingrese la nueva cantidad del producto: ")
                    while not cantidad_nueva.isdigit() or int(cantidad_nueva) < 0:            #se verifica si el campo esta vacio, si el dato ingresado no es de tipo numerico o si el dato ingresado es menor a 0
                        print(Fore.RED + Style.BRIGHT + "------------¡ERROR!------------\nEl dato ingresado es inválido\n-------------------------------" + Style.RESET_ALL)
                        cantidad_nueva = input("Ingrese la nueva cantidad del producto: ")
                    cursor.execute("UPDATE Productos SET Cantidad = ? WHERE Id = ?", (cantidad_nueva, id))              #se actualiza el stock del producto con la cantidad que ingreso el usuario
                    conexion.commit()                #se guardan los cambios hechos en la tabla Productos con el commit
                    print(Fore.GREEN + Style.BRIGHT + "\n¡Producto actualizado correctamente!" + Style.RESET_ALL)
                    terminado = True         #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
                      
                elif int(respuesta) == 0:         #si el usuario no desea continuar con dicho producto
                    print(Style.BRIGHT + Fore.RED + "\nOperacion abortada" + Style.RESET_ALL)
                    terminado = True          #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
                
            else:
                print(Fore.RED + Style.BRIGHT + "\nEl ID del producto ingresado no existe" + Style.RESET_ALL)
                terminado = True       #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
                
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos registrados" + Style.RESET_ALL)
            terminado = True        #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
            
        conexion.close()          #se cierra la conexion con la base de datos
        
        
def eliminar_producto():
    print(Fore.BLUE + "\n----- ELIMINAR PRODUCTO -----" + Style.RESET_ALL)
    terminado = False          #se crea una variable booleana para determinar cuando se termina de utilizar esta seccion del menu principal
    while terminado == False:                        #mientras la variable booleana sea falso, ejecuta el siguiente bloque de codigo 
        conexion = sqlite3.connect("Inventario.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Productos")
        resultados = cursor.fetchall()
        if resultados:              #se verifica si existen valores dentro de la tabla Productos
            id = input("Ingrese el ID del producto que desea eliminar: ")
            while not id.isdigit() or int(id) <= 0:          #se verifica mientras el campo este vacio, si ingresa un dato no numerico o si ingresa un valor menor o igual a 0
                print(Fore.RED + Style.BRIGHT + "------------¡ERROR!------------\nEl dato ingresado es inválido\n-------------------------------" + Style.RESET_ALL)
                id = input("Ingrese el ID del producto que desea eliminar: ")
                
            cursor.execute("SELECT * FROM PRODUCTOS WHERE Id = ?", (id,))
            buscar_id = cursor.fetchone()
            if buscar_id:              #se verifica si existe el id del producto ingresado
                cursor.execute("SELECT Nombre FROM Productos WHERE Id = ?", (id,))
                nombreP = cursor.fetchone()
                respuesta = input(f"El producto a eliminar es {nombreP[0]}, ¿Desea continuar con este producto? (1 para si | 0 para no): ")
                while not respuesta.isdigit() or int(respuesta) < 0 or int(respuesta) > 1:             #se verifica mientras el campo este vacio, si ingresa un dato no numerico, si ingresa un valor menor a 0 o mayor a 1
                    print(Fore.RED + Style.BRIGHT + "------------¡ERROR!------------\nEl dato ingresado es inválido\n-------------------------------" + Style.RESET_ALL)
                    respuesta = input(f"El producto a eliminar es {nombreP[0]}, ¿Desea continuar con este producto? (1 para si | 0 para no): ")
                    
                if int(respuesta) == 1:             #si el usuario desea continuar con dicho producto
                    cursor.execute("DELETE FROM Productos WHERE Id = ?", (id,))     #se elimina el producto de la tabla Productos 
                    conexion.commit()            #se guardan los cambios hechos en la tabla Productos con el commit
                    print(Style.BRIGHT + Fore.GREEN + "\n¡Producto eliminado correctamente!" + Style.RESET_ALL)
                    terminado = True           #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
                      
                elif int(respuesta) == 0:           #si el usuario no desea continuar con dicho producto
                    print(Fore.RED + Style.BRIGHT + "\nOperacion abortada" + Style.RESET_ALL)
                    terminado = True       #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
                
            else:            #si no existe el id del producto ingresado
                print(Fore.RED + Style.BRIGHT + "\nEl ID del producto ingresado no existe" + Style.RESET_ALL)
                terminado = True       #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
                
        else:             #si no existen valores dentro de la tabla Productos
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos registrados" + Style.RESET_ALL)
            terminado = True        #se cambia el valor de la variable terminado a True, por lo que el programa vuelve al menu principal
            
        conexion.close()            #se cierra la conexion con la base de datos
        
        
def buscar_producto():
    print(Fore.MAGENTA + "\n----- BUSCAR PRODUCTOS -----" + Style.RESET_ALL)
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()
    if resultados:       #se verifica si existen valores en la tabla Productos
        buscar = input("Ingrese el ID, nombre o categoría del producto que desea buscar: ")
        while buscar == "":           #se verifica mientras el campo este vacio
            print(Fore.RED + Style.BRIGHT + "---------------------¡ERROR!----------------------\nDebe ingresar alguno de los 3 datos para continuar\n--------------------------------------------------" + Style.RESET_ALL)
            buscar = input("Ingrese el ID, nombre o categoria del producto que desea buscar: ")
        
        cursor.execute("SELECT * FROM Productos WHERE Id = ? OR Nombre = ? OR Categoria = ?", (buscar, buscar, buscar))
        producto = cursor.fetchall()
        if producto:       #se verifica si existe el id del prodcuto ingresado
            cursor.execute("SELECT COUNT(*) FROM Productos WHERE Id = ? OR Nombre = ? OR Categoria = ?", (buscar, buscar, buscar,))
            encontrados = cursor.fetchone()
            print(Fore.GREEN + Style.BRIGHT + f"\nSe ha encontrado {encontrados[0]} resultado/s posible" + Style.RESET_ALL)
            for registro in producto: 
                print(f"\nID: {registro[0]}\nNombre del producto: {registro[1]}\nDescripcion: {registro[2]}\nCantidad: {registro[3]}\nPrecio: {registro[4]}\nCategoria: {registro[5]}")
            
        else:              #si no existe el id del producto 
            print(Fore.RED + Style.BRIGHT + "\nEl producto ingresado no existe" + Style.RESET_ALL)
            
    else:              #si no existen valores dentro de la tabla Productos
        print(Fore.RED + Style.BRIGHT + "\nNo hay productos registrados" + Style.RESET_ALL)
        
    conexion.close()
    
    
def stock_bajo():
    print(Fore.CYAN + "\n----- REPORTE DE STOCK BAJO -----" + Style.RESET_ALL)
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()
    if resultados:      #se verifica si existen valores en la tabla Productos
        stock = input("Ingrese el limite de stock a informar: ")
        while not stock.isdigit() or int(stock) < 0:           #se verifica mientras el campo este vacio, si ingresa un dato no numerico o si ingresa un valor menor o igual a 0
            print(Fore.RED + Style.BRIGHT + "------------¡ERROR!------------\nEl dato ingresado es inválido\n-------------------------------" + Style.RESET_ALL)
            stock = input("Ingrese el limite de stock a informar: ")
        
        cursor.execute("SELECT COUNT(*) FROM Productos WHERE Cantidad <= ?", (stock,))          #se hace una consulta para que cuente la cantidad de prodcutos con una cantidad menor a la ingresada anteriormente
        productos = cursor.fetchone()
        print(Fore.GREEN + f"\nHay {productos[0]} producto/s con stock bajo" + Style.RESET_ALL)
        cursor.execute("SELECT * FROM Productos WHERE Cantidad <= ?", (stock,))      #se hace una consulta para que muestre todos los prodcutos con una cantidad menor a la ingresada anteriormente
        producto = cursor.fetchall()
        for registro in producto:
            print(f"\nID: {registro[0]}\nNombre del producto: {registro[1]}\nDescripcion: {registro[2]}\nCantidad: {registro[3]}\nPrecio: {registro[4]}\nCategoria: {registro[5]}")
            
    else:        #si no existen valores dentro de la tabla Productos
        print(Fore.RED + Style.BRIGHT + "\nNo hay productos registrados" + Style.RESET_ALL)
        
        
def menu():
    print(Style.BRIGHT + "\n---------------------------\nMenú Principal\n---------------------------" + Style.RESET_ALL)
    print(Fore.RED + "1. Registrar producto" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Mostrar productos" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Actualizar productos" + Style.RESET_ALL)
    print(Fore.BLUE + "4. Eliminar productos" + Style.RESET_ALL)
    print(Fore.MAGENTA + "5. Buscar productos" + Style.RESET_ALL)
    print(Fore.CYAN + "6. Reportar stock bajo" + Style.RESET_ALL)
    print(Fore.BLACK + "7. Salir" + Style.RESET_ALL)
    respuesta = int(input("\nIngrese una opcion: "))
    return respuesta
    

baseD()
while True:      #mientras que sea verdadero, que ejecute el siguiente bloque de codigo todo el tiempo
    opcion = menu()       #se guarda en la variable opcion el resultado de la funcion menu 
    if opcion == 1:
        registrar_producto()
    
    elif opcion == 2:
        mostrar_productos()
        
    elif opcion == 3:
        actualizar_producto()
        
    elif opcion == 4:
        eliminar_producto()
     
    elif opcion == 5:
        buscar_producto()
        
    elif opcion == 6:
        stock_bajo()
        
    elif opcion == 7:
        print("\nSaliendo del programa...\n")
        break
    
    else:      #si no se elige ninguna de las opciones del menu
        print(Fore.RED + Style.BRIGHT + "\nLa opcion ingresada no es valida" + Style.RESET_ALL)