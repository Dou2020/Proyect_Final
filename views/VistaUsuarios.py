import tkinter as tk
from tkinter import ttk, messagebox

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def gestionUsuarios(root: tk.Tk, usuarios):
    ventanaUsuarios = tk.Toplevel(root)
    ventanaUsuarios.title("Ventana Gestión de Usuarios")
    ventanaUsuarios.geometry("600x500")
    ventanaUsuarios.configure(bg="#f7f7f7")
    
    # Configurar la rejilla principal para que la tabla se expanda
    ventanaUsuarios.rowconfigure(3, weight=1)
    ventanaUsuarios.columnconfigure(0, weight=1)
    
    style = ttk.Style(ventanaUsuarios)
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
    style.configure("TButton",
                    font=("Helvetica", 10, "bold"),
                    padding=5)
    
    # Título
    etiquetaTitulo = ttk.Label(ventanaUsuarios, text="Usuarios", font=("Helvetica", 16, "bold"), background="#f7f7f7")
    etiquetaTitulo.grid(row=0, column=0, pady=10, sticky="n")
    
    frame_form = ttk.Frame(ventanaUsuarios, padding=10)
    frame_form.grid(row=1, column=0, sticky="ew")
    frame_form.columnconfigure(1, weight=1)
    
    etiquetaID = ttk.Label(frame_form, text="ID Usuario:")
    etiquetaID.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    idUsuario = ttk.Entry(frame_form)
    idUsuario.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    idUsuario.bind("<Return>", focus_next_widget)
    
    labelNombre = ttk.Label(frame_form, text="Nombre del Usuario:")
    labelNombre.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    nombreUsuario = ttk.Entry(frame_form)
    nombreUsuario.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    nombreUsuario.bind("<Return>", focus_next_widget)
    
    labelEdad = ttk.Label(frame_form, text="Edad del Usuario:")
    labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    edadUsuario = ttk.Entry(frame_form)
    edadUsuario.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    edadUsuario.bind("<Return>", focus_next_widget)
    
    frame_buttons = ttk.Frame(ventanaUsuarios, padding=10)
    frame_buttons.grid(row=2, column=0, sticky="ew")
    frame_buttons.columnconfigure((0, 1, 2), weight=1)
    
    def agregarUsuario():
        idUsuarioInput = idUsuario.get()
        nombreUsuarioInput = nombreUsuario.get()
        edadUsuarioInput = edadUsuario.get()
        if idUsuarioInput != "" and nombreUsuarioInput != "" and edadUsuarioInput != "":
            resultado = usuarios.registrar_usuario(idUsuarioInput, nombreUsuarioInput, edadUsuarioInput)
            messagebox.showinfo("Información", resultado)
            idUsuario.delete(0, tk.END)
            nombreUsuario.delete(0, tk.END)
            edadUsuario.delete(0, tk.END)
            listar()
        else:
            messagebox.showinfo("Error", "Los campos deben estar llenos")
    
    def buscarUsuario():
        idUsuarioInput = idUsuario.get()
        nombreUsuarioInput = nombreUsuario.get()
        ventanaBuscarUsuarios = tk.Toplevel(root)
        ventanaBuscarUsuarios.title("Buscar Usuarios")
        ventanaBuscarUsuarios.geometry("400x400")
        
        tablaEncontrados = ttk.Treeview(ventanaBuscarUsuarios, columns=("ID_Usuario", "Nombre", "Edad"), show="headings")
        for col in ("ID_Usuario", "Nombre", "Edad"):
            tablaEncontrados.heading(col, text=col)
            tablaEncontrados.column(col, minwidth=50, width=110, anchor="center")
        tablaEncontrados.pack(expand=True, fill="both", padx=10, pady=10)
        
        encontrados = []
        if idUsuarioInput != "":
            encontrados = usuarios.buscar_usuario_id(idUsuarioInput)
        elif nombreUsuarioInput != "":
            encontrados = usuarios.buscar_usuario_nombre(nombreUsuarioInput)
        
        idUsuario.delete(0, tk.END)
        nombreUsuario.delete(0, tk.END)
        edadUsuario.delete(0, tk.END)
        
        tablaEncontrados.tag_configure("even", background="#E8E8E8")
        tablaEncontrados.tag_configure("odd", background="#DFDFDF")
        for i, row in enumerate(encontrados):
            tag = "even" if i % 2 == 0 else "odd"
            tablaEncontrados.insert("", "end", values=row, tags=(tag,))
    
    def eliminarUsuario():
        idUsuarioInput = idUsuario.get()
        resultado = usuarios.eliminar_usuario(idUsuarioInput)
        messagebox.showinfo("Información", resultado)
        idUsuario.delete(0, tk.END)
        listar()
    
    buttonAgregar = ttk.Button(frame_buttons, text="Agregar", command=agregarUsuario)
    buttonAgregar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    buttonBuscar = ttk.Button(frame_buttons, text="Buscar", command=buscarUsuario)
    buttonBuscar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    buttonEliminar = ttk.Button(frame_buttons, text="Eliminar", command=eliminarUsuario)
    buttonEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
    
    frame_table = ttk.Frame(ventanaUsuarios, padding=10)
    frame_table.grid(row=3, column=0, sticky="nsew")
    ventanaUsuarios.rowconfigure(3, weight=1)
    
    tree = ttk.Treeview(frame_table, columns=("ID_Usuario", "Nombre", "Edad"), show="headings")
    for col in ("ID_Usuario", "Nombre", "Edad"):
        tree.heading(col, text=col)
        tree.column(col, minwidth=50, width=110, anchor="center")
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    tree.tag_configure("even", background="#E8E8E8")
    tree.tag_configure("odd", background="#DFDFDF")
    
    def listar():
        for item in tree.get_children():
            tree.delete(item)
        for i, row in enumerate(usuarios.ver_usuarios()):
            tag = "even" if i % 2 == 0 else "odd"
            tree.insert("", "end", values=row, tags=(tag,))
    listar()
    
    ventanaUsuarios.update()
    ventanaUsuarios.minsize(600, 500)
