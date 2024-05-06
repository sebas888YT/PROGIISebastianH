import tkinter as tk

def ingresar():
    pass

ventana = tk.Tk()
ventana.title("Inicio de Sesión")

frame_izquierda = tk.Frame(ventana, bg="white", width=200, height=400)
frame_derecha = tk.Frame(ventana, bg="lightgrey", width=400, height=400)

frame_izquierda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame_derecha.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

logo = tk.PhotoImage(file="lobo_logo.png")  
logo_label = tk.Label(frame_izquierda, image=logo)
logo_label.pack(pady=10)

tk.Label(frame_derecha, text="Inicio de Sesión", font=("Arial", 16)).pack(pady=20)
tk.Label(frame_derecha, text="Usuario:").pack()
usuario_entry = tk.Entry(frame_derecha)
usuario_entry.pack(pady=5)
tk.Label(frame_derecha, text="Contraseña:").pack()
clave_entry = tk.Entry(frame_derecha, show="*")
clave_entry.pack(pady=5)
ingresar_button = tk.Button(frame_derecha, text="Ingresar", command=ingresar)
ingresar_button.pack(pady=20)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(0, weight=1)

ventana.mainloop()
