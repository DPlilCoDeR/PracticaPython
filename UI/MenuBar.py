from tkinter import *
from app.Controller import *


class MenuBar(Menu):

    def __init__(self, parent, controller):
        Menu.__init__(self, parent)
        self.controller = controller

        file_menu = Menu(self, tearoff=False)
        self.add_cascade(label="BBDD", underline=0, menu=file_menu)
        file_menu.add_command(label="Crear tabla", underline=1, command=lambda: self.controller.create_table())
        file_menu.add_command(label="Exit", command=self.quit)

        crud_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Operaciones", menu=crud_menu)
        crud_menu.add_command(label='Guardar', command=lambda: self.controller.insert_item())
        crud_menu.add_command(label='Leer', command=lambda: self.controller.show_item())
        crud_menu.add_command(label='Actualizar', command=lambda: self.controller.update_item())
        crud_menu.add_command(label='Borrar', command=lambda: self.controller.delete_item())

        borrar_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Borrar", menu=borrar_menu)
        borrar_menu.add_command(label="Borrar Campos", command=lambda: self.controller.clean_form())

        ayuda_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Ayuda", underline=0, menu=ayuda_menu)
        ayuda_menu.add_command(label="Saber mas...")
