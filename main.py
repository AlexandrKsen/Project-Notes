from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

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
    text.delete('1,0', END)
    text.insert('1,0', data)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.csv')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Неизвестная ошибка. Невозможно сохранить файл.")


#def open_catalog:






root = Tk()
root.title("Заметки")
root.geometry("500x300")

text = Text(root, width=400, height=400)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
file_catalogs = Menu(menu_bar)

file_menu.add_command(label="NewNote", command=new_file)
file_menu.add_command(label="OpenNote", command=open_file)
file_menu.add_command(label="SaveAs", command=save_as)

menu_bar.add_cascade(label="Файл", menu=file_menu)

# file_catalogs.add_command(label="Прочитать каталог", command=open_catalog)
file_catalogs.add_command(label="Прочитать каталог", )
#file_catalogs.add_command(label="Удалить файл", command=save_as)
file_catalogs.add_command(label="Удалить файл", command=save_as)

menu_bar.add_cascade(label="Каталог", menu=file_catalogs)

root.config(menu=menu_bar)
root.mainloop()

