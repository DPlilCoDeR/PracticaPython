from tkinter import messagebox


class VentanasEmergentes:

    @staticmethod
    def guardado_exitoso():
        messagebox.showinfo("Prueba", "Guardado con exito")

    @staticmethod
    def tabla_creada():
        messagebox.showinfo("Exito", "La tabla a sido creada")

    @staticmethod
    def error_tabla():
        messagebox.showwarning("Error", "La tabla ya estaba creada")
