from tkinter import *
from tkinter.ttk import *
from .FrameCrud import FrameCrud


class FrameFormulario(Frame):

    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.widget_formulario()
        self.widget_crud = FrameCrud(self.controller)
        self.pack()

    def widget_formulario(self):
        self.texto_ID = Label(self, text="ID: ")
        self.texto_ID.grid(column=0, row=1)
        self.id_variable = IntVar()
        self.entrada_ID = Entry(self, textvariable=self.id_variable)
        self.entrada_ID.grid(column=1, row=1, columnspan=2)

        self.texto_nombre = Label(self, text="Nombre: ")
        self.texto_nombre.grid(column=0, row=2)
        self.nombre_variable = StringVar()
        self.entrada_nombre = Entry(self, textvariable=self.nombre_variable)
        self.entrada_nombre.grid(column=1, row=2, columnspan=2)

        self.texto_apellido = Label(self, text="Apellido: ")
        self.texto_apellido.grid(column=0, row=3)
        self.apellido_variable = StringVar()
        self.entrada_apellido = Entry(self, textvariable=self.apellido_variable)
        self.entrada_apellido.grid(column=1, row=3, columnspan=2)

        self.texto_password = Label(self, text="Password: ")
        self.texto_password.grid(column=0, row=4)
        self.password_variable = StringVar()
        self.entrada_password = Entry(self, textvariable=self.password_variable)
        self.entrada_password.config(show="*")
        self.entrada_password.grid(column=1, row=4, columnspan=2)

        self.texto_comentarios = Label(self, text="Comentarios: ")
        self.texto_comentarios.grid(column=0, row=5)
        self.entrada_comentarios = Text(self, width=20, height=10)
        self.entrada_comentarios.grid(column=1, row=5, columnspan=2)
