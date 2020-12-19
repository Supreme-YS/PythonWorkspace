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
 
