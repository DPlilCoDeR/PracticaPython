from app.Application import *
from data.Basedatos import *

if __name__ == "__main__":
    base_datos = BaseDatos()
    ui = Application(base_datos)
    ui.mainloop()
