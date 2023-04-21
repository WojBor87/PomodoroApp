from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in [0, 2, 4, 6]:
        count_down(work_sec)
        reps += 1
    elif reps in [1, 3, 5]:
        count_down(short_break_sec)
        reps += 1
    elif reps == 7:
        count_down(long_break_sec)
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count >= 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("The Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=2, row=2)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 45), fg=GREEN)
timer_label.grid(column=2, row=1)
check_label = Label(text="✔", bg=YELLOW, font=(FONT_NAME, 25), fg=GREEN)
check_label.grid(column=2, row=4)
start_button = Button(text="Start", bg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", bg=GREEN, highlightthickness=0)
reset_button.grid(column=3, row=3)

window.mainloop()
