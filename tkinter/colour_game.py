import tkinter as tk
from random import shuffle

colors = ['red','green','yellow','purple','gray','cyan','blue','black','orange']
last_color = None
time_out = 30
score = 0
start = False

root = tk.Tk()

color_label = tk.Label(root,text=', '.join(colors),bg='#333333',fg='#eeeeee',font=('Times',15,'bold'))
color_label.pack(side= tk.TOP,fill=tk.X,expand=tk.YES)

time_label = tk.Label(root,text=f'Time Left : {time_out}',width=25)
time_label.config(font= ('courier',15,'bold'),fg='#eeeeee',bg='#333333')
time_label.pack(side=tk.TOP,fill=tk.X,expand=tk.YES)

display_label = tk.Label(root,text='',fg='red',bg='#c0c0c0',width=10)
display_label.config(font=('courier',50,'bold'),borderwidth=5,relief=tk.RAISED)
display_label.pack(side=tk.TOP,expand=tk.YES)

score_label = tk.Label(root,text=f'Your Score : {score}',width=25,height=3)
score_label.config(font=('courier',20,'bold'),bg='#333333',fg='#eeeeee')
score_label.pack(side=tk.TOP,expand=tk.YES)

text_label = tk.Label(root,text='Type your guess color Here',bg='#333333',fg='#eeeeee')
text_label.config(font=('times',15,'bold'))
text_label.pack(side=tk.TOP,expand=tk.YES)

Entry_text = tk.Entry(root,font=('courier',25,'bold'),width=25,fg='#eeeeee',bg='#333333')
Entry_text.pack(side=tk.TOP,expand=tk.YES)

Exit_button = tk.Button(root,text='EXIT',command=root.quit,width=10)
Exit_button.config(font=('Times',20,'bold'),bg='#dddddd',fg='#333333',relief=tk.RAISED)
Exit_button.pack(side=tk.BOTTOM,expand=tk.YES)

def choose_color():
    global last_color
    shuffle(colors)
    if last_color == colors[0]:
        choose_color()
    else:
        last_color = colors[0]
    
def change_color(event):
    global score,start
    start = True
    if Entry_text.get().lower().strip() == colors[0]:
        score += 1
        score_label.config(text=f'Your Score : {score}')
    Entry_text.focus_set()
    Entry_text.delete(0,tk.END)
    choose_color()
    display_label.config(text=colors[1].upper(),fg=colors[0])

def start_timer():
    global time_out,start,score
    if start :
        if time_out:
            time_out -= 1
            time_label.config(text=f'Time Left : {time_out}')
            time_label.update()
            time_label.after(1000,start_timer)
        else :
            display_label.config(text='')
            win = tk.Toplevel(root)
            win.focus()
            win.grab_set()
           
            score_display = tk.Label(win,text=f'Your Final Score is : {score}')
            score_display.config(fg='#dddddd',bg='#333333',height=5,width=20,font=('courier',25,'bold'))
            score_display.pack(fill=tk.BOTH,expand=tk.YES)

            Button_exit = tk.Button(win,text="EXIT",command=win.destroy)
            Button_exit.config(font=('times',15,'bold'),fg='#333333',bg='#dddddd')
            Button_exit.pack(side=tk.BOTTOM,fill=tk.X,expand=tk.YES)

            win.wm_minsize(400,300)
            time_out = 30
            score = 0
            start = False
            start_timer()
    else:
        time_label.after(1000,start_timer)
    
    Entry_text.focus()


start_timer()
root.bind('<Return>',change_color)
root.config(bg='#333333')
root.wm_minsize(600,400)
root.title('COLOR GAME')
root.mainloop()