from tkinter import *
from tkinter.ttk import *


class FrameCrud(Frame):

    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.buttons_crud()
        self.pack()

    def buttons_crud(self):
        Button.__init__(self)
        self.boton_save = Button(self, text="Save", command=lambda: self.controller.insert_item(self.controller.name, self.controller.last_name, self.controller.password))
        self.boton_save.grid(column=0, row=0)

        self.boton_read = Button(self, text="Read", command=lambda: self.controller.show_item(self.controller.user_id))
        self.boton_read.grid(column=1, row=0)

        self.boton_update = Button(self, text="Update", command=lambda: self.controller.update_item())
        self.boton_update.grid(column=2, row=0)

        self.boton_delete = Button(self, text="Delete", command=lambda: self.controller.delete_item())
        self.boton_delete.grid(column=3, row=0)
