import tkinter as tk
from math import sqrt

def calculate_function(event=None):
    a = float(entry_a.get())
    b = float(entry_b.get())
    
    result = (sqrt(a / (b - a))) * ((b**2 + a * b)) - abs(b + 2)
    format_result = "{:.2f}".format(result)  # Вивести з точністю до 2 знаків після коми
    label_result.config(text="Результат: " + format_result)  # Оновити текст в Label
    
   
root = tk.Tk()
root.title("Обчислення функції")
root.geometry("400x400")  # Змінити розміри вікна (ширина x висота)

# Змінити фон вікна
#root.configure(bg="#f2f2f2")  # Встановити колір фону за HEX-кодом


# Зображення
label_image = tk.Label()
label_image.pack()
photo = tk.PhotoImage(file="f1.png")
label_image.configure(image=photo)

label_a = tk.Label(root, text="Введіть значення a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

# Написи та поля введення
label_b = tk.Label(root, text="Введіть значення b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()


# Кнопка для обчислення
button_calculate = tk.Button(root, text="Обчислити")
button_calculate.pack()
button_calculate.bind('<Button-1>', calculate_function)


# Відображення результату
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()