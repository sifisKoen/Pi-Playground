import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# -------------------------- GLOBAL VARIABLES ----------------------------- #
repetitions = 0
# We create clock_times as a global variable
# Because we need to start and stop the clock
# This process happening in two different functions
# count_down() and reset_timer()
clock_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    window.after_cancel(clock_timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global repetitions
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global repetitions
    repetitions = repetitions + 1

    # Convert timers to seconds because we need to pass them
    # to the count_down function where the count down will start
    working_seconds = WORK_MIN * 60
    short_brake_seconds = SHORT_BREAK_MIN * 60
    long_brake_seconds = LONG_BREAK_MIN * 60

    # Check in which repetition(round) of pomodoro we are
    # and depends the round we start the time
    if repetitions % 2 != 0:
        title_label.config(text="Work Session")
        count_down(working_seconds)
    elif repetitions % 8 == 0:
        title_label.config(text="Long 20min Session", foreground=RED)
        popup_message("Take a large 20 minutes break")
        count_down(long_brake_seconds)
    else:
        title_label.config(text="Short 5min Session", foreground=PINK)
        popup_message("Take a small 5 minutes break")
        count_down(short_brake_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global clock_timer
        clock_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks_user_has = ""
        working_sessions = math.floor(repetitions / 2)
        for sessions in range(working_sessions):
            check_marks_user_has += "✔"
        check_mark.configure(text=check_marks_user_has)

# ---------------------------- POP UP MESSAGE ------------------------------- #


def popup_message(text_message):
    popup = tkinter.Tk()
    popup.wm_title("Break")
    label = tkinter.Label(popup, text=text_message, font=FONT_NAME)
    label.pack(side="top", fill="x", pady=20)
    popup_button = tkinter.Button(popup, text="Okay", command=popup.destroy)
    popup_button.pack()
    # Don't use main loop here will stop the timer


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Reading")
window.config(padx=100, pady=50, background=YELLOW)

# Canvas creation
# We use this highlightthickness=0 for to hide the border of the canvas
# Stack overflow thread https://stackoverflow.com/questions/4310489/how-do-i-remove-the-light-grey-border-around-my-canvas-widget
canvas = tkinter.Canvas(width=200, height=224,
                        background=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# ---------- Label creation ----------

# Timer text label creation
title_label = tkinter.Label(text="Timer", font=(
    FONT_NAME, 35, "bold"), foreground=GREEN, background=YELLOW)
title_label.grid(column=1, row=0)

# Check marks label creation
check_mark = tkinter.Label(foreground=GREEN, background=YELLOW)
check_mark.grid(column=1, row=3)

# ---------- Buttons Creation ----------

# Starting Button Creation
starting_timer_button = tkinter.Button(
    text="Start", highlightthickness=0, command=start_timer)
starting_timer_button.grid(column=0, row=2)

# Reset Button Creation
reset_timer_button = tkinter.Button(
    text="Reset", highlightthickness=0, command=reset_timer)
reset_timer_button.grid(column=2, row=2)

window.mainloop()
