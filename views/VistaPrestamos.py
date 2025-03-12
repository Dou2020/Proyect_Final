import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def gestionPrestamos(root: tk.Tk, prestamos):
    ventanaPrestamos = tk.Toplevel(root)
    ventanaPrestamos.title("Gestión de Prestamos")
    ventanaPrestamos.geometry("600x500")
    
    ventanaPrestamos.rowconfigure(3, weight=1)
    ventanaPrestamos.columnconfigure(0, weight=1)

    style = ttk.Style(ventanaPrestamos)
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

    etiquetaTitulo = ttk.Label(ventanaPrestamos, text="Prestamos", font=("Helvetica", 16, "bold"))
    etiquetaTitulo.grid(row=0, column=0, pady=10, sticky="n")

    frame_form = ttk.Frame(ventanaPrestamos, padding=10)
    frame_form.grid(row=1, column=0, sticky="ew")
    frame_form.columnconfigure(1, weight=1)

    # ISBM
    labelIsbm = ttk.Label(frame_form, text="ISBM del Libro:")
    labelIsbm.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    isbmLibro = ttk.Entry(frame_form)
    isbmLibro.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    isbmLibro.bind("<Return>", focus_next_widget)

    # ID USUARIO
    labelUsuario = ttk.Label(frame_form, text="Id del Usuario:")
    labelUsuario.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    idUsuario = ttk.Entry(frame_form)
    idUsuario.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    idUsuario.bind("<Return>", focus_next_widget)

    # Fecha de Prestamo
    labelFecha = ttk.Label(frame_form, text="Fecha de Devolucion:")
    labelFecha.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    fechaPrestamo = DateEntry(frame_form, date_pattern="dd-mm-yyyy")
    fechaPrestamo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    fechaPrestamo.bind("<Return>", focus_next_widget)

    frame_buttons = ttk.Frame(ventanaPrestamos, padding=10)
    frame_buttons.grid(row=2, column=0, sticky="ew")
    frame_buttons.columnconfigure((0, 1, 2), weight=1)

    def agregarPrestamo():
        isbmInput = isbmLibro.get()
        idUsuarioInput = idUsuario.get()
        fechaPrestamoInput = fechaPrestamo.get()
        if isbmInput != "" and idUsuarioInput != "" and fechaPrestamoInput != "":
            detalle = prestamos.prestar_libro(isbmInput, idUsuarioInput, fechaPrestamoInput)
            messagebox.showinfo("Información", detalle)
            isbmLibro.delete(0, tk.END)
            idUsuario.delete(0, tk.END)
            listar()
        else:
            messagebox.showinfo("Error", "Los campos deben estar llenos")

    def buscarPrestamo():
        isbmInput = isbmLibro.get()
        idUsuarioInput = idUsuario.get()
        ventanaPrestamosBuscar = tk.Toplevel(root)
        ventanaPrestamosBuscar.title("Buscar Prestamos")
        ventanaPrestamosBuscar.geometry("500x400")
        
        tablaEncontrados = ttk.Treeview(ventanaPrestamosBuscar, columns=("Libro", "Usuario","Fecha_Prestamo", "Devolucion", "Estado"), show="headings")
        for col in ("Libro", "Usuario","Fecha_Prestamo", "Devolucion", "Estado"):
            tablaEncontrados.heading(col, text=col)
            tablaEncontrados.column(col, minwidth=50, width=110, anchor="center")
        tablaEncontrados.pack(expand=True, fill="both", padx=10, pady=10)
        

        tablaEncontrados.tag_configure("even", background="#E8E8E8")
        tablaEncontrados.tag_configure("odd", background="#DFDFDF")
        
        encontrados = []
        if isbmInput != "":
            encontrados = prestamos.buscar_prestamo_libro(isbmInput)
        elif idUsuarioInput != "":
            encontrados = prestamos.buscar_prestamo_usuario(idUsuarioInput)
       
        isbmLibro.delete(0, tk.END)
        idUsuario.delete(0, tk.END)
        
        for i, row in enumerate(encontrados):
            tag = "even" if i % 2 == 0 else "odd"
            tablaEncontrados.insert("", "end", values=row, tags=(tag,))

    def devolverPrestamo():
        isbmInput = isbmLibro.get()
        idUsuarioInput = idUsuario.get()
        if isbmInput != "" and idUsuarioInput != "":
            detalle = prestamos.devolver_libro(isbmInput, idUsuarioInput)
            messagebox.showinfo("Información", detalle)
            isbmLibro.delete(0, tk.END)
            idUsuario.delete(0, tk.END)
            listar()
        else:
            messagebox.showinfo("Error", "Los campos deben estar llenos")


    buttonAgregar = ttk.Button(frame_buttons, text="Agregar Prestamo", command=agregarPrestamo)
    buttonAgregar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    buttonBuscar = ttk.Button(frame_buttons, text="Buscar Prestamo", command=buscarPrestamo)
    buttonBuscar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    buttonEliminar = ttk.Button(frame_buttons, text="Devolver Prestamo", command=devolverPrestamo)
    buttonEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    frame_table = ttk.Frame(ventanaPrestamos, padding=10)
    frame_table.grid(row=3, column=0, sticky="nsew")
    ventanaPrestamos.rowconfigure(3, weight=1)
    
    tree = ttk.Treeview(frame_table, columns=("Libro", "Usuario","Fecha_Prestamo", "Devolucion", "Estado"), show="headings")
    for col in ("Libro", "Usuario","Fecha_Prestamo", "Devolucion", "Estado"):
        tree.heading(col, text=col)
        tree.column(col, minwidth=50, width=110, anchor="center")
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    tree.tag_configure("even", background="#E8E8E8")
    tree.tag_configure("odd", background="#DFDFDF")
    
    def listar():
        for item in tree.get_children():
            tree.delete(item)
        for i, row in enumerate(prestamos.ver_prestamos()):
            tag = "even" if i % 2 == 0 else "odd"
            tree.insert("", "end", values=row, tags=(tag,))
    listar()


    ventanaPrestamos.update()
    ventanaPrestamos.minsize(600, 500)
