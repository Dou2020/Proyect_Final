import sqlite3
from datetime import date
def create_table():
    try:
        with sqlite3.connect('biblioteca.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS morosidad (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isbm_libros TEXT NOT NULL,
                    id_usuario TEXT NOT NULL,
                    fecha_devolucion DATE NOT NULL,
                    FOREIGN KEY(isbm_libros) REFERENCES libros(isbm),
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario)
                )
            ''')
    except sqlite3.DatabaseError as db_err:
        print(f"Error en la base de datos: {db_err}")
    except Exception as err:
        print(f"Error general: {err}")

def ver_morosidad_prestamos():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("SELECT l.titulo, u.nombre, p.dia, p.fecha_devolucion, p.tipo FROM prestamos p INNER JOIN "
        "libros l ON l.isbm = p.libros_isbm INNER JOIN usuarios u ON u.id = p.id_usuario WHERE p.fecha_devolucion < p.dia AND p.tipo = 'PRESTADO'")
        return cursor.fetchall()
    except Exception as err:
        return(str(err))
    finally:
        conn.close()

def agregar_morosidad(isbm, id_usuario):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO morosidad(isbm_libros, id_usuario, fecha_devolucion) VALUES(?,?,?)",(isbm, id_usuario, date.today()))
        conn.commit()
        return f'La morosidad se ha registrado correctamente. Datos: {isbm}, {id_usuario}'
    except Exception as err:
        return str(err)
    finally:
        conn.close()

def ver_todas_morosidades():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT l.titulo, u.nombre, p.dia, p.fecha_devolucion, m.fecha_devolucion FROM morosidad m INNER JOIN "
        "libros l ON l.isbm = m.isbm_libros INNER JOIN usuarios u ON u.id = m.id_usuario INNER JOIN prestamos p ON p.libros_isbm = m.isbm_libros AND p.id_usuario = m.id_usuario")
        return cursor.fetchall()
    except Exception as err:
        return(str(err))
    finally:
        conn.close()

def morosidad(isbn, id_usuario):
    """
    Verifica si un usuario tiene un libro en morosidad.
    Retorna True si el usuario tiene morosidad con el libro, de lo contrario False.
    """
    try:
        with sqlite3.connect('biblioteca.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT COUNT(*) FROM morosidad 
                WHERE isbn_libros = ? AND id_usuario = ?
            ''', (isbn, id_usuario))
            resultado = cursor.fetchone()

            return resultado[0] > 0  # Retorna True si existe el registro, False si no
    except sqlite3.DatabaseError as db_err:
        print(f"Error en la base de datos: {db_err}")
        return False
    except Exception as err:
        print(f"Error general: {err}")
        return False


def devolver_conmorosidad(isbn, id_usuario):
    """
    Elimina el registro de morosidad cuando el usuario devuelve el libro.
    """
    try:
        with sqlite3.connect('biblioteca.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM morosidad 
                WHERE isbn_libros = ? AND id_usuario = ?
            ''', (isbn, id_usuario,))
            conn.commit()
            print("Libro devuelto y morosidad eliminada.")
    except sqlite3.DatabaseError as db_err:
        print(f"Error en la base de datos: {db_err}")
    except Exception as err:
        print(f"Error general: {err}")