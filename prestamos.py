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
                    fecha_devolucion DATE,
                    FOREIGN KEY(libros_isbm) REFERENCES libros(isbm)
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
                )
            ''')
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()

def ver_prestamos():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("SELECT l.titulo,u.nombre, p.dia, p.fecha_devolucion, p.tipo FROM prestamos p INNER JOIN "
        "libros l ON l.isbm = p.libros_isbm INNER JOIN usuarios u ON u.id = p.id_usuario")
        #print(cursor.fetchall())
        return cursor.fetchall()
    except Exception as err:
        return(str(err))
    finally:
        conn.close()

def buscar_prestamo_libro(isbm):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("SELECT l.titulo,u.nombre, p.dia, p.fecha_devolucion, p.tipo FROM prestamos p INNER JOIN "
        "libros l ON l.isbm = p.libros_isbm INNER JOIN usuarios u ON u.id = p.id_usuario WHERE p.libros_isbm = ?",(isbm,))
        return cursor.fetchall()
    except Exception as err:
        return(str(err))
    finally:
        conn.close()

def buscar_prestamo_usuario(id_usuario):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("SELECT l.titulo,u.nombre, p.dia, p.fecha_devolucion, p.tipo FROM prestamos p INNER JOIN "
        "libros l ON l.isbm = p.libros_isbm INNER JOIN usuarios u ON u.id = p.id_usuario WHERE p.id_usuario = ?",(id_usuario,))
        return cursor.fetchall()
    except Exception as err:
        return(str(err))
    finally:
        conn.close()

def prestar_libro(isbm,id_usuario,fecha_prestamo):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        if isbm == '' and id_usuario == '':
            return 'Ingrese todos los atributos'

        if not is_libro_prestar(isbm):
            cursor.execute("INSERT INTO prestamos(libros_isbm, id_usuario, tipo,dia, fecha_devolucion) VALUES(?,?,?,?,?)",(isbm,id_usuario,'PRESTADO',date.today(),fecha_prestamo,))
            conn.commit()
            if cursor.rowcount == 1:
                return f'El libro fue prestado con exito, detalle: {isbm} ,{id_usuario}'
            else:
                return 'El libro o el usuario no existe.'
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

        cursor.execute('SELECT * FROM prestamos WHERE libros_isbm = ? and tipo = ? ORDER BY dia ASC LIMIT 1',(isbm,'PRESTADO'))
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
            cursor.execute("UPDATE prestamos SET tipo = ? WHERE libros_isbm = ? AND id_usuario = ? AND tipo = ?", ('DEVUELTO',isbm,id_usuario, 'PRESTADO'))
            conn.commit()
            if cursor.rowcount == 1:
                return f'El libro fue devuelto con exito: {isbm} ,{id_usuario}'
            else:
                return 'No hay libro prestado con estos datos'
        else:
            return 'No hay libro prestado con estos datos'

    except Exception as err:
        return str(err)
    finally:
        conn.close()