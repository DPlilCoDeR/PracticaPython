from tkinter import *
from data.Basedatos import *

class MenuBar(Menu):

    def __init__(self, parent):
        Menu.__init__(self, parent)

        self.db = BaseDatos()

        file_menu = Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=file_menu)
        file_menu.add_cascade(label="Crear tabla", underline=1, command=lambda: self.db.execute("""CREATE TABLE DATOS_USUARIO(
                                                                                         USER_ID INTEGER PRIMARY KEY
                                                                                         AUTOINCREMENT,
                                                                                         NOMBRE VARCHAR(20),
                                                                                         APELLIDO VARCHAR(20), 
                                                                                         PASSWORD VARCHAR(10),
                                                                                         COMENTARIOS VARCHAR (80))"""))
        file_menu.add_command(label="Exit", command=self.quit)

        crud_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Crud", underline=0, menu=crud_menu)
        crud_menu.add_cascade(label="Save")
        crud_menu.add_cascade(label="Read")
        crud_menu.add_cascade(label="Update")
        crud_menu.add_cascade(label="Delete")

        ayuda_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Ayuda", underline=0, menu=ayuda_menu)
        ayuda_menu.add_cascade(label="Saber mas...")