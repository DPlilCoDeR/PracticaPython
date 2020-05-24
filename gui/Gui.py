from tkinter import *
from tkinter.ttk import *


class Gui(Frame):

    def widget_formulario(self):

        self.texto_ID = Label(self, text="ID: ")
        self.texto_ID.grid(column=1, row=1)
        self.entrada_ID = Entry(self)
        self.entrada_ID.grid(column=2, row=1)

        self.texto_nombre = Label(self, text="Nombre: ")
        self.texto_nombre.grid(column=1, row=2)
        self.entrada_nombre = Entry(self)
        self.entrada_nombre.grid(column=2, row=2)

        self.texto_apellido = Label(self, text="Apellido: ")
        self.texto_apellido.grid(column=1, row=3)
        self.entrada_apellido = Entry(self)
        self.entrada_apellido.grid(column=2, row=3)

        self.texto_password = Label(self, text="Password: ")
        self.texto_password.grid(column=1, row=4)
        self.entrada_password = Entry(self)
        self.entrada_password.grid(column=2, row=4)

        self.texto_comentarios = Label(self, text="Comentarios: ")
        self.texto_comentarios.grid(column=1, row=5)
        self.entrada_comentarios = Entry(self)
        self.entrada_comentarios.grid(column=2, row=5)

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.widget_formulario()
