import sqlite3

class Model(object):

    def __init__(self):
        self.ddbb_name = "prueba_bbdd2.db"
        self._connection = sqlite3.connect(self.ddbb_name)
        self._miCursor = self._connection.cursor()


    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._miCursor

    def create_table(self):
        self.cursor.execute('''CREATE TABLE USUARIOS(
        USER_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
        NAME VARCHAR(50),
        LAST_NAME VARCHAR(50),
        PASSWORD VARCHAR(10),
        COMMENTS VARCHAR(50))''')

        self.connection.commit()


    def create_item(self, name, last_name, password, comments):
        datos = [name, last_name, password, comments]
        self.cursor.execute("INSERT INTO Usuario VALUES(NULL,?,?,?,?)", (datos))

        self.connection.commit()
        print("Guardado con exito")

    def read_item(self, user_id):
        self.cursor.execute("SELECT * FROM Usuario WHERE USER_ID=?", [user_id])
        usuario = self.cursor.fetchall()
        return usuario

    def update_item(self, user_id, name, last_name, password, comments):
        new_datos =[name, last_name, password, comments, user_id]
        self.cursor.execute("UPDATE Usuario SET NAME=?, LAST_NAME=?, PASSWORD=?, COMMENTS=? WHERE USER_ID=?", new_datos)

        self.connection.commit()
        print('Update Exitoso')

    def delete_item(self, user_id):
        self.cursor.execute("DELETE FROM Usuario WHERE USER_ID=?", [user_id])

        self.connection.commit()
        print('DELETE exitoso')