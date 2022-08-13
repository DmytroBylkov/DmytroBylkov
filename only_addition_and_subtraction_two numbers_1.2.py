import time
import tkinter as tk
import random
"""
Ця версія відрізняється від попередніх тим, що при переході кількості балів за 10, 20 змінюються числа
0-10 балів числа 10-90 та 0-10
11-20 балів числа 20-80 та 10-20
більше 20 балів числа 30-70 та 20-30 

також на даний момент відключив кнопку перемикання приклада на наступний, вони перемикаються тільки при натисканні "="
при цьому перевіряється рішення та при вірному рішенні додається 1 бал, при невірному віднімається 3 бали

Ця версія також недороблена, так як не встигає показати правильне чи ні рішення, також планується додати мелодію
"""

def calculate(operation):
    """
    Функція для обробки подій, поки в ній погано розуміюся
    """
    global formula, result, count, symbol
    
    if operation == "C":
        formula = formula[0:-1]
    elif operation == "=":
        if symbol == "+":
            if formula == str(number + number2):
                result = "Вірно"               
                count = count + 1
                #time.sleep(0.5)
                label_text7.configure(text=count)
                #label_text5.configure(text=result, fg="green")
                upd_Text()
            else:
                result = "Помилка"  
                #label_text5.configure(text=result, fg="red")            
                count = count - 3
                #time.sleep(0.5)
                label_text7.configure(text=count)
                upd_Text()
        else:
            if formula == str(number - number2):
                result = "Вірно"
                #label_text5.configure(text=result, fg="green")
                count = count + 1
                #time.sleep(0.5)
                label_text7.configure(text=count)
                upd_Text()
            else:
                result = "Помилка" 
                #label_text5.configure(text=result, fg="red")
                count = count - 3
                #time.sleep(0.5)
                label_text7.configure(text=count)
                upd_Text()
    else:
        if formula == "0":
            formula = ""
        formula += operation
    label_text4.configure(text=formula)

    if result == "Вірно":
        label_text5.configure(text=result, fg="green")
        
    else:
        label_text5.configure(text=result, fg="red")

        

def symbol():
    """
    Функція випадково надає знак для дії для прикладів + чи -
    """
    symbols = ["+", "-"]
    symbol = symbols[random.randint(0, 1)]
    return symbol

def rand_number1():
    """
    Функція надає перше число для прикладів
    """
    global count
    if count < 10:
        num = random.randint(10, 90)
    elif count < 20:
        num = random.randint(20, 80)
    else:
        num = random.randint(30, 70)
    return num

def rand_number2():
    """
    Функція надає друге число для прикладів, воно має бути не більше за перше число,щоб у разі дії віднімання результат був не менше 0
    """
    global count
    if count < 10:
        num2 = random.randint(0, 10)
    elif count < 20:
        num2 = random.randint(10, 20)
    else:
        num2 = random.randint(20, 30)
    return num2

def upd_Text():
    """
    Функція для кнопки "Наступний приклад", оновлює перше та друге число, знак дії та очищує поле вводу і поле оцінювання відповіді
    """
    global number, number2, result, formula, count, symbol
    number = rand_number1()
    number2 = rand_number2()
    
    label_text1.config(text=number)
    label_text3.config(text=number2)
    result = ""
    formula = "0"
    label_text4.config(text="0")
    label_text5.config(text="")
    
    screen.update_idletasks()


            
#    Основна частина 

screen = tk.Tk() # Створюється вікно програми
screen.title("Programm for trening summary two numbers") # назва програми у верхньому рядку
screen.geometry("1000x800") # розмір екрану програми
screen.resizable(False,False) # це робить неможливим зміну розміру вікна програми
screen.configure(bg="lightGray") # встановлюється фон вікна




#Створення чисел та знаку дії для подальшого відображення
count = 0
number = rand_number1()
number2 = rand_number2()

symbol = symbol()

#поле відображення першого числа
label_text1 = tk.Label(text=number, font=("Roboto", 50, "bold"), bg="lightGray", fg="green")
label_text1.place(x=375, y=100)

#поле відображення символу
label_text2 = tk.Label(text=symbol, font=("Roboto", 50, "bold"), bg="lightGray", fg="green")
label_text2.place(x=475, y=100)

#поле відображення другого числа
label_text3 = tk.Label(text=number2, font=("Roboto", 50, "bold"), bg="lightGray", fg="green")
label_text3.place(x=545, y=100)

#створення поля вводу відповідей
formula = "0"
label_text4 = tk.Label(text=formula, font=("Roboto", 50, "bold"), bg="Gray", fg="black", width=5)
label_text4.place(x=400, y=250)

#створення поля ввиводу результату
result = ""
label_text5 = tk.Label(text=result, font=("Roboto", 50, "bold"), bg="lightGray", fg="green", width=7)
label_text5.place(x=350, y=350)

#Поля для назви "Балли" та їх відображення
#count = 0
label_text6 = tk.Label(text="Балли", font=("Roboto", 20,), bg="lightGray").place(x=70,y=70)
label_text7 = tk.Label(text=count, font=("Roboto", 20,), bg="lightGray")
label_text7.place(x=100,y=100)

#Створення кнопок
buttons = [ "1", "2", "3", "4","5", "6", "7","8", "9", "0", "=","C"]

x= 70  # координата верхнього лівого кута першої кнопки
y = 540 # коодината верхнього лівого кута першої кнопки

for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button, bg= "lightBlue", font=("Roboto", 20), command=get_lbl).place(x=x, y=y, width=200, height=50)
    x += 220 # для створення наступної кнопки збільшуємо х на ширину кнопки плюс відступ
    if x > 800: # для переносу кнопок на насупний ряд, коли ряд заповнений
        x = 70 
        y += 70 


#Окрема кнопка для оновлення чисел,що треба рахувати на екрані
#buttons1 = ["Наступний приклад"]

#for button1 in buttons1:
    #get_lbl1 = lambda x=button1: calculate(x)
    #tk.Button(text=button1, bg="lightBlue", font=("Roboto", 20), command=upd_Text).place(x=650, y=70, width=300, height=50)


screen.mainloop() # запуск головного вікна