from tkinter import *

calculator = Tk()
calculator.title("calculator")
calculator.geometry("470x560+600+200")
calculator.configure(bg = "light cyan")
calculator.resizable(False, False)    


frame_result = Frame(calculator, width = 450, height = 50)
frame_result.pack(padx = 10, pady = 20)
frame_pad = Frame(calculator, width = 400, height = 100)
frame_pad.configure(bg = "light cyan")
frame_pad.pack(padx=20, pady=10)


display = Entry(frame_result, width = 11, font = 'helvetica 50', relief = "solid", justify = "right")    #입력창 텍스트 오른쪽 정렬
display.pack()
display.insert(0, "")


press_possible=True
answer_trigger = False

def click(item):   
    global answer_trigger
    current = display.get()
    if answer_trigger:    
        display.delete(0, "end")
        answer_trigger = False
    display.insert("end",item)
        
def press_once(item) :    
    current = display.get()
    global press_possible
    if not (current[(len(current) -1)] == "+"  or current[(len(current) -1)]  == "-" or current[(len(current) -1)] == "*" or current[(len(current) -1)] == "/"):
        display.insert("end", item)
        press_possible = True

def dot_possible():    
    global press_possible
    if(press_possible == True):
        display.insert("end",".")
        press_possible = False

def clear():    
    display.delete(0, "end")

def back():    
    erase = Entry.get(display)
    x = ''    
    for i in range(len(erase) -1):
        x+=erase[i]    
    display.delete(0, "end")   
    display.insert(0, x)    

def equal():    
    global answer_trigger
    answer_trigger = True
    try:
        val = Entry.get(display)
        result = eval(val)
        display.delete(0, "end")
        display.insert(0, round(result, 8))
    except:
        display.delete(0,"end")
        display.insert("end","Zero Division")   


btn_clear = Button(frame_pad, width = 7, height = 2, bg="lavender blush", fg = "salmon", text = "C", font = "helvetica 15 bold", command = clear)
btn_change = Button(frame_pad, width = 7, height = 2, bg="lavender blush", fg = "MediumPurple2", text = "+/-", font = "helvetica 15 bold", command = lambda:click("-"))
btn_back = Button(frame_pad, width = 7, height = 2, bg="lavender blush", fg = "salmon", text = "Back", font = "helvetica 15 bold", command = back)

btn_clear.grid(row = 0, column = 0, sticky=N+E+W+S, padx=7, pady=7)
btn_change.grid(row = 0, column = 1, sticky=N+E+W+S, padx=7, pady=7)
btn_back.grid(row = 0, column = 2, columnspan = 2, sticky=N+E+W+S, padx=7, pady=7)


btn_7 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "7", font = "helvetica 15", command = lambda:click(7))
btn_8 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "8", font = "helvetica 15", command = lambda:click(8))
btn_9 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "9", font = "helvetica 15", command = lambda:click(9))
btn_add = Button(frame_pad, width = 7, height = 2, bg="lavender blush", fg = "MediumPurple2", text = "+", font = "helvetica 15 bold", command = lambda:press_once("+"))

btn_7.grid(row = 1, column = 0, sticky=N+E+W+S, padx=7, pady=7)
btn_8.grid(row = 1, column = 1, sticky=N+E+W+S, padx=7, pady=7)
btn_9.grid(row = 1, column = 2, sticky=N+E+W+S, padx=7, pady=7)
btn_add.grid(row = 1, column = 3, sticky=N+E+W+S, padx=7, pady=7)

btn_4 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "4", font = "helvetica 15", command = lambda:click(4))
btn_5 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "5", font = "helvetica 15", command = lambda:click(5))
btn_6 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "6", font = "helvetica 15", command = lambda:click(6))
btn_substract = Button(frame_pad, width = 7, height = 2, bg="lavender blush", fg = "MediumPurple2", text = "-", font = "helvetica 15 bold", command = lambda:press_once("-"))

btn_4.grid(row = 2, column = 0, sticky=N+E+W+S, padx=7, pady=7)
btn_5.grid(row = 2, column = 1, sticky=N+E+W+S, padx=7, pady=7)
btn_6.grid(row = 2, column = 2, sticky=N+E+W+S, padx=7, pady=7)
btn_substract.grid(row = 2, column = 3, sticky=N+E+W+S, padx=7, pady=7)


btn_1 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "1", font = "helvetica 15", command = lambda:click(1))
btn_2 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "2", font = "helvetica 15", command = lambda:click(2))
btn_3 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "3", font = "helvetica 15", command = lambda:click(3))
btn_mutiply = Button(frame_pad, width = 7, height = 2, bg="lavender blush", fg = "MediumPurple2", text = "X", font = "helvetica 15 bold", command = lambda:press_once("*"))

btn_1.grid(row = 3, column = 0, sticky=N+E+W+S, padx=7, pady=7)
btn_2.grid(row = 3, column = 1, sticky=N+E+W+S, padx=7, pady=7)
btn_3.grid(row = 3, column = 2, sticky=N+E+W+S, padx=7, pady=7)
btn_mutiply.grid(row = 3, column = 3, sticky=N+E+W+S, padx=7, pady=7)


btn_0 = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = "0", font = "helvetica 15", command = lambda:click(0))
btn_dot = Button(frame_pad, width = 7, height = 2, bg = "seashell", fg = "grey29", text = ".", font = "helvetica 15", command = lambda:dot_possible())
btn_equal = Button(frame_pad, width = 7, height = 2, bg="seashell", fg = "grey29", text = "=", font = "helvetica 15 bold", command = equal)
btn_divide = Button(frame_pad, width = 7, height = 2, bg="lavender blush", fg = "MediumPurple2", text = "/", font = "helvetica 15 bold", command = lambda:press_once("/"))

btn_0.grid(row = 4, column = 0, sticky=N+E+W+S, padx=7, pady=7)
btn_dot.grid(row = 4, column = 1, sticky=N+E+W+S, padx=7, pady=7)
btn_equal.grid(row = 4, column = 2, sticky=N+E+W+S, padx=7, pady=7)
btn_divide.grid(row = 4, column = 3, sticky=N+E+W+S, padx=7, pady=7)

calculator.mainloop()