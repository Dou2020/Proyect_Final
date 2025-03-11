import sqlite3

def createTable():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS prestamos(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    libros_isbm TEXT NOT NULL,
                    id_usuario TEXT NOT NULL,
                    FOREIGN KEY(libros_isbm) REFERENCES libros(isbm)
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
                )
            ''')
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()