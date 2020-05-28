from tkinter import *
from tkinter.ttk import *
from app.Controlador import *


class FrameCrud(Frame):

    def __init__(self, user_id, nombre, apellido, password, comentarios, master=None):
        super().__init__(master)
        self.user_id = user_id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.comentarios = comentarios
        self.controlador = Controlador()
        self.buttons_crud()
        self.pack()

    def buttons_crud(self):
        Button.__init__(self)
        self.boton_save = Button(self, text="Save", command=lambda: self.controlador.insert(self.nombre, self.apellido, self.password, self.comentarios))
        self.boton_save.grid(column=1, row=1)

        self.boton_read = Button(self, text="Read", command=lambda: self.controlador.read(self.user_id))
        self.boton_read.grid(column=2, row=1)

        self.boton_update = Button(self, text="Update", command=lambda: self.controlador.update_bbdd(self.nombre, self.apellido, self.password, self.comentarios, self.user_id))
        self.boton_update.grid(column=1, row=2)

        self.boton_delete = Button(self, text="Delete", command=lambda: self.controlador.delete(self.user_id))
        self.boton_delete.grid(column=2, row=2)
