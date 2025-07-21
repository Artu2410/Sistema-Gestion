import sqlite3

# Creamos la tabla de productos
def crear_tabla():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT)"""
    )
    conn.commit()
    conn.close()  # Asegurarnos de cerrar la conexión

# Agregar un producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoria del producto: ")

    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (nombre, descripcion, cantidad, precio, categoria)
    )
    conn.commit()
    conn.close()  # Asegurarnos de cerrar la conexión
    print(f"Producto '{nombre}' agregado con exito.")

# Mostrar todos los productos
def mostrar_productos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()  # Asegurarnos de cerrar la conexión

    if productos:
        print("Inventario:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoria: {producto[5]}")
    else:
        print("No hay productos en el inventario.")

# Actualizar la cantidad de un producto
def actualizar_producto():
    id = int(input("Ingrese el ID del producto a actualizar: "))
    cantidad = int(input("Ingrese la nueva cantidad del producto: "))

    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?', (cantidad, id))
    conn.commit()
    conn.close()  # Asegurarnos de cerrar la conexión
    print(f"Producto con ID {id} actualizado con exito.")

# Eliminar un producto
def eliminar_producto():
    id = int(input("Ingrese el ID del producto a eliminar: "))

    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id = ?', (id,))
    conn.commit()
    conn.close()  # Asegurarnos de cerrar la conexión
    print(f"Producto con ID {id} eliminado con exito.")

# Buscar un producto por ID
def buscar_producto():
    id = int(input("Ingrese el ID del producto a buscar: "))

    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos WHERE id = ?', (id,))
    producto = cursor.fetchone()
    conn.close()  # Asegurarnos de cerrar la conexión

    if producto:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoria: {producto[5]}")
    else:
        print("No se encontro ningun producto con ese ID.")

# Reporte de bajo stock
def reporte_bajo_stock():
    limite = int(input("Ingrese el limite de cantidad para el reporte: "))

    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos WHERE cantidad <= ?', (limite,))
    productos = cursor.fetchall()
    conn.close()  # Asegurarnos de cerrar la conexión

    if productos:
        print(f"Productos con cantidad menor o igual a {limite}:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoria: {producto[5]}")
    else:
        print("No hay productos con bajo stock.")

# Menu principal para interactuar con el usuario
def main():
    crear_tabla()
    while True:
        print("-" * 40)
        print("\nMenu")
        print("-" * 40)
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_bajo_stock()
        elif opcion == '7':
            print("¡Gracias por usar el sistema de gestion de productos!")
            break
        else:
            print("Opcion invalida. Por favor, seleccione una opcion.")
main()