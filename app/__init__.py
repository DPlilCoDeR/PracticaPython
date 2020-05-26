from UI.FrameFormulario import *

"""root = Tk()
app = Gui(master=root)
app.config(menu=Gui.menuBar)
app.mainloop()"""


def hello():
    print("hello!")


class Application(Tk):

    def __init__(self):
        Tk.__init__(self)
        frame = FrameFormulario()
        frame.widget_formulario()
        frame.botones_crud()
        frame.barra_menus()
        self.config(menu=frame.menuBar)

if __name__ == "__main__":
    ui = Application()
    ui.mainloop()
