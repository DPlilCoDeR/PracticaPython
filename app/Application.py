from UI.FrameCrud import *
from UI.MenuBar import *
from UI.FrameFormulario import *


class Application(Tk):

    def __init__(self, db):
        Tk.__init__(self)
        self.database = db
        self.title("Practica Guiada")
        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)
        self.formulario = FrameFormulario(self)
        self.crud = FrameCrud(self.formulario.user_id, self.formulario.nombre.get(), self.formulario.apellido.get(), self.formulario.password.get(), self.formulario.comentarios.get())
