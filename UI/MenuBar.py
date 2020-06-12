from tkinter import *
from app.Controller import *


class MenuBar(Menu):

    def __init__(self, parent, controller):
        Menu.__init__(self, parent)
        self.controller = controller

        file_menu = Menu(self, tearoff=False)
        self.add_cascade(label="BBDD", underline=0, menu=file_menu)
        file_menu.add_command(label="Crear tabla", underline=1)
        file_menu.add_command(label="Exit", command=self.quit)

        borrar_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Borrar", menu=borrar_menu)
        borrar_menu.add_command(label="Borrar Campos", command= lambda: self.controller.borrar_campos())

        ayuda_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Ayuda", underline=0, menu=ayuda_menu)
        ayuda_menu.add_command(label="Saber mas...")
