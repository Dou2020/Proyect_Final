import sqlite3


conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS morosidad(
            id integer PRIMARY KEY AUTOINCREMENT,
            isbm_libros TEXT NOT NULL,
            id_usuario TEXT NOT NULL,
            FOREIGN KEY(isbm_libros) REFERENCES libros(isbm),
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario)
        )
    ''')
conn.commit()
conn.close()