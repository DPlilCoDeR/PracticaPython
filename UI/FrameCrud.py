from tkinter import *
from tkinter.ttk import *


import data.Basedatos as bbdd


class FrameCrud(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.buttons_crud()
        self.pack()

    def buttons_crud(self):
        Button.__init__(self)
        self.boton_save = Button(self, text="Save", command=lambda: bbdd.BaseDatos.insertar_a_la_bbdd())
        self.boton_save.grid(column=1, row=1)

        self.boton_read = Button(self, text="Read", command=lambda: bbdd.BaseDatos.obtener_de_bbdd())
        self.boton_read.grid(column=2, row=1)

        self.boton_update = Button(self, text="Update", command=lambda: bbdd.BaseDatos.actualizar_bbdd())
        self.boton_update.grid(column=1, row=2)

        self.boton_delete = Button(self, text="Delete", command=lambda: bbdd.BaseDatos.eliminiar_de_bbdd())
        self.boton_delete.grid(column=2, row=2)
