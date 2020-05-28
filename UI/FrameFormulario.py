from tkinter import *
from tkinter.ttk import *


class FrameFormulario(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.user_id = IntVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.password = StringVar()
        self.comentarios = StringVar()
        self.widget_formulario()
        self.pack()

    def widget_formulario(self):
        self.texto_ID = Label(self, text="ID: ")
        self.texto_ID.grid(column=1, row=1)
        self.entrada_ID = Entry(self, textvariable=self.user_id)
        self.entrada_ID.grid(column=2, row=1, columnspan=2)

        self.texto_nombre = Label(self, text="Nombre: ")
        self.texto_nombre.grid(column=1, row=2)
        self.entrada_nombre = Entry(self, textvariable=self.nombre)
        self.entrada_nombre.grid(column=2, row=2, columnspan=2)

        self.texto_apellido = Label(self, text="Apellido: ")
        self.texto_apellido.grid(column=1, row=3)
        self.entrada_apellido = Entry(self, textvariable=self.apellido)
        self.entrada_apellido.grid(column=2, row=3, columnspan=2)

        self.texto_password = Label(self, text="Password: ")
        self.texto_password.grid(column=1, row=4)
        self.entrada_password = Entry(self, textvariable=self.password)
        self.entrada_password.grid(column=2, row=4, columnspan=2)

        self.texto_comentarios = Label(self, text="Comentarios: ")
        self.texto_comentarios.grid(column=1, row=5)
        self.entrada_comentarios = Entry(self, textvariable=self.comentarios)
        self.entrada_comentarios.grid(column=2, row=5, columnspan=2)
