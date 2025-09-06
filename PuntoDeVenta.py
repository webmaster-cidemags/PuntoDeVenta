#Ejercicio 1: Crea variables para representar productos
#default data
#nombre_producto_1 = "Producto"  # Cadena (str)
#precio_1 = 00.00                # Flotante (float)
#cantidad_1 = 0                  # Entero (int)
#disponible_1 = False            # Booleano (bool)

lista=["Truza", "Sudadera", "Agregar Producto"]
stocks=[1,2,3]
stock1=["Truza",.99,5000,True]
stock2=["Sudadera",199.90,500,False]
stock3=["producto",00.00,000,False]

def menu_principal():
    print('--------------- BIENVENIDO A SISTEMA DE ADMINISTRACION DE STOCK ---------------')
    print('----------------SELECCIONA LA OPCION DESEADA: ---------------------------------')
    print('----------------1)REVISAR STOCK -----------------------------------------------')
    print('----------------2)CALCULAR PRECIO POR VOLUMEN ---------------------------------')
    print('----------------3)INGRESAR PRODUCTOS ------------------------------------------')
    print('----------------4) SALIR DEL SISTEMA ------------------------------------------')
    op=int(input('OPCIÓN: '))
    return op

def stock_general():
    for i in range(3):
        print(stocks[i])
        print(lista[i])
        

    #STOCK 1
    #Ejercicio 2: Muestra la información del producto
    print(f"Producto: {stock1[0]}")
    print(f"Precio: ${stock1[1]}")
    print(f"Cantidad en stock: {stock1[2]}")
    print(f"¿Disponible? {stock1[3]}")
    precio_1=stock1[1]
    cantidad_1=stock1[2]
    valor_total_1 = precio_1 * cantidad_1
    print(f"Valor total en stock 1: ${valor_total_1:.2f}")
    
    #STOCK 2
    print(f"Producto: {stock2[0]}")
    print(f"Precio: ${stock2[1]}")
    print(f"Cantidad en stock: {stock2[2]}")
    print(f"¿Disponible? {stock2[3]}")
    precio_2=stock2[1]
    cantidad_2=stock2[2]
    valor_total_2 = precio_2 * cantidad_2
    print(f"Valor total en stock 2: ${valor_total_2:.2f}")

    #STOCK 3
    print(f"Producto: {stock3[0]}")
    print(f"Precio: ${stock3[1]}")
    print(f"Cantidad en stock: {stock3[2]}")
    print(f"¿Disponible? {stock3[3]}")
    precio_3=stock3[1]
    cantidad_3=stock3[2]
    valor_total_3 = precio_3 * cantidad_3
    print(f"Valor total en stock 2: ${valor_total_3:.2f}")
    
def calculo_stock():
    #nombre_producto_1=stock_general()
    #cantidad_1=stock_general()
    #valor_total_1=stock_general()
    precio_1=stock1[1]
    precio_2 = stock2[1]
    #nombre_producto_2=stock_general()
    #cantidad_2=stock_general()
    #valor_total_2=stock_general()
    #precio_2=stock_general()
    print('SI NECESITA SABER EL PRECIO DE ALGUNOS PRODUCTOS EN STOCK 1: ')
    n1=int(input('INGRESE LA CANTIDAD A SOLICITAR n1= '))
    print(f"{stock1[0]}")
    valor_parcial_1=precio_1* n1
    print(f"Valor parcial de {stock1[0]} en stock 1: ${valor_parcial_1:.2f}")
    print('SI NECESITA SABER EL PRECIO DE ALGUNOS PRODUCTOS EN STOCK 2: ')
    n2=int(input('INGRESE LA CANTIDAD A SOLICITAR n2= '))
    valor_parcial_2=precio_2 * n2
    print(f"Valor parcial de {stock2[0]} en stock 2: ${valor_parcial_2:.2f}")

def ingresarStock():
     #STOCK 3
     # Vamos a ingresar un nuevo STOCK 3 y a solicitar cada uno de los datos al Usuario:
     print("Ingresa los datos correspondientes a tu producto")
     stock3[0]=input(' Ingresa el nombre de tu producto: ')
     stock3[1]=float(input('Ingresa el Precio de tu producto: '))
     stock3[2]=int(input('Ingresa el número de productos en stock: '))
     stock3[3]=bool(input('Ingresa disponibilidad: '))
     print(f"Producto: {stock3[0]}")
     print(f"Precio:${stock3[1]}")
     print(f"Cantidad en stock: {stock3[2]}")
     print(f"Disponible: {stock3[3]}")
     precio_3=stock3[1]
     cantidad_3=stock3[2]
     valor_total_3 = precio_3 * cantidad_3
     print(f"Valor total en stock 2: ${valor_total_3:.2f}")


# usuario y contraseña
# El usuario y la contraseña siempre van a ser admin / admin
user='admin'
password='admin'

while True:
    usuario=str(input('Ingresa tu Usuario: '))
    contrasena=str(input('Ingresa tu Contraseña: '))
    if (usuario==user and contrasena==password):
        #DEFINIMOS while como True  para que el sistema se funciones hasta que x sea diferente de 1 (x!=1)
        while True:  
            op=menu_principal()
            if(op==1):
                stock_general()                
            elif(op==2):
                calculo_stock()
            elif(op==3):
                ingresarStock()
            elif(op==4):
                print("SALIENDO DE PUNTO DE VENTA ... ")
                break
    else:
        print('Ingresa un usuario y contraseña valida')
        input('Enter para continuar')
