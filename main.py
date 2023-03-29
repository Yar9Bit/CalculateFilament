from tkinter import *
from tkinter import ttk
from data import filament
from math import pi


class FilamentFrame(ttk.Frame):
    d = 1.75

    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 10, 'pady': 5}
        fil_list = [fl for fl in filament]

        self.combobox = ttk.Combobox(values=fil_list)
        self.combobox.pack(anchor=W, **options)

        self.label = ttk.Label(text='Выбор пластика')
        self.label.pack(before=self.combobox, anchor=W, **options)
        self.label_consumption = ttk.Label(font=30)
        self.label_consumption.pack(anchor=N)

        self.label_ent = ttk.Label(text='Введите длину расхода прутка филамента(мм)')
        self.ent = ttk.Entry()
        self.btn_ent = ttk.Button(text='Расчёт расхода пластика', command=self.calculate_consumption)
        self.ent.pack(**options)
        self.btn_ent.pack(after=self.ent, **options)
        self.label_ent.pack(before=self.ent, **options)

        self.pack()

    def filament_volume(self) -> float:
        sel_filament = filament.get(self.combobox.get()).get('density')
        inp_mm = abs(int(self.ent.get()))
        consumption = ((inp_mm * pi * (self.d ** 2) / 4) * sel_filament)
        return consumption

    def calculate_consumption(self) -> None:
        self.label_consumption['text'] = '{0:.3f} грамм'.format(self.filament_volume() / 1000)
        return None


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 10, 'pady': 10}

        self.label = ttk.Label(self, text='Программа для расчёта расхода пластика', font=22)
        self.label.pack(**options)

        self.pack(anchor=CENTER, expand=False)


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Программа')
        self.geometry('640x640')


if __name__ == '__main__':
    app = App()
    frame = MainFrame(app)
    combobox_frame = FilamentFrame(app)
    app.mainloop()
