import tkinter as tk
from math import sqrt

def calculate_function(event=None):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        p = (a + b + c) / 2
        R = (a * b * c) / (4 * sqrt(p * (p - a) * (p - b) * (p - c)))
        w_a = (2 / (b + c)) * sqrt(b * c * p * (p - a))

        format_R = "{:.2f}".format(R)
        format_p = "{:.2f}".format(p)
        format_w = "{:.2f}".format(w_a)
        
        label_result.config(text=f"R = {format_R}, wₐ = {format_w}")
    except Exception as e:
        label_result.config(text=f"Помилка: {str(e)}")


   

root = tk.Tk()
root.title("Обчислення функції")
root.geometry("400x400")  # Змінити розміри вікна (ширина x висота)

# Змінити фон вікна
#root.configure(bg="#f2f2f2")  # Встановити колір фону за HEX-кодом


# Зображення
label_image = tk.Label()
label_image.pack()
photo = tk.PhotoImage(file="lb13.2.gif")
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

label_c = tk.Label(root, text="Введіть значення c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()



# Кнопка для обчислення
button_calculate = tk.Button(root, text="Обчислити",command=calculate_function)
button_calculate.pack()
button_calculate.bind('<Button-1>', calculate_function)


# Відображення результату
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()