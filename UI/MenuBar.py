from tkinter import *


class MenuBar(Menu):

    def __init__(self, parent):
        Menu.__init__(self, parent)
        file_menu = Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=file_menu)
        file_menu.add_command(label="Exit", underline=1, command=self.quit)
