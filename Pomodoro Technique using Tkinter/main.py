from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time_calc = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetter():
    global reps
    window.after_cancel(time_calc)
    canvas.itemconfig(timer, text="00:00")
    my_label.config(text="Timer", font=(FONT_NAME, 30, 'bold'))
    check.config(text="", bg='#F5D5AE')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_action():
    global reps
    reps += 1
    work_s = WORK_MIN * 60
    shortbreak_s = SHORT_BREAK_MIN * 60
    longbreak_s = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        my_label.config(text="Long Break", font=(FONT_NAME, 22, 'bold'), fg='#9C254D')
        counter(longbreak_s)

    elif reps % 2 == 0:
        my_label.config(text="Short Break", font=(FONT_NAME, 22, 'bold'), fg='#5DA7DB')
        counter(shortbreak_s)

    else:
        my_label.config(text="Work", font=(FONT_NAME, 25, 'bold'), fg='#975C8D')
        counter(work_s)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    global time_calc
    min_rem = count // 60
    seconds_rem = count % 60

    if min_rem < 10:
        min_rem = "0" + str(min_rem)
    if seconds_rem < 10:
        seconds_rem = "0" + str(seconds_rem)
    if seconds_rem == 0:
        seconds_rem = "00"
    canvas.itemconfig(timer, text=f"{min_rem}:{seconds_rem}")
    if count > 0:
        time_calc = window.after(1000, counter, count - 1)
    else:
        start_action()
        st = ""
        for _ in range(reps // 2):
            st += '✔'
        check.config(text=st, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.minsize(width=450, height=480)
window.config(padx=80, pady=40, bg='#F5D5AE')
my_label = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), bg="#F5D5AE", fg='#68B984')
my_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg='#F5D5AE', highlightthickness=0)
tom = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tom)
timer = canvas.create_text(102, 128, text='00:00', fill="#FFFBEB", font=(FONT_NAME, 27, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text=" Start ", command=start_action)
start_button.grid(column=0, row=2)
reset_button = Button(text=" Reset ", command=resetter)
reset_button.grid(column=2, row=2)


def checkbutton_used():
    print(checked_state.get())


# text='✔'
check = Label(fg='#5F8D4E', bg='#F5D5AE')
check.grid(column=1, row=3)

window.mainloop()
