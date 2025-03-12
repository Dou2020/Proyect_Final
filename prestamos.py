import sqlite3
from datetime import date

def createTable():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS prestamos(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    libros_isbm TEXT NOT NULL,
                    id_usuario TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    dia DATE NOT NULL,
                    FOREIGN KEY(libros_isbm) REFERENCES libros(isbm)
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
                )
            ''')
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()

def prestar_libro(isbm,id_usuario):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        if isbm == '' and id_usuario == '':
            return 'Ingrese todos los atributos'

        if is_libro_prestar(isbm):
            cursor.execute("INSERT INTO prestamos(libros_isbm, id_usuario, tipo,dia) VALUES(?,?,?,?)",(isbm,id_usuario,'PRESTAR',date.today()))
            conn.commit()
            return f'Insert Prestar: {isbm} ,{id_usuario}'
        else:
            return f'El libro isbm:{isbm} ya esta prestado por id:{id_usuario}'

    except Exception as err:
        return str(err)
    finally:
        conn.close()

def buscar_prestar_isbm(isbm):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if isbm !='' :
            cursor.execute("SELECT * FROM prestamos WHERE libros_isbm = ?", (isbm,))
            return cursor.fetchall()
        else:
            return 'Ingrese el ISBM'
    except Exception as err:
        return str(err)
    finally:
        conn.close()

def buscar_prestar_usuario(usuario):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        if usuario !='' :
            cursor.execute("SELECT * FROM prestamos WHERE id_usuario = ?", (usuario,))
            return cursor.fetchall()
        else:
            return 'Ingrese el ISBM'
    except Exception as err:
        return str(err)
    finally:
        conn.close()

def is_libro_prestar(isbm,tipo):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('SELECT tipo FROM prestamos WHERE libros_isbm = ? ORDER BY id DESC LIMIT 1',(isbm,))


    except Exception as err:
        print(str(err))
        return False
    finally:
        conn.close()

def devolver_libro(isbm,id_usuario):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        if isbm =='' and id_usuario =='':
            return 'ingrese todos los atributos'

        if is_libro_prestar(isbm,'DEVOLVER'):
            cursor.execute("INSERT INTO prestamos(libros_isbm, id_usuario, tipo,dia) VALUES(?,?,?,?)",(isbm,id_usuario,'DEVOLVER',date.today()))
            conn.commit()
            return f'Insert Devolver de: {isbm} ,{id_usuario}'
        else:
            return f'No hay libro prestado isbm:{isbm} y id:{id_usuario}'

    except Exception as err:
        return str(err)
    finally:
        conn.close()
