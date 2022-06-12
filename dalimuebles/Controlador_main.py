from tkinter import Tk
import pestañas


class Controller_note:
    def __init__(self, root_w):
        self.master = root_w
        self.objeto_vista = pestañas.Aplicacion(self.master)


if __name__ == "__main__":
    master = Tk()
    master.wm_title("CRUD de Muebles")
    mi_app = Controller_note(master)
    master.mainloop()
