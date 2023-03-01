import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import filedialog as fd


file_name = NONE
All_catalogs = ''

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.csv')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Неизвестная ошибка. Невозможно сохранить файл.")


def curent_catalog():
    All_catalogs = os.getcwd()
    print('Текущий каталог = '+All_catalogs)


def open_catalog():
    Out_files_in_catalogs =os.getcwd()
    result = os.walk(Out_files_in_catalogs)
    for i, j, k in result:
        for file in k:


            substring = ".csv"
            if file.find(substring) != -1:
                text.insert(END, "\n" + file)
            else:
                print
                "Подстрока не найдена!"



def remove_note():
    filetypes = (
        ('text files', '*.csv'),)

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    print('выбранный файл = '+filename+' удален ')
    os.remove(filename)


root = Tk()
root.title("Заметки")
root.geometry("500x300")

text = Text(root, width=500, height=300)
text.pack()

menu_bar = Menu(root)

#Otbor_Cataloga = Menu(menu_bar)
file_menu = Menu(menu_bar)
file_catalogs = Menu(menu_bar)


file_menu.add_command(label="Создать заметку...", command=new_file)
file_menu.add_command(label="Открыть заметку...", command=open_file)
file_menu.add_command(label="Сохранить заметку как...", command=save_as)
file_menu.add_command(label="Удалить заметку...", command=remove_note)
menu_bar.add_cascade(label="Файл", menu=file_menu)

file_catalogs.add_command(label="Список заметок...", command=open_catalog)
menu_bar.add_cascade(label="Каталог", menu=file_catalogs)



root.config(menu=menu_bar)
root.mainloop()
