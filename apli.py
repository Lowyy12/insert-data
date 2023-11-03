import tkinter as tk
from tkinter import ttk

def guardar_valores():
    id_texto = id_entrada.get()
    nombre = nombre_entrada.get()
    valor = valor_entrada.get()
    
    # Verifica si el ID es numérico
    if not id_texto.isdigit():
        mensaje.config(text="El valor del ID debe ser numérico.")
    else:
        id = int(id_texto)
        # Verifica si el ID ya existe en el archivo
        if not verificar_id_existente(id):
            with open("datos.csv", "a") as archivo:
                archivo.write(f"ID, {id}, Nombre, {nombre}, Producto, {valor}\n")
            
            nombre_entrada.delete(0, tk.END)
            valor_entrada.delete(0, tk.END)
            id_entrada.delete(0, tk.END)
            mensaje.config(text="Valores guardados con éxito.")
        else:
            mensaje.config(text=f"El ID {id} ya existe en el archivo.")

def verificar_id_existente(id):
    try:
        with open("datos.csv", "r") as archivo:
            contenido = archivo.read()
            return f"ID, {id}," in contenido
    except FileNotFoundError:
        return False

ventana = tk.Tk()
ventana.title("Campos de Entrada")

# Estilo
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#4CAF50")

# Alinear a la izquierda
ventana.geometry("400x250")
ventana.grid_columnconfigure(0, weight=1)

etiqueta_id = tk.Label(ventana, text="Ingresa un ID único:", anchor="w", padx=10)
etiqueta_id.grid(row=0, column=0, sticky="w")

id_entrada = tk.Entry(ventana, width=30)
id_entrada.grid(row=0, column=1, sticky="w")

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:", anchor="w", padx=10)
etiqueta_nombre.grid(row=1, column=0, sticky="w")

nombre_entrada = tk.Entry(ventana, width=30)
nombre_entrada.grid(row=1, column=1, sticky="w")

etiqueta_valor = tk.Label(ventana, text="Ingresa un producto:", anchor="w", padx=10)
etiqueta_valor.grid(row=2, column=0, sticky="w")

valor_entrada = tk.Entry(ventana, width=30)
valor_entrada.grid(row=2, column=1, sticky="w")

boton = ttk.Button(ventana, text="Guardar valores", command=guardar_valores)
boton.grid(row=3, column=0, columnspan=2, pady=10, sticky="w")

mensaje = tk.Label(ventana, text="", anchor="w", padx=10, fg="red")
mensaje.grid(row=4, column=0, columnspan=2, sticky="w")

ventana.mainloop()
