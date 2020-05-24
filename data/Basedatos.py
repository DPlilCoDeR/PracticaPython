import sqlite3


class BaseDatos:

    conexion_bbdd = sqlite3.connect("bbdd_practica")
    cursor_bbdd = conexion_bbdd.cursor()

    def insertar_a_la_bbdd(self, nombre, apellidos, password, comentarios):
        self.cursor_bbdd.execute("INSERT INTO DATOS_FORMULARIO VALUES (?, ?, ?, ?)", nombre, apellidos, password, comentarios)

    def obteber_de_bbdd(self, user_id):
        self.cursor_bbdd.execute('SELECT * FROM DATOS_FORMULARIOS WHERE USER_ID=?', user_id)

    def actualizar_bbdd(self, user_id):
        self.cursor_bbdd.execute('UPDATE DATOS_FORMULARIO SET WHERE USER_ID=?', user_id)

    def eliminiar_de_bbdd(self, user_id):
        self.cursor_bbdd.execute('DELETE FROM DATOS_FORMULARIO WHERE USER_ID=?', user_id)

    def __init__(self):
        self.cursor_bbdd.execute("""CREATE TABLE DATOS_FORMULARIO (
        USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(10)
        APELLIDO VARCHAR(30),
        PASSWORD VARCHAR (10),
        COMENTARIOS VARCHAR(50)
        )""")