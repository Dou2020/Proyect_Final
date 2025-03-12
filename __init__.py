
import tkinter as tk
from views import VistaLibros
from Proyect_Final.views import VistaUsuarios
import libros
import usuarios

#import utilidades

root = tk.Tk()

root.title("Sistema de Gestión de Biblioteca")
root.geometry("700x500")
def gestionDeLibros():
    VistaLibros.gestionLibros(root, libros)

def gestionDeUsuarios():
    VistaUsuarios.gestionUsuarios(root, usuarios)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_gestion = tk.Menu(menu_bar, tearoff=0)
menu_gestion.add_command(label="Libros", command=gestionDeLibros)
menu_gestion.add_command(label="Usuarios", command=gestionDeUsuarios)
#menu_gestion.add_command(label="Citas", command=gestionDeCitas)
menu_bar.add_cascade(label="Gestión", menu=menu_gestion)


root.mainloop()