from data.subModel import *

class Model(object):

    def __init__(self):
        self._item_type = 'Usuario'
        self._connection = connect_to_bbdd(ddbb_name)
        create_table(self.connection, self.item_type)

    @property
    def connection(self):
        return self._connection

    @property
    def item_type(self):
        return self._item_type

    def create_item(self, name, last_name, password, comments):
        insert_one(
            self.connection, name, last_name, password, comments, self.item_type)

    def read_item(self, user_id):
        select_one(
            self.connection, user_id, self.item_type)

    def update_item(self, user_id, name, last_name, password, comments):
        update_one(
            self.connection, user_id, name, last_name, password, comments, self.item_type)

    def delete_item(self, user_id):
        delete_one(self.connection, user_id, self.item_type)