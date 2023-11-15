import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from modules.recognition.recognition_functions import create_user, user_verification

def add_user_command():
    try:
        # Получаем введенное имя пользователя из текстового поля
        username = txt.get().strip()  # Убедимся, что у нас нет лишних пробелов

        # Проверяем, что введено имя пользователя
        if not username:
            showerror("Ошибка", "Введите имя пользователя")
            return

        # Вызываем функцию для добавления пользователя
        create_user(username)

        # Выводим информационное сообщение об успешном добавлении пользователя
        showinfo("Информация", "Пользователь успешно добавлен")

    except Exception as ex:
        # В случае ошибки выводим сообщение об ошибке
        showerror("Ошибка", str(ex))

def user_verification_command():
    try:
        # Вызываем функцию для проверки пользователя
        result = user_verification()

        # Проверяем результат проверки
        if result[0]:
            # Если пользователь распознан, выводим приветствие с именем пользователя
            showinfo("Информация", f"Привет, {result[1]}!")
        else:
            # Если пользователь не распознан, выводим сообщение об ошибке
            showerror("Ошибка", "ACHTUNG: Неизвестный пользователь")

    except Exception as ex:
        # В случае ошибки выводим сообщение об ошибке
        showerror("Ошибка", str(ex))

# Создаем основное окно приложения
main_window = tk.Tk()

# Задаем заголовок окна
main_window.title("Face Recognition")

# Устанавливаем размеры окна
main_window.geometry("350x300")

# Создаем и настраиваем виджеты
for c in range(2):
    main_window.columnconfigure(index=c, weight=1)
for r in range(2):
    main_window.rowconfigure(index=r, weight=1)

# Создаем кнопку для проверки пользователя
btn1 = tk.Button(text="Проверить пользователя", command=user_verification_command)
btn1.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

# Создаем кнопку для добавления пользователя
btn3 = tk.Button(text="Добавить пользователя", command=add_user_command)
btn3.grid(row=1, column=0, columnspan=1, ipadx=70, ipady=6, padx=5, pady=5)

# Создаем текстовое поле для ввода имени пользователя
txt = tk.Entry()
txt.grid(row=1, column=1, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

# Запускаем основной цикл приложения
main_window.mainloop()
