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

        if not is_libro_prestar(isbm):
            cursor.execute("INSERT INTO prestamos(libros_isbm, id_usuario, tipo,dia) VALUES(?,?,?,?)",(isbm,id_usuario,'PRESTAR',date.today()))
            conn.commit()
            return f'Insert Prestar: {isbm} ,{id_usuario}'
        else:
            return 'El libro ya esta prestado.'

    except Exception as err:
        return str(err)
    finally:
        conn.close()

def is_libro_prestar(isbm):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM prestamos WHERE libros_isbm = ? and tipo = ? ORDER BY dia ASC LIMIT 1',(isbm,'PRESTAR'))
        return len(cursor.fetchall()) > 0
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

        if is_libro_prestar(isbm):
            cursor.execute("INSERT INTO prestamos(libros_isbm, id_usuario, tipo,dia) VALUES(?,?,?,?)",(isbm,id_usuario,'DEVOLVER',date.today()))
            conn.commit()
            return f'Insert Devolver de: {isbm} ,{id_usuario}'
        else:
            return 'No hay libro prestado de este tipo'

    except Exception as err:
        return str(err)
    finally:
        conn.close()
