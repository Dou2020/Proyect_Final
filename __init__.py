import tkinter as tk
from views import VistaLibros
from views import VistaUsuarios

import libros
libros.create_table()

# Pruebas de funcionalidades
#print(libros.agregar_libro('code1','anonimo','code1'))
#print(libros.agregar_libro('code2','anonimo','code2'))
#print(libros.agregar_libro('code3','anonimo','code3'))
#print(libros.ver_libros())
#print(libros.eliminar_libro('code3'))
#print(libros.buscar_libro_titulo('code2'))
#print(libros.buscar_libro_isbm('code2'))
#print(libros.buscar_libro_autor('anonimo'))

import usuarios
usuarios.create_table()

# Pruebas de Funcionalidades
#print(usuarios.registrar_usuario('user1','Dou',22))
#print(usuarios.registrar_usuario('user2','Eduar',12))
#print(usuarios.registrar_usuario('user3','Eduar',12))
#print(usuarios.ver_usuarios())
#print(usuarios.eliminar_usuario('user3'))

import prestamos
prestamos.createTable()
#print(prestamos.prestar_libro('code1','user1'))
#print(prestamos.devolver_libro('code1','user1'))
#print(prestamos.prestar_libro('code2','user2'))
#print(prestamos.devolver_libro('code2','user2'))

import morosidad
morosidad.create_table()


import utilidades

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