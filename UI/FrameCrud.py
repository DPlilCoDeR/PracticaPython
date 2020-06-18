from tkinter import *
from tkinter.ttk import *


class FrameCrud(Frame):

    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.buttons_crud()
        self.pack()


