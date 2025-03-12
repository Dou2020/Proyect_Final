import tkinter as tk
from views import VistaLibros
from views import VistaUsuarios
from views import VistaPrestamos
import libros
import usuarios
import prestamos
#import utilidades

root = tk.Tk()

root.title("Sistema de Gestión de Biblioteca")
root.geometry("700x500")
def gestionDeLibros():
    VistaLibros.gestionLibros(root, libros)

def gestionDeUsuarios():
    VistaUsuarios.gestionUsuarios(root, usuarios)

def gestionDePrestamos():
    VistaPrestamos.gestionPrestamos(root, prestamos)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_gestion = tk.Menu(menu_bar, tearoff=0)
menu_gestion.add_command(label="Libros", command=gestionDeLibros)
menu_gestion.add_command(label="Usuarios", command=gestionDeUsuarios)
menu_gestion.add_command(label="Prestamos", command=gestionDePrestamos)
menu_bar.add_cascade(label="Gestión", menu=menu_gestion)


root.mainloop()