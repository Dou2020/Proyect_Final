import tkinter as tk
from views import VistaLibros
from views import VistaUsuarios
from views import VistaPrestamos
from views import VistaMorosidad
import libros
import usuarios
import prestamos
import morosidad
import utilidades

root = tk.Tk()

root.title("Sistema de Gestión de Biblioteca")
root.geometry("700x500")
def gestionDeLibros():
    VistaLibros.gestionLibros(root, libros)

def gestionDeUsuarios():
    VistaUsuarios.gestionUsuarios(root, usuarios)

def gestionDePrestamos():
    VistaPrestamos.gestionPrestamos(root, prestamos)

def gestionMorosidad():
    VistaMorosidad.gestionMorosidad(root, morosidad, prestamos)

frame = tk.Frame(root, bg="#E8EAF6")  # Mismo color de fondo
frame.pack(expand=True)

# Estilo de botones
boton_style = {
    "width": 20,
    "height": 2,
    "font": ("Arial", 12, "bold"),
    "fg": "white",
    "bd": 3,  # Borde más grueso
    "relief": "raised"  # Efecto tridimensional
}

def on_enter(event, boton, color):
    boton.config(bg=color)

def on_leave(event, boton, color):
    boton.config(bg=color)

boton_libros = tk.Button(frame, text="📚 Gestión de Libros", bg="#3498db", **boton_style, command=gestionDeLibros)
boton_libros.grid(row=0, column=0, padx=20, pady=20)
boton_libros.bind("<Enter>", lambda e: on_enter(e, boton_libros, "#2980b9"))
boton_libros.bind("<Leave>", lambda e: on_leave(e, boton_libros, "#3498db"))

boton_usuarios = tk.Button(frame, text="👥 Gestión de Usuarios", bg="#2ecc71", **boton_style, command=gestionDeUsuarios)
boton_usuarios.grid(row=0, column=1, padx=20, pady=20)
boton_usuarios.bind("<Enter>", lambda e: on_enter(e, boton_usuarios, "#27ae60"))
boton_usuarios.bind("<Leave>", lambda e: on_leave(e, boton_usuarios, "#2ecc71"))

boton_prestamos = tk.Button(frame, text="📖 Gestión de Préstamos", bg="#f39c12", **boton_style, command=gestionDePrestamos)
boton_prestamos.grid(row=1, column=0, padx=20, pady=20)
boton_prestamos.bind("<Enter>", lambda e: on_enter(e, boton_prestamos, "#e67e22"))
boton_prestamos.bind("<Leave>", lambda e: on_leave(e, boton_prestamos, "#f39c12"))

boton_morosidad = tk.Button(frame, text="⚠️ Gestión de Morosidad", bg="#e74c3c", **boton_style, command=gestionMorosidad)
boton_morosidad.grid(row=1, column=1, padx=20, pady=20)
boton_morosidad.bind("<Enter>", lambda e: on_enter(e, boton_morosidad, "#c0392b"))
boton_morosidad.bind("<Leave>", lambda e: on_leave(e, boton_morosidad, "#e74c3c"))

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_gestion = tk.Menu(menu_bar, tearoff=0)
menu_gestion.add_command(label="Libros", command=gestionDeLibros)
menu_gestion.add_command(label="Usuarios", command=gestionDeUsuarios)
menu_gestion.add_command(label="Prestamos", command=gestionDePrestamos)
menu_gestion.add_command(label="Morosidad", command=gestionMorosidad)
menu_bar.add_cascade(label="Gestión", menu=menu_gestion)

root.mainloop()