# Definición de la clase Producto - esto es la plantilla para crear objetos de tipo producto
class Producto:
    #Método constructor: se ejecuta automáticamente al crear una nueva instancia
    def __init__(self, nombre, precio, cantidad):
        # self.nombre: atributo que almacena el nombre del producto
        self.nombre = nombre
        # self.precio: atributo que almacena el precio del producto
        self.precio = precio
        # self.cantidad: atributo que almacena la cantidad disponible en inventario
        self.cantidad = cantidad

    #Método para aumentar la cantidad disponible del producto
    def agregar_cantidad(self, cantidad):
        #Verifica si la cantidad a agregar es positiva
        if cantidad > 0:
            #Aumenta el atributo cantidad sumando el valor recibido
            self.cantidad += cantidad
            #Muestra mensaje confirmando la operación usando f-string
            print(f"Se han agregado {cantidad} unidades de {self.nombre}.")
        else:
            #Mensaje de error si la cantidad no es positiva
            print("La cantidad a agregar debe ser mayor que 0.")

    #Método para reducir la cantidad disponible del producto
    def eliminar_cantidad(self, cantidad):
        
        #Primera condición: cantidad positiva y suficiente stock disponible
        if cantidad > 0 and self.cantidad >= cantidad:
            #Reduce la cantidad restando el valor recibido
            self.cantidad -= cantidad
            print(f"Se han eliminado {cantidad} unidades de {self.nombre}.")
            
        #Segunda condición: cantidad no positiva
        elif cantidad <= 0:
            print("La cantidad a eliminar debe ser mayor que 0.")
        #Tercera condición: cantidad insuficiente en inventario
        else:
            print(f"No hay suficientes unidades de {self.nombre} para eliminar {cantidad}.")

    #Método para mostrar toda la información del producto
    def mostrar_informacion(self):
        #Muestra el nombre del producto
        print(f"Nombre: {self.nombre}")
        #Muestra el precio con formato de 2 decimales (.2f)
        print(f"Precio: ${self.precio:.2f}")
        #Muestra la cantidad disponible
        print(f"Cantidad disponible: {self.cantidad}")

# --- CREACIÓN DE OBJETOS (INSTANCIAS) ---

#Crea primer objeto: producto1 con nombre "Camiseta", precio 15.99 y cantidad 10
producto1 = Producto("Camiseta", 15.99, 10)

#Crea segundo objeto: producto2 con nombre "Pantalón", precio 29.95 y cantidad 5
producto2 = Producto("Pantalón", 29.95, 5)

#Crea tercer objeto: producto3 con nombre "Zapatos", precio 44.99 y cantidad 12
producto3 = Producto("Zapatos", 44.99, 12)

# --- OPERACIONES CON LOS OBJETOS ---

#Llama al método agregar_cantidad() del producto1 para añadir 3 unidades
producto1.agregar_cantidad(3)

#Llama al método eliminar_cantidad() del producto2 para quitar 2 unidades
producto2.eliminar_cantidad(2)

#Llama al método mostrar_informacion() del producto3 para ver sus datos
producto3.mostrar_informacion()