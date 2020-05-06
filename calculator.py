from tkinter import *
cal = Tk()
cal.title("Calculator")
txt = StringVar()
operator = ""

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    txt.set(operator)
def Clear():
    global operator
    operator = ""
    txt.set("")
def Equal():
    global operator
    result = str(eval(operator))
    txt.set(result)
    operator = ""

display = Entry(cal, width=12, bd=10, fg="black", bg="green", justify='right', font=('Courier New', 25, 'bold'),
                textvariable=txt, insertwidth=5, insertbackground="white").grid(columnspan=5)

leftParenthesis=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text="(", command=lambda:btnClick("(")).grid(row=1, column=0)
rightParenthesis=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text=")", command=lambda:btnClick(")")).grid(row=1, column=1)
percent=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text="%", command=lambda:btnClick('%')).grid(row=1, column=2)
point=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text=".", command=lambda:btnClick(".")).grid(row=1, column=3)

btn7=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="7", command=lambda:btnClick(7)).grid(row=2, column=0)
btn8=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="8", command=lambda:btnClick(8)).grid(row=2, column=1)
btn9=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="9", command=lambda:btnClick(9)).grid(row=2, column=2)
btnAdd=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text="+", command=lambda:btnClick('+')).grid(row=2, column=3)

btn4=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="4", command=lambda:btnClick(4)).grid(row=3, column=0)
btn5=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="5", command=lambda:btnClick(5)).grid(row=3, column=1)
btn6=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="6", command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text="-", command=lambda:btnClick('-')).grid(row=3, column=3)

btn1=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="1", command=lambda:btnClick(1)).grid(row=4, column=0)
btn2=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="2", command=lambda:btnClick(2)).grid(row=4, column=1)
btn3=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="3", command=lambda:btnClick(3)).grid(row=4, column=2)
btnMul=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text="*", command=lambda:btnClick('*')).grid(row=4, column=3)

Clear=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text="C", command = Clear).grid(row=5, column=0)
btn0=Button(cal, height=1, width=3, bd=7, fg="white", bg="black", font=('Courier New', 20, 'bold'),
            text="0", command = lambda:btnClick(0)).grid(row=5, column=1)
Equal=Button(cal, height=1, width=3, bd=7, fg="white", bg="red", font=('Courier New', 20, 'bold'),
            text="=", command = Equal).grid(row=5, column=2)
btnDiv=Button(cal, height=1, width=3, bd=7, fg="white", bg="gray", font=('Courier New', 20, 'bold'),
            text="/", command = lambda:btnClick('/')).grid(row=5, column=3)

cal.mainloop()
