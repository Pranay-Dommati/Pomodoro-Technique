from tkinter import *
global trick_marks
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
trick_marks = ""
timer_manager = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_manager
    global trick_marks
    global reps
    reps = 0
    trick_marks = ""
    window.after_cancel(timer_manager)
    canvas_timer_text.itemconfig(timer_setup1,text="Timer",font=(FONT_NAME,35,"bold"),fill=GREEN)
    canvas_time.itemconfig(timer_text,text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer(count):
    global reps
    global timer_manager
    min = count // 60
    sec = count % 60
    if sec >= 0 and sec < 10:
        sec = f"0{sec}"
    canvas_time.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer_manager = window.after(1000, timer, count-1)
    else:
        global trick_marks
        if reps % 2 != 0:
            for _ in range((reps//2)+1):
                trick_marks += "✅"
            right_mark_label.config(text=trick_marks, font=(FONT_NAME,10,"bold"))
        start_timer()


def start_timer():
    global reps
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    work_sec = WORK_MIN*60
    if reps % 2 == 0:
        canvas_timer_text.itemconfig(timer_setup1,text="Work",fill=GREEN)
        reps += 1
        timer(work_sec)
    elif reps % 2 != 0 and reps % 7 != 0:
        canvas_timer_text.itemconfig(timer_setup1, text="Break", fill=PINK)
        reps +=1
        timer(short_break_sec)
    else:
        canvas_timer_text.itemconfig(timer_setup1, text="Break", fill=RED)
        reps += 1
        timer(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro time management")
window.config(padx=50,pady=60,bg=YELLOW)

canvas_time = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas_time.create_image(100, 112, image=img)
timer_text = canvas_time.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"),fill="white")
canvas_time.grid(row=1,column=1)

canvas_timer_text = Canvas(height=60,width=300,bg=YELLOW,highlightthickness=0)
timer_setup1 = canvas_timer_text.create_text(150,18,text="Timer",font=(FONT_NAME,35,"bold"),fill=GREEN)
canvas_timer_text.grid(row=0,column=1)

start_button = Button(text="start",command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="reset", command=reset_timer)
reset_button.grid(row=2,column=2)

right_mark_label = Label(fg=GREEN,font=(FONT_NAME,10,"normal"),bg=YELLOW)
right_mark_label.grid(row=3,column=1)







window.mainloop()