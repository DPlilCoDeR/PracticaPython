from tkinter import *
from tkinter.ttk import *
from .FrameCrud import FrameCrud


class FrameFormulario(Frame):

    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.widget_formulario()
        self.buttons_crud()
        self.pack()

    def widget_formulario(self):
        self.texto_ID = Label(self, text="ID: ")
        self.texto_ID.grid(column=0, row=1)
        self.id_variable = StringVar()
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

    def buttons_crud(self):
        self.boton_save = Button(self, text="Save", command=lambda: self.controller.insert_item(self.nombre_variable.get(), self.apellido_variable.get(), self.password_variable.get()))
        self.boton_save.grid(column=0, row=0)

        self.boton_read = Button(self, text="Read", command=lambda: self.controller.show_item(self.id_variable.get()))
        self.boton_read.grid(column=1, row=0)

        self.boton_update = Button(self, text="Update", command=lambda: self.controller.update_item(self.id_variable.get(), self.nombre_variable.get(), self.apellido_variable.get(), self.password_variable.get()))
        self.boton_update.grid(column=2, row=0)

        self.boton_delete = Button(self, text="Delete", command=lambda: self.controller.delete_item())
        self.boton_delete.grid(column=3, row=0)
