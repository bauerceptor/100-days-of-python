import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=400, height=250)
window.config(padx=30,pady=40)

# Label
my_label = tkinter.Label(text='A cool label', font=("Courier", 24, "italic"))
my_label.grid(row=0, column=0)

# Custom Function for Button
def button_clicked():
    my_label['text'] = input.get()

# Button
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(row=1, column=1)
new_button = tkinter.Button(text='hello there')
new_button.grid(row=0, column=2)

# Input Box
input = tkinter.Entry()
input.grid(row=2, column=3)
# input_value = input.get()
# print(input_value)

window.mainloop()
