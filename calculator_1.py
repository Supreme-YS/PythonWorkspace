from tkinter import *
from tkinter import ttk
 
operation = ''  
temp_number = 0
answer_trigger = False
 
def button_pressed(value):
    global temp_number
    global answer_trigger
    if value=='AC':
        number_entry.delete(0,'end')
        operation = ''
        answer_trigger = False
        print("AC pressed")
    else:
        if answer_trigger:
            number_entry.delete(0,"end")
            answer_trigger = False
        number_entry.insert("end",value)
        print(value,"pressed")
 
def float_filter(value):
    try:
        int(value)
        return int(value)
    except ValueError:
        return float(value)
 
# 두값이 같으면 정수로 표현가능.==> 정수값으로 반환.
def int_changer(value):
    if int(value) == float(value):
        return int(value)
    else:
        return float(value)
 
def math_button_pressed(value):
    global operation 
    global temp_number
    global answer_trigger
    if not number_entry.get() == '':
        operation = value
        temp_number = float_filter(number_entry.get())
        number_entry.delete(0,'end')
        print(temp_number,operation)
 
def equal_button_pressed():
    global operation
    global temp_number
    global answer_trigger
    if not (operation =='' and number_entry.get()==''):
        number = int(number_entry.get())
        if operation == '/':
            solution = temp_number/number
        elif operation == '*':
            solution = temp_number*number
        elif operation == '+':
            solution = temp_number+number
        else :
            solution = temp_number-number
             
        #int_changer() 함수를 한번 거쳐서, 값저장.
        solution = int_changer(solution)
        number_entry.delete(0,'end')
        number_entry.insert(0,solution)
        print(temp_number,operation,number,"=",solution)
        operation = ''
        temp_number = 0
        answer_trigger = True
         
