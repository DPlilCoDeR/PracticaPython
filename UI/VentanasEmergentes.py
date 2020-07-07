from tkinter import messagebox


class VentanasEmergentes:

    @staticmethod
    def guardado_exitoso():
        messagebox.showinfo("Save", "Guardado con exito")

    @staticmethod
    def update_exitoso():
        messagebox.showinfo('Update', 'Actualizado con exito')

    @staticmethod
    def delete_exitoso():
        messagebox.showinfo('Delete', 'Borrado con exito')

    @staticmethod
    def tabla_creada():
        messagebox.showinfo("Exito", "La tabla a sido creada")

    @staticmethod
    def error_tabla():
        messagebox.showwarning("Error", "La tabla ya esta creada")
