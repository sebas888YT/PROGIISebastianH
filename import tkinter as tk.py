import tkinter as tk
from tkinter import messagebox

def show_entry():
    """Mostrar el texto ingresado en el Entry."""
    text = entry.get()
    messagebox.showinfo("Texto ingresado", f"Texto ingresado: {text}")

def show_selection():
    """Mostrar la opción seleccionada en el Radiobutton."""
    selection = var.get()
    messagebox.showinfo("Opción seleccionada", f"Opción seleccionada: {selection}")

def show_checkbox():
    """Mostrar el estado del Checkbutton."""
    state = check_var.get()
    if state:
        messagebox.showinfo("Estado del Checkbutton", "Checkbutton marcado")
    else:
        messagebox.showinfo("Estado del Checkbutton", "Checkbutton desmarcado")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Widgets")

# Crear un Entry
entry_label = tk.Label(root, text="Ingrese un texto:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Crear un botón para mostrar el texto ingresado
entry_button = tk.Button(root, text="Mostrar Entry", command=show_entry)
entry_button.pack()

# Crear un Radiobutton
var = tk.StringVar()
radio_label = tk.Label(root, text="Seleccione una opción:")
radio_label.pack()
radio1 = tk.Radiobutton(root, text="Opción 1", variable=var, value="Opción 1")
radio1.pack()
radio2 = tk.Radiobutton(root, text="Opción 2", variable=var, value="Opción 2")
radio2.pack()

# Crear un botón para mostrar la opción seleccionada
radio_button = tk.Button(root, text="Mostrar Radiobutton", command=show_selection)
radio_button.pack()

# Crear un Checkbutton
check_var = tk.BooleanVar()
check_button = tk.Checkbutton(root, text="Marcar/Desmarcar", variable=check_var)
check_button.pack()

# Crear un botón para mostrar el estado del Checkbutton
check_button = tk.Button(root, text="Mostrar Checkbutton", command=show_checkbox)
check_button.pack()

# Ejecutar el bucle principal
root.mainloop()
