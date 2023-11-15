import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from modules.recognition.recognition_functions import create_user, user_verification


def add_user_command():
    try:
        username = txt.get()
        if username == None or len(username) == 0:
            showerror("Ошибка", "Введите имя пользователя")
        create_user(username)
        showinfo("Информация", "Пользователь успшено добавлен")
    except Exception as ex:
        showerror("Ошибка", str(ex))


def user_verification_command():
    try:
        result = user_verification()

        if result[0]:
            showinfo("Информация", f"Привет, {result[1]}!")
        else:
            showerror("Ошибка", "ACHTUNG: Неизвестный пользователь")
    except Exception as ex:
        showerror("Ошибка", str(ex))


main_window = tk.Tk()
main_window.title = "Face Recognition"
main_window.geometry("350x300")

for c in range(2):
    main_window.columnconfigure(index=c, weight=1)
for r in range(2):
    main_window.rowconfigure(index=r, weight=1)

btn1 = tk.Button(text="Проверить пользователя", command=user_verification_command)
btn1.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

btn3 = tk.Button(text="Добавить пользователя", command=add_user_command)
btn3.grid(row=1, column=0, columnspan=1, ipadx=70, ipady=6, padx=5, pady=5)

txt = tk.Entry()
txt.grid(row=1, column=1, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

main_window.mainloop()
