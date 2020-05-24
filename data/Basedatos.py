import sqlite3


class BaseDatos:
    conexion_bbdd=sqlite3.connect("bbdd_practica")