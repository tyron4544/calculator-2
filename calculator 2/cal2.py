from functools import partial; from tkinter import *
win = Tk()
result = Label(win, text="0", width=15, font=("Segoe Print", 29), bg="#212f3d", fg="white", anchor="e")
result.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="ew")
row_num, column_num = 1, 0
buttons = ["^", "//", "mod", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", ".", "0", "=", "÷"]
def paa(x):
    text = result.cget("text")
    operators = ["+", "-", "x", "÷", "//", "^", "mod"]
    if x == "C": result.config(text="0")
    elif x == "=":
        try:
            expression = text.replace("^", "**").replace("x", "*").replace("mod","%").replace("÷","/")
            result.config(text=str(eval(expression)))
        except: result.config(text="Error")
    else:
        if text == "0" or text == "Error": text = " "
        if any(text.endswith(op) for op in operators) and x in operators:
            for op in operators:
                if text.endswith(op): text = text[:-len(op)]
            text += x
        else: text += x
        result.config(text=text)
for i in range(len(buttons)):
    Button(win, text=buttons[i], width=6, height=2, font=("Gothic Century", 19), command=partial(paa, buttons[i]), bg="#2c3e50", fg="white").grid(row=row_num, column=column_num)
    column_num += 1
    if column_num == 4: row_num += 1; column_num = 0
win.config(bg="#212f3d"); win.geometry(f"400x463+{int(win.winfo_screenwidth()/2 - 400/2)}+{int(win.winfo_screenheight()/2 - 463/2)}"); win.mainloop()
