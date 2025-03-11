
import libros
libros.create_table()

# Pruebas de funcionalidades
print(libros.agregar_libro('code1','anonimo','code1'))
print(libros.agregar_libro('code2','anonimo','code2'))
print(libros.agregar_libro('code3','anonimo','code3'))
print(libros.ver_libros())
print(libros.eliminar_libro('code3'))
print(libros.buscar_libro('code2'))

import usuarios
usuarios.create_table()

# Pruebas de Funcionalidades
print(usuarios.registrar_usuario('user1','Dou',22))
print(usuarios.registrar_usuario('user2','Eduar',12))
print(usuarios.registrar_usuario('user3','Eduar',12))
print(usuarios.ver_usuarios())
print(usuarios.eliminar_usuario('user3'))

import prestamos
prestamos.createTable()


import morosidad
import utilidades
