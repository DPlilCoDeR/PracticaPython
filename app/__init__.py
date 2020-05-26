from UI.FrameFormulario import *
from UI.MenuBar import *
from UI.FrameCrud import *


class Application(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Practica Guiada")
        menubar = MenuBar(self)
        self.config(menu=menubar)

        FrameFormulario()
        FrameCrud()


if __name__ == "__main__":
    ui = Application()
    ui.mainloop()
