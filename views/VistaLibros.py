import tkinter as tk
from tkinter import ttk, messagebox

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def gestionLibros(root: tk.Tk, libros):
    ventanaLibros = tk.Toplevel(root)
    ventanaLibros.title("Gestión de Libros")
    ventanaLibros.geometry("600x500")
    
    ventanaLibros.rowconfigure(3, weight=1)
    ventanaLibros.columnconfigure(0, weight=1)

    style = ttk.Style(ventanaLibros)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#F0F0F0",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#F0F0F0")
    style.map("Treeview", background=[("selected", "#347083")])
    style.configure("Treeview.Heading",
                    font=("Helvetica", 12, "bold"),
                    background="#4CAF50",
                    foreground="white")

    # Título centrado
    etiquetaTitulo = ttk.Label(ventanaLibros, text="Biblioteca", font=("Helvetica", 16, "bold"))
    etiquetaTitulo.grid(row=0, column=0, pady=10, sticky="n")

    frame_form = ttk.Frame(ventanaLibros, padding=10)
    frame_form.grid(row=1, column=0, sticky="ew")
    frame_form.columnconfigure(1, weight=1)

    # ISBM
    labelIsbm = ttk.Label(frame_form, text="ISBM:")
    labelIsbm.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    isbmLibro = ttk.Entry(frame_form)
    isbmLibro.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    isbmLibro.bind("<Return>", focus_next_widget)

    # Nombre del Libro
    labelTituloLibro = ttk.Label(frame_form, text="Nombre del Libro:")
    labelTituloLibro.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    nombreLibro = ttk.Entry(frame_form)
    nombreLibro.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    nombreLibro.bind("<Return>", focus_next_widget)

    # Autor
    labelAutor = ttk.Label(frame_form, text="Autor:")
    labelAutor.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    autorLibro = ttk.Entry(frame_form)
    autorLibro.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    autorLibro.bind("<Return>", focus_next_widget)

    frame_buttons = ttk.Frame(ventanaLibros, padding=10)
    frame_buttons.grid(row=2, column=0, sticky="ew")
    frame_buttons.columnconfigure((0, 1, 2), weight=1)

    def agregarLibro():
        isbmInput = isbmLibro.get()
        nombreLibroInput = nombreLibro.get()
        autorLibroInput = autorLibro.get()
        if isbmInput != "" and nombreLibroInput != "" and autorLibroInput != "":
            detalle = libros.agregar_libro(nombreLibroInput, autorLibroInput, isbmInput)
            messagebox.showinfo("Información", detalle)
            isbmLibro.delete(0, tk.END)
            nombreLibro.delete(0, tk.END)
            autorLibro.delete(0, tk.END)
            listar()
        else:
            messagebox.showinfo("Error", "Los campos deben estar llenos")

    def buscarLibro():
        isbmInput = isbmLibro.get()
        nombreLibroInput = nombreLibro.get()
        autorLibroInput = autorLibro.get()
        ventanaLibrosBuscar = tk.Toplevel(root)
        ventanaLibrosBuscar.title("Buscar Libros")
        ventanaLibrosBuscar.geometry("400x400")
        
        tablaEncontrados = ttk.Treeview(ventanaLibrosBuscar, columns=("ISBM", "Nombre", "Autor"), show="headings")
        for col in ("ISBM", "Nombre", "Autor"):
            tablaEncontrados.heading(col, text=col)
            tablaEncontrados.column(col, minwidth=50, width=110, anchor="center")
        tablaEncontrados.pack(expand=True, fill="both", padx=10, pady=10)
        

        tablaEncontrados.tag_configure("even", background="#E8E8E8")
        tablaEncontrados.tag_configure("odd", background="#DFDFDF")
        
        encontrados = []
        if isbmInput != "":
            encontrados = libros.buscar_libro_isbm(isbmInput)
        elif nombreLibroInput != "":
            encontrados = libros.buscar_libro_titulo(nombreLibroInput)
        elif autorLibroInput != "":
            encontrados = libros.buscar_libro_autor(autorLibroInput)
        isbmLibro.delete(0, tk.END)
        nombreLibro.delete(0, tk.END)
        autorLibro.delete(0, tk.END)
        
        for i, row in enumerate(encontrados):
            tag = "even" if i % 2 == 0 else "odd"
            tablaEncontrados.insert("", "end", values=row, tags=(tag,))

    def eliminarLibro():
        isbmInput = isbmLibro.get()
        resultado = libros.eliminar_libro(isbmInput)
        messagebox.showinfo("Información", resultado)
        isbmLibro.delete(0, tk.END)
        listar()

    buttonAgregar = ttk.Button(frame_buttons, text="Agregar", command=agregarLibro)
    buttonAgregar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    buttonBuscar = ttk.Button(frame_buttons, text="Buscar", command=buscarLibro)
    buttonBuscar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    buttonEliminar = ttk.Button(frame_buttons, text="Eliminar", command=eliminarLibro)
    buttonEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    frame_table = ttk.Frame(ventanaLibros, padding=10)
    frame_table.grid(row=3, column=0, sticky="nsew")
    ventanaLibros.rowconfigure(3, weight=1)
    
    tree = ttk.Treeview(frame_table, columns=("ISBM", "Nombre", "Autor"), show="headings")
    for col in ("ISBM", "Nombre", "Autor"):
        tree.heading(col, text=col)
        tree.column(col, minwidth=50, width=110, anchor="center")
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    tree.tag_configure("even", background="#E8E8E8")
    tree.tag_configure("odd", background="#DFDFDF")
    
    def listar():
        for item in tree.get_children():
            tree.delete(item)
        for i, row in enumerate(libros.ver_libros()):
            tag = "even" if i % 2 == 0 else "odd"
            tree.insert("", "end", values=row, tags=(tag,))
    listar()


    ventanaLibros.update()
    ventanaLibros.minsize(600, 500)
