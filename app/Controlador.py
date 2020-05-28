from data.Basedatos import *


class Controlador(BaseDatos):

    def __init__(self):
        super().__init__()

    def insert(self, nombre, apellido, password, comentarios):
        self.execute('INSERT INTO DATOS_USUARIO VALUES(NULL,?,?,?,?)', (nombre, apellido, password, comentarios))
        print(nombre)
        return

    def read(self,user_id):
        self.query("""SELECT * FROM DATOS_USUARIO WHERE USER_ID=?""", user_id)

    def update_bbdd(self, nombre, apellido, password, comentarios, user_id):
        self.execute("""UPDATE DATOS_USUARIO SET NOMBRE=?, APELLIDO=?, PASSWORD=?, COMENTARIOS=? WHERE USER_ID = 
        ?""", (nombre, apellido, password, comentarios, user_id))

    def delete(self, user_id):
        self.execute("""DELETE FROM DATOS_USUARIO WHERE USER_ID=?""", user_id)
