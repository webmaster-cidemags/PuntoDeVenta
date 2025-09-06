import tkinter as tk
from tkinter import messagebox

#Añadir datos
# Datos iniciales
stock1 = ["Truza", 0.99, 5000, True]
stock2 = ["Sudadera", 199.90, 500, False]
stock3 = ["producto", 00.00, 000, False]

def login():
    if usuario_entry.get() == "admin" and contra_entry.get() == "admin":
        login_frame.pack_forget()
        menu_frame.pack()
    else:
        messagebox.showerror("Error", "Usuario/contraseña incorrectos")

def mostrar_stock():
    stock_text = ""
    for i, stock in enumerate([stock1, stock2, stock3], 1):
        valor_total = stock[1] * stock[2]
        stock_text += f"PRODUCTO {i}:\n"
        stock_text += f"Nombre: {stock[0]}\n"
        stock_text += f"Precio: ${stock[1]:.2f}\n"
        stock_text += f"Cantidad: {stock[2]}\n"
        stock_text += f"Disponible: {'Sí' if stock[3] else 'No'}\n"
        stock_text += f"Valor total: ${valor_total:.2f}\n\n"

    messagebox.showinfo("Stock General", stock_text)

def calcular_precio():
    try:
        n1 = int(cant1_entry.get()) if cant1_entry.get() else 0
        n2 = int(cant2_entry.get()) if cant2_entry.get() else 0
        total1 = stock1[1] * n1
        total2 = stock2[1] * n2
        total_general = total1 + total2
        resultado = f"{stock1[0]} ({n1} und): ${total1:.2f}\n"
        resultado += f"{stock2[0]} ({n2} und): ${total2:.2f}\n"
        resultado += f"TOTAL: ${total_general:.2f}"
        messagebox.showinfo("Resultado", resultado)
    except:
        messagebox.showerror("Error", "Ingrese números válidos")

def ingresar_producto():
    stock3[0] = nombre_entry.get()
    stock3[1] = float(precio_entry.get())
    stock3[2] = int(cantidad_entry.get())
    stock3[3] = disponible_var.get()
    messagebox.showinfo("Éxito", "Producto actualizado correctamente")

def salir():
    if messagebox.askyesno("Salir", "¿Seguro que quieres salir?"):
        root.quit()

# Ventana principal
root = tk.Tk()
root.title("Sistema de Stock")
root.geometry("400x500")

# Frame de login
login_frame = tk.Frame(root)
login_frame.pack(pady=50)

tk.Label(login_frame, text="Usuario:").pack()
usuario_entry = tk.Entry(login_frame)
usuario_entry.pack(pady=5)

tk.Label(login_frame, text="Contraseña:").pack()
contra_entry = tk.Entry(login_frame, show="*")
contra_entry.pack(pady=5)

tk.Button(login_frame, text="Ingresar", command=login).pack(pady=10)

# Frame del menú principal (oculto al inicio)
menu_frame = tk.Frame(root)

tk.Label(menu_frame, text="SISTEMA DE STOCK", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(menu_frame, text="1. Revisar Stock", command=mostrar_stock, width=20).pack(pady=5)
tk.Button(menu_frame, text="2. Calcular Precios", command=calcular_precio, width=20).pack(pady=5)
tk.Button(menu_frame, text="3. Ingresar Producto", command=ingresar_producto, width=20).pack(pady=5)
tk.Button(menu_frame, text="4. Salir", command=salir, width=20).pack(pady=5)

# Frame para cálculo de precios
calc_frame = tk.Frame(menu_frame)
tk.Label(calc_frame, text="Cantidad Truzas:").pack()
cant1_entry = tk.Entry(calc_frame)
cant1_entry.pack()
tk.Label(calc_frame, text="Cantidad Sudaderas:").pack()
cant2_entry = tk.Entry(calc_frame)
cant2_entry.pack()

# Frame para ingresar productos
ingreso_frame = tk.Frame(menu_frame)
tk.Label(ingreso_frame, text="Nombre:").pack()
nombre_entry = tk.Entry(ingreso_frame)
nombre_entry.pack()
tk.Label(ingreso_frame, text="Precio:").pack()
precio_entry = tk.Entry(ingreso_frame)
precio_entry.pack()
tk.Label(ingreso_frame, text="Cantidad:").pack()
cantidad_entry = tk.Entry(ingreso_frame)
cantidad_entry.pack()

tk.Label(ingreso_frame, text="Disponible:").pack()
disponible_var = tk.BooleanVar()
tk.Checkbutton(ingreso_frame, variable=disponible_var).pack()

root.mainloop()
