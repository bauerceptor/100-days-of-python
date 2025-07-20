import tkinter

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas["bg"] = YELLOW
    title_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps in (1, 3, 5, 7):
        count_down(WORK_MIN * 60)
        title_label.config(text="Work")
    elif reps in (2, 4, 6):
        break_ui()
        count_down(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        break_ui()
        count_down(LONG_BREAK_MIN * 60)
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    if minutes < 10:
        minutes = f"0{minutes}"

    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        global reps
        for _ in range(reps // 2):
            marks += "✅"
        checkmarks_label.config(text=marks)


# --------------------------- MISC FUNCTIONS ---------------------------------- #
def break_ui():
    global reps
    if reps == 8:
        title_label.config(text="Break", fg=RED)
    else:
        title_label.config(text="Break", fg=PINK)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


# Title Label

title_label = tkinter.Label(
    text="Timer", fg=GREEN, font=(FONT_NAME, 40, "normal"), bg=YELLOW
)
title_label.grid(row=0, column=1)

# Setting up Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(
    100, 112, image=tomato_img
)  # x-pos, y-pos, PhotoImage (reads image files)
timer_text = canvas.create_text(
    109, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)

canvas.grid(row=1, column=1)

# calling count_down() function after initiating the canvas

# Start Button
start_btn = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

# Reset Button
reset_btn = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=3)

# Tick Label
checkmarks_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
checkmarks_label.grid(row=3, column=1)


window.mainloop()
