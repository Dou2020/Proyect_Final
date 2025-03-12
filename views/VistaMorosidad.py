import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def gestionMorosidad(root: tk.Tk, morosidad, prestamos):
    ventanaMorosidad = tk.Toplevel(root)
    ventanaMorosidad.title("Gestión de Morosidad")
    ventanaMorosidad.geometry("600x500")
    
    ventanaMorosidad.rowconfigure(3, weight=1)
    ventanaMorosidad.columnconfigure(0, weight=1)

    style = ttk.Style(ventanaMorosidad)
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

    etiquetaTitulo = ttk.Label(ventanaMorosidad, text="Morosidad", font=("Helvetica", 16, "bold"))
    etiquetaTitulo.grid(row=0, column=0, pady=10, sticky="n")

    frame_form = ttk.Frame(ventanaMorosidad, padding=10)
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

    frame_buttons = ttk.Frame(ventanaMorosidad, padding=10)
    frame_buttons.grid(row=2, column=0, sticky="ew")
    frame_buttons.columnconfigure((0, 1, 2), weight=1)

    def devolverPrestamo():
        isbmInput = isbmLibro.get()
        idUsuarioInput = idUsuario.get()
        if isbmInput != "" and idUsuarioInput != "":
            detalle = prestamos.devolver_libro(isbmInput, idUsuarioInput)
            morosidad.agregar_morosidad(isbmInput, idUsuarioInput)
            messagebox.showinfo("Información", detalle)
            isbmLibro.delete(0, tk.END)
            idUsuario.delete(0, tk.END)
            listar()
        else:
            messagebox.showinfo("Error", "Los campos deben estar llenos")
    def verMorosidad():
        ventanaVerMorosidad = tk.Toplevel(root)
        ventanaVerMorosidad.title("Registro Morosidad")
        ventanaVerMorosidad.geometry("500x400")
        
        tablaEncontrados = ttk.Treeview(ventanaVerMorosidad, columns=("Libro", "Usuario","Fecha_Prestamo", "Devolucion", "Entrega"), show="headings")
        for col in ("Libro", "Usuario","Fecha_Prestamo", "Devolucion", "Entrega"):
            tablaEncontrados.heading(col, text=col)
            tablaEncontrados.column(col, minwidth=50, width=110, anchor="center")
        tablaEncontrados.pack(expand=True, fill="both", padx=10, pady=10)
        

        tablaEncontrados.tag_configure("even", background="#E8E8E8")
        tablaEncontrados.tag_configure("odd", background="#DFDFDF")
        encontrados=morosidad.ver_todas_morosidades()
       
        for i, row in enumerate(encontrados):
            tag = "even" if i % 2 == 0 else "odd"
            tablaEncontrados.insert("", "end", values=row, tags=(tag,))



    buttonVer = ttk.Button(frame_buttons, text="Registro de Morosidad", command=verMorosidad)
    buttonVer.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    buttonEliminar = ttk.Button(frame_buttons, text="Devolver Prestamo", command=devolverPrestamo)
    buttonEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    frame_table = ttk.Frame(ventanaMorosidad, padding=10)
    frame_table.grid(row=3, column=0, sticky="nsew")
    ventanaMorosidad.rowconfigure(3, weight=1)
    
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
        for i, row in enumerate(morosidad.ver_morosidad_prestamos()):
            tag = "even" if i % 2 == 0 else "odd"
            tree.insert("", "end", values=row, tags=(tag,))
    listar()


    ventanaMorosidad.update()
    ventanaMorosidad.minsize(600, 500)
