import tkinter as tk
from tkinter import ttk, messagebox

from tkcalendar import DateEntry

def focus_next_widget(event):
  event.widget.tk_focusNext().focus()
  return "Break"

def gestionLibros(root: tk.Tk, libros):
    ventanaLibros = tk.Toplevel(root)
    ventanaLibros.title("Ventana Gestion de Libros")
    ventanaLibros.geometry("600x500")

    etiquetaTitulo = tk.Label(ventanaLibros, text="Biblioteca", justify="center")
    etiquetaTitulo.grid(row=0, column=1 ,padx=10, pady=10)

    # ID LIBRO
    labelIsbm = tk.Label(ventanaLibros, text="ISBM")
    labelIsbm.grid(row=1, column=0, padx=10, pady=10)
    isbmLibro = tk.Entry(ventanaLibros)
    isbmLibro.grid(row=1, column=1, padx=10, pady=10)
    isbmLibro.bind("<Return>", focus_next_widget)

    # NOMBRE TITULO
    labelTitulo = tk.Label(ventanaLibros, text="Nombre del Libro")
    labelTitulo.grid(row=2, column=0, padx=10, pady=10)
    nombreLibro = tk.Entry(ventanaLibros)
    nombreLibro.grid(row=2, column=1, padx=10, pady=10)
    nombreLibro.bind("<Return>", focus_next_widget)

    # AUTOR
    labelAutor = tk.Label(ventanaLibros, text="Autor del Libro")
    labelAutor.grid(row=3, column=0, padx=10, pady=10)
    autorLibro = tk.Entry(ventanaLibros)
    autorLibro.grid(row=3, column=1, padx=10, pady=10)

    autorLibro.bind("<Return>", focus_next_widget)

    tree = ttk.Treeview(ventanaLibros, columns=("ISBM", "Nombre", "Autor"), show="headings")
    for col in ("ISBM", "Nombre", "Autor"):
        tree.heading(col, text=col)
        tree.column(col, minwidth=50, width=110, stretch=False)
    tree.grid(row=7,sticky="nsew")
    tree.grid(pady=10, padx=10)

    def listar():
        for item in tree.get_children():
            tree.delete(item)
        for row in libros.ver_libros():
            tree.insert("", "end", values=row)
    listar()
    def agregarLibro():
        isbmInput = isbmLibro.get()
        nombreLibroInput = nombreLibro.get()
        autorLibroInput = autorLibro.get()

        if isbmInput!="" and nombreLibroInput != "" and autorLibroInput != "":
            detalle = libros.agregar_libro(nombreLibroInput, autorLibroInput, isbmInput)
            messagebox.showinfo("Informacion",detalle)
            autorLibro.delete(0,tk.END)
            isbmLibro.delete(0,tk.END)
            nombreLibro.delete(0,tk.END)
            listar()
        else:
            messagebox.showinfo("Error", "Los campos deben de estar llenos")

    def buscarLibro():
        isbmInput = isbmLibro.get()
        nombreLibroInput = nombreLibro.get()
        autorLibroInput = autorLibro.get()
        ventanaLibrosBuscar = tk.Toplevel(root)
        ventanaLibrosBuscar.title("LibrosBuscar")
        ventanaLibrosBuscar.geometry("400x400")
        tablaEncontrados = ttk.Treeview(ventanaLibrosBuscar, columns=("ISBM", "Nombre", "Autor"), show="headings")
        encontrados = []
        if(isbmInput!= ""):
            encontrados = libros.buscar_libro_isbm(isbmInput)

        elif(nombreLibroInput!=""):
            encontrados = libros.buscar_libro_titulo(nombreLibroInput)

        elif(autorLibroInput!=""):
            encontrados = libros.buscar_libro_autor(autorLibroInput)

        autorLibro.delete(0, tk.END)
        isbmLibro.delete(0, tk.END)
        nombreLibro.delete(0, tk.END)
        for col in ("ISBM", "Nombre", "Autor"):
            tablaEncontrados.heading(col, text=col)
            tablaEncontrados.column(col, minwidth=50, width=110, stretch=False)
        tablaEncontrados.grid(row=6, column=0, sticky="nsew")
        tablaEncontrados.grid(pady=10, padx=10)
        for item in tablaEncontrados.get_children():
            tablaEncontrados.delete(item)
        for row in encontrados:
            tablaEncontrados.insert("", "end", values=row)
    def eliminarLibro():
        isbmInput = isbmLibro.get()
        resultado = libros.eliminar_libro(isbmInput)
        messagebox.showinfo("Informacion", resultado)
        isbmLibro.delete(0, tk.END)
        listar()



    buttonAgregar = tk.Button(ventanaLibros, text="Editar", command=agregarLibro)
    buttonAgregar.grid(row=4, column=0, columnspan=2, pady=10)
    buttonBuscar = tk.Button(ventanaLibros, text="Buscar", command=buscarLibro)
    buttonBuscar.grid(row=4, column=1, columnspan=2, pady=10)
    buttonEliminar = tk.Button(ventanaLibros, text="Eliminar", command=eliminarLibro)
    buttonEliminar.grid(row=4, column=2, columnspan=2, pady=10)




