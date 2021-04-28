'''
A simple Calculator using Tkinter
'''

# importing Tkinter
import tkinter as tk
# importing Grid from tkinter
from tkinter import Grid

# create a Root Window
root = tk.Tk()
# Title for window
root.title('Calculator')
# set minimum size of window
root.wm_minsize(width=500, height=300)


# All buttons
buttons = [
            ['(', ')', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
      ]

# flag variable
flag = False


def back_space():
    '''
    funtion for backspace
    :return: None
    '''
    # delete last number or character
    var.set(var.get()[:-1])


def on_click(char):
    '''
    evaluating expression
    :param char: number on button
    :return: None
    '''
    global flag

    if flag:
        var.set('')
        flag = False

    curent = var.get()

    if char == '=':
        try:
            ans = eval(curent)
        except SyntaxError:
            ans = 'Invaild Input'

        flag = True
        var.set(ans)
    else:
        var.set(curent+char)


# AC (clear) Button
ac = tk.Button(root, text="AC", padx=10, pady=10, fg='#17202A', bg='#E5E8E8', command=lambda: var.set(''))
ac.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
ac.config(font=('times', 15, 'bold'))
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

# Entry Box
var = tk.StringVar()
Entry_box = tk.Entry(root, textvariable=var)
Entry_box.config(font=('Times', 20, 'bold'), width=10)
Entry_box.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)


# Backspace Button
back = tk.Button(root, text="<-", padx=10, pady=10, fg='#17202A', bg='#E5E8E8', command=back_space)
back.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
back.config(font=('times', 20, 'bold'))
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 3, weight=1)

for row in range(1, 6):
    for col in range(0, 4):
        button = tk.Button(root, text=buttons[row-1][col], padx=10, pady=10)
        button.config(font=('times', 15, 'bold'))
        button.config(fg='#17202A', bg='#E5E8E8', command=lambda c=buttons[row-1][col]: on_click(c))

        button.grid(row=row, column=col, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
        Grid.rowconfigure(root, row, weight=1)
        Grid.columnconfigure(root, col, weight=1)


root.mainloop()
