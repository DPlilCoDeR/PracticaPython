from tkinter import *
from tkinter.ttk import *

import data.Basedatos as bbdd


class Gui(Frame):
    user_id = IntVar()
    nombre = StringVar()
    apellido = StringVar()
    password = StringVar()
    comentarios = StringVar()

    def widget_formulario(self,):
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
        self.entrada_apellido = Entry(self, self.apellido)
        self.entrada_apellido.grid(column=2, row=3, columnspan=2)

        self.texto_password = Label(self, text="Password: ")
        self.texto_password.grid(column=1, row=4)
        self.entrada_password = Entry(self, self.password)
        self.entrada_password.grid(column=2, row=4, columnspan=2)

        self.texto_comentarios = Label(self, text="Comentarios: ")
        self.texto_comentarios.grid(column=1, row=5)
        self.entrada_comentarios = Entry(self, self.comentarios)
        self.entrada_comentarios.grid(column=2, row=5, columnspan=2)

    def botones_crud(self):
        self.boton_save = Button(self, text="Save", command=lambda: bbdd.BaseDatos.insertar_a_la_bbdd())
        self.boton_save.grid(column=1, row=6)

        self.boton_read = Button(self, text="Read", command=lambda: bbdd.BaseDatos.obtener_de_bbdd())
        self.boton_read.grid(column=2, row=6)

        self.boton_update = Button(self, text="Update", command=lambda: bbdd.BaseDatos.actualizar_bbdd())
        self.boton_update.grid(column=3, row=6)

        self.boton_delete = Button(self, text="Delete", command=lambda: bbdd.BaseDatos.eliminiar_de_bbdd())
        self.boton_delete.grid(column=4, row=6)

    def barra_menus(self):
        pass

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.widget_formulario()
        self.botones_crud()
        self.barra_menus()
