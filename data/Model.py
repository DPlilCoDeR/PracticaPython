from data.subModel import *

class Model(object):

    def __init__(self):
        self._item_type = 'product'
        self._connection = connect_to_bbdd(ddbb_name)
        create_table(self.connection, self.item_type)

    @property
    def connection(self):
        return self._connection

    @property
    def item_type(self):
        return self._item_type

    def create_item(self, name, price, quantity):
        insert_one(
            self.connection, name, price, quantity, self.item_type)

    def read_item(self, name):
        select_one(
            self.connection, name, self.item_type)

    def update_item(self, name, price, quantity):
        update_one(
            self.connection, name, price, quantity, self.item_type)

    def delete_item(self, name):
        delete_one(self.connection, name, self.item_type)