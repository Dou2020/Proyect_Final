import sqlite3

def create_table():
    try:
        with sqlite3.connect('biblioteca.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS morosidad (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isbn_libros TEXT NOT NULL,
                    id_usuario TEXT NOT NULL,
                    FOREIGN KEY (isbn_libros) REFERENCES libros(isbn),
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
                )
            ''')
    except sqlite3.DatabaseError as db_err:
        print(f"Error en la base de datos: {db_err}")
    except Exception as err:
        print(f"Error general: {err}")


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