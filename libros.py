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

        if titulo !='' and autor !='' and isbm !='':
            cursor.execute("INSERT INTO libros(isbm,titulo,autor) VALUES(?,?,?)",(isbm,titulo,autor,))
            conn.commit()
            return f'Insert correctamente {isbm} ,{titulo}, {autor}'
        else:
            return 'ingrese todos los atributos'
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
            return f'Elimino correctamente {isbm}'
        else:
            return 'Ingrese el ISBM'
    except Exception as err:
        return str(err)
    finally:
        conn.close()

# FUNCION DE BUSCAR LIBRO POR TITULO
def buscar_libro(titulo):
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