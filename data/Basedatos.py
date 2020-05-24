import sqlite3


class BaseDatos:

    conexion_bbdd = sqlite3.connect("bbdd_practica")
    cursor_bbdd = conexion_bbdd.cursor()

    def __init__(self):
        self.cursor_bbdd.execute("""CREATE TABLE DATOS_FORMULARIO (
        USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(10)
        APELLIDO VARCHAR(30),
        PASSWORD VARCHAR (10),
        COMENTARIOS VARCHAR(50)
        )""")