import tkinter as tk
from tkinter import ttk, messagebox
import os
import string
import turtle as t

from Фрактали.Пилюка_Кантора_Всі_порядки import draw_cantor
from Фрактали.Сніжинка_Коха_Всі_порядки import koch
from Фрактали.Трикутник_Серпінського_Всі_порядки import triangle,sierpinski_triangle
from Фрактали.Сніжинка_2 import snowflake

# from Сніжинка_Коха_Всі_порядки import koch

def is_number(char): 
      return char.isdigit() # повертає True тільки в тому випадку  коли значення є цифрою


def Cantor_dust_draw(): # Малює Пилюку Кантора
    top = tk.Toplevel(root)
    top.title("Пилюка Кантора")
    top.geometry("250x150")

    lable = tk.Label(top,text="Вкажіть від 1 до 4 ")
    lable.pack(pady=2)

    entry = tk.Entry(top,width=1,validate="key") # Введення зміної entry
    vcmd = (top.register(is_number),'%S') # Перевірка на цифру
    entry.config(validate="key",validatecommand=vcmd)
    entry.pack(pady=5)

    error_label = tk.Label(top,text="",fg="red")
    error_label.pack(pady=7)

    def Exception():
        value = entry.get()
        if value == "":
            error_label.config(text="Пустий рядок! Введіть число від 1 до 4.")
        elif not (1 <= int(value) <= 4):
            error_label.config(text="Число повинно бути від 1 до 4!")
        else:
            error_label.config(text="")
            t.hideturtle()     
            t.clear()          

            draw_cantor(int(value)-1, 120)

            t.penup()          
            t.home()           
            t.pendown()        
                    
    button = tk.Button(top,text="Натиснути",command=Exception)
    button.pack(pady=6)    


def Kochs_Snowflake_draw():
    top = tk.Toplevel(root)
    top.title("Сніжинка_Коха")
    top.geometry("250x150")

    lable = tk.Label(top,text="Вкажіть від 1 до 4 ")
    lable.pack(pady=2)

    entry = tk.Entry(top,width=1,validate="key") # Введення зміної entry
    vcmd = (top.register(is_number),'%S') # Перевірка на цифру
    entry.config(validate="key",validatecommand=vcmd)
    entry.pack(pady=5)

    error_label = tk.Label(top,text="",fg="red")
    error_label.pack(pady=7)

    def Exception():
       value = entry.get()
       if value == "":
           error_label.config(text="Пустий рядок! Введіть число від 1 до 4.")
       elif not (1 <= int(value) <= 4):
           error_label.config(text="Число повинно бути від 1 до 4!")
       else:
           error_label.config(text="")
           t.hideturtle()     
           t.clear()          

           if(int(value)<=2):
               koch(int(value)-1,250)

           else:
               for i in range(3):
                   koch(int(value)-1,250)
                   t.right(120)
               
           t.penup()          
           t.home()           
           t.pendown() 
       
    button = tk.Button(top,text="Натиснути",command=Exception)
    button.pack(pady=6)


def triangle_Serpynsky_draw():
    top = tk.Toplevel(root)
    top.title("Трикутник Серпіньского")
    top.geometry("250x150")

    lable = tk.Label(top,text="Вкажіть від 1 до 4 ")
    lable.pack(pady=2)

    entry = tk.Entry(top,width=1,validate="key") # Введення зміної entry
    vcmd = (top.register(is_number),'%S') # Перевірка на цифру
    entry.config(validate="key",validatecommand=vcmd)
    entry.pack(pady=5)

    error_label = tk.Label(top,text="",fg="red")
    error_label.pack(pady=7)

    def Exception():
       value = entry.get()
       if value == "":
           error_label.config(text="Пустий рядок! Введіть число від 1 до 4.")
       elif not (1 <= int(value) <= 4):
           error_label.config(text="Число повинно бути від 1 до 4!")
       else:
           error_label.config(text="")
           t.hideturtle()     
           t.clear()          

           if(int(value)==1):
               triangle(200)

           else:
               sierpinski_triangle(400,int(value))
               
           t.penup()          
           t.home()           
           t.pendown() 
       
    button = tk.Button(top,text="Натиснути",command=Exception)
    button.pack(pady=6)
           
# def 

def Snowflake_2_draw():
    top = tk.Toplevel(root)
    top.title("Сніжинка_2")
    top.geometry("250x150")

    lable = tk.Label(top,text="Вкажіть від 1 до 4 ")
    lable.pack(pady=2)

    entry = tk.Entry(top,width=1,validate="key") # Введення зміної entry
    vcmd = (top.register(is_number),'%S') # Перевірка на цифру
    entry.config(validate="key",validatecommand=vcmd)
    entry.pack(pady=5)

    error_label = tk.Label(top,text="",fg="red")
    error_label.pack(pady=7)

    def Exception():
       value = entry.get()
       if value == "":
           error_label.config(text="Пустий рядок! Введіть число від 1 до 4.")
       elif not (1 <= int(value) <= 4):
           error_label.config(text="Число повинно бути від 1 до 4!")
       else:
           error_label.config(text="")
           t.hideturtle()     
           t.clear()          

           snowflake(int(value),200)
               
           t.penup()          
           t.home()           
           t.pendown() 
       
    button = tk.Button(top,text="Натиснути",command=Exception)
    button.pack(pady=6)

root = tk.Tk()
root.title("Вибір Фігур")
root.geometry("300x350")
root.resizable(False, False)



# icon = tk.PhotoImage(file="c:\\Users\\david\\OneDrive\\Рабочий стол\\Пайтон_малюнки\\images\\pngwing.com (1).png") # іконка для верхнього меню
# root.iconphoto(False, icon) # створює ікноку у лівому верхньому куту

frame = ttk.Frame(root, padding=(1, 1, 12, 12))
frame.pack(expand=True)

# Центральна назва
Hint = ttk.Label(frame, text="Вибір фігур", font=("Arial", 16))
Hint.pack(pady=(10, 25))  # верхній і нижній відступ

# Кнопки меню
btn1 = ttk.Button(frame, text="Пилюка Кантора",command=Cantor_dust_draw)
btn1.pack(fill="x", pady=10)

btn2 = ttk.Button(frame, text="Сніжинка Коха",command=Kochs_Snowflake_draw)
btn2.pack(fill="x", pady=10)

btn3 = ttk.Button(frame, text="Трикутник Серпінського",command=triangle_Serpynsky_draw)
btn3.pack(fill="x", pady=10)

btn4 = ttk.Button(frame,text="Сніжинка 2",command=Snowflake_2_draw)
btn4.pack(fill="x", pady=10) # fill x - розтягнення віджета по ікс

root.mainloop()