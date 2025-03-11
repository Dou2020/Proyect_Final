import tkinter as tk
from tkinter import ttk, messagebox

from tkcalendar import DateEntry


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "Break"


def gestionUsuarios(root: tk.Tk, usuarios):
    ventanaUsuarios = tk.Toplevel(root)
    ventanaUsuarios.title("Ventana Gestion de Usuarios")
    ventanaUsuarios.geometry("600x500")

    etiquetaTitulo = tk.Label(ventanaUsuarios, text="Usuarios", justify="center")
    etiquetaTitulo.grid(row=0, column=1, padx=10, pady=10)

    # ID USUARIO
    etiquetaID = tk.Label(ventanaUsuarios, text="ID Usuario")
    etiquetaID.grid(row=1, column=0, padx=10, pady=10)
    idUsuario = tk.Entry(ventanaUsuarios)
    idUsuario.grid(row=1, column=1, padx=10, pady=10)
    idUsuario.bind("<Return>", focus_next_widget)

    # NOMBRE USUARIO
    labelNombre = tk.Label(ventanaUsuarios, text="Nombre del Usuario")
    labelNombre.grid(row=2, column=0, padx=10, pady=10)
    nombreUsuario = tk.Entry(ventanaUsuarios)
    nombreUsuario.grid(row=2, column=1, padx=10, pady=10)
    nombreUsuario.bind("<Return>", focus_next_widget)

    # EDAD USUARIO
    labelEdad = tk.Label(ventanaUsuarios, text="Edad del Usuario")
    labelEdad.grid(row=3, column=0, padx=10, pady=10)
    edadUsuario = tk.Entry(ventanaUsuarios)
    edadUsuario.grid(row=3, column=1, padx=10, pady=10)
    edadUsuario.bind("<Return>", focus_next_widget)

    tree = ttk.Treeview(ventanaUsuarios, columns=("ID_Usuario", "Nombre", "Edad"), show="headings")
    for col in ("ID_Usuario", "Nombre", "Edad"):
        tree.heading(col, text=col)
        tree.column(col, minwidth=50, width=110, stretch=False)
    tree.grid(row=7, sticky="nsew")
    tree.grid(pady=10, padx=10)

    def listar():
        for item in tree.get_children():
            tree.delete(item)
        for row in usuarios.ver_usuarios():
            tree.insert("", "end", values=row)

    listar()

    def agregarUsuario():
        idUsuarioInput = idUsuario.get()
        nombreUsuarioInput = nombreUsuario.get()
        edadUsuarioInput = edadUsuario.get()

        if idUsuarioInput != "" and nombreUsuarioInput != "" and edadUsuarioInput != "":
            resultado = usuarios.registrar_usuario(idUsuarioInput, nombreUsuarioInput, edadUsuarioInput)
            messagebox.showinfo("Informacion", resultado)
            idUsuario.delete(0, tk.END)
            nombreUsuario.delete(0, tk.END)
            edadUsuario.delete(0, tk.END)
            listar()
        else:
            messagebox.showinfo("Error", "Los campos deben de estar llenos")

    def buscarUsuario():
        idUsuarioInput = idUsuario.get()
        nombreUsuarioInput = nombreUsuario.get()
        ventanaBuscarUsuarios = tk.Toplevel(root)
        ventanaBuscarUsuarios.title("Buscar Usuarios")
        ventanaBuscarUsuarios.geometry("400x400")
        tablaEncontrados = ttk.Treeview(ventanaBuscarUsuarios, columns=("ID_Usuario", "Nombre", "Edad"), show="headings")
        encontrados = []
        if (idUsuarioInput != ""):
            encontrados = usuarios.buscar_usuario_id(idUsuarioInput)

        elif (nombreUsuarioInput != ""):
            encontrados = usuarios.buscar_usuario_nombre(nombreUsuarioInput)

        idUsuarioInput.delete(0, tk.END)
        nombreUsuarioInput.delete(0, tk.END)
        edadUsuario.delete(0, tk.END)
        for col in ("ID_Usuario", "Nombre", "Edad"):
            tablaEncontrados.heading(col, text=col)
            tablaEncontrados.column(col, minwidth=50, width=110, stretch=False)
        tablaEncontrados.grid(row=6, column=0, sticky="nsew")
        tablaEncontrados.grid(pady=10, padx=10)
        for item in tablaEncontrados.get_children():
            tablaEncontrados.delete(item)
        for row in encontrados:
            tablaEncontrados.insert("", "end", values=row)

    def eliminarUsuario():
        idUsuarioInput = idUsuario.get()
        resultado = usuarios.eliminar_usuario(idUsuarioInput)
        messagebox.showinfo("Informacion", resultado)
        idUsuario.delete(0, tk.END)
        listar()

    buttonAgregar = tk.Button(ventanaUsuarios, text="Editar", command=agregarUsuario)
    buttonAgregar.grid(row=4, column=0, columnspan=2, pady=10)
    buttonBuscar = tk.Button(ventanaUsuarios, text="Buscar", command=buscarUsuario)
    buttonBuscar.grid(row=4, column=1, columnspan=2, pady=10)
    buttonEliminar = tk.Button(ventanaUsuarios, text="Eliminar", command=eliminarUsuario)
    buttonEliminar.grid(row=4, column=2, columnspan=2, pady=10)
