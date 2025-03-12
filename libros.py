import sqlite3

def create_table():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros(
                    isbm TEXT PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL
                )
        ''')
        conn.commit()
    except Exception as err:
        return str(err)
    finally:
        conn.close()

def ver_libros():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM libros")
        return cursor.fetchall()

    except Exception as err:
        return str(err)
    finally:
        conn.close()

# FUNCION AGREGAR LIBRO
def agregar_libro(titulo, autor,isbm):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        if titulo =='' and autor =='' and isbm =='':
            return 'ingrese todos los atributos'
        if len( buscar_libro_isbm(isbm) ) == 0:
            cursor.execute("INSERT INTO libros(isbm,titulo,autor) VALUES(?,?,?)",(isbm,titulo,autor,))
            conn.commit()
            return f'Libro agregado correctamente  {isbm} ,{titulo}, {autor}'
        else:
            return f'Ya existe el Libro con isbm: {isbm}'

    except Exception as err:
        return str(err)
    finally:
        conn.close()

# FUNCION ELIMINAR LIBRO
def eliminar_libro(isbm):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if isbm !='' :
            cursor.execute("DELETE FROM libros WHERE isbm = ?", (isbm,))
            conn.commit()
            if cursor.rowcount == 1:
                return f'Libro Eliminado correctamente ISBM: {isbm}'
            else:
                return f'No se encontro el Libro a eliminar ISBM: {isbm} '
        else:
            return 'Ingrese el ISBM'
    except Exception as err:
        return str(err)
    finally:
        conn.close()

# FUNCION DE BUSCAR LIBRO POR TITULO
def buscar_libro_titulo(titulo):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if titulo !='' :
            cursor.execute("SELECT * FROM libros WHERE titulo = ?", (titulo,))
            return cursor.fetchall()
        else:
            return 'Ingrese un titulo'
    except Exception as err:
        str(err)
    finally:
        conn.close()

# FUNCION DE BUSCAR LIBRO POR AUTOR
def buscar_libro_autor(autor):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if autor !='' :
            cursor.execute("SELECT * FROM libros WHERE autor = ?", (autor,))
            return cursor.fetchall()
        else:
            return 'Ingrese un autor'
    except Exception as err:
        str(err)
    finally:
        conn.close()

# FUNCION DE BUSCAR LIBRO POR ISBM
def buscar_libro_isbm(isbm):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if isbm !='' :
            cursor.execute("SELECT * FROM libros WHERE isbm = ?", (isbm,))
            return cursor.fetchall()
        else:
            return 'Ingrese el ISBM'
    except Exception as err:
        return str(err)
    finally:
        conn.close()
