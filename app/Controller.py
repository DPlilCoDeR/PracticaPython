from tkinter import *

from data.Model import Model
from UI.FrameFormulario import FrameFormulario
from UI.MenuBar import MenuBar


class Controller:

    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = FrameFormulario(self)
        self.menu = MenuBar(self.root, self)

        self.user_id = self.view.id_variable.get()
        self.name = self.view.nombre_variable.get()
        self.last_name = self.view.apellido_variable.get()
        self.password = self.view.password_variable.get()

        self.root.config(menu=self.menu)
        self.root.mainloop()

    def borrar_campos(self):
        self.view.id_variable.set("")
        self.view.nombre_variable.set("")
        self.view.apellido_variable.set("")
        self.view.password_variable.set("")

    def show_item(self, user_id):

        user = self.model.read_item(user_id)
        self.view.nombre_variable.set(user)

    def insert_item(self, name, last_name, password, comments=None):
        item_type = self.model.item_type
        try:
            self.model.create_item(name, last_name, password, comments)
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(name, item_type, e)

    def update_item(self, name, price, quantity):
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type

        try:
            older = self.model.read_item(name)
            self.model.update_item(name, price, quantity)
            self.view.display_item_updated(
                name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def update_item_type(self, new_item_type):
        old_item_type = self.model.item_type
        self.model.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)

    def delete_item(self, name):
        item_type = self.model.item_type
        try:
            self.model.delete_item(name)
            self.view.display_item_deletion(name)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
