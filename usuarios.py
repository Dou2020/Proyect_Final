import sqlite3

def create_table():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios(
                    id TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL
                )
            ''')
        conn.commit()
    except Exception as err:
        return err
    finally:
        conn.close()

def ver_usuarios():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        return cursor.fetchall()

    except Exception as err:
        return str(err)
    finally:
        conn.close()

def registrar_usuario(id, nombre, edad):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios(id,nombre,edad) VALUES(?,?,?)",(id,nombre,edad,))
        conn.commit()
        if cursor.rowcount == 1:
            return f'El usuario se ha registrado correctamente. Datos: {id}, {nombre}, {edad}'
        else:
            return f'El usuario {nombre}, id:{id} existe'
    except Exception as err:
        return str(err)
    finally:
        conn.close()

def eliminar_usuario(id):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if id == '':
            return 'Ingrese un ID'

        cursor.execute("DELETE FROM usuarios WHERE id = ?",(id,))
        conn.commit()
        if cursor.rowcount == 1:
            return f'Se la eliminado el usuario con el ID: {id}'
        else:
            return f'No se encontro el usuario con el  ID: {id}'

    except Exception as err:
        return str(err)
    finally:
        conn.close()

def buscar_usuario_id(id):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if id != '' :
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
            return cursor.fetchall()
        else:
            return 'Ingrese un id del usuario'
    except Exception as err:
        str(err)
    finally:
        conn.close()

def buscar_usuario_nombre(nombre):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if id != '' :
            cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
            return cursor.fetchall()
        else:
            return 'Ingrese el nombre del usuario'
    except Exception as err:
        str(err)
    finally:
        conn.close()