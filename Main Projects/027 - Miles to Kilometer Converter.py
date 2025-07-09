import tkinter

window = tkinter.Tk()
window.title('Miles to Kilometers Converter')
window.minsize(width=300, height=150)
window.config(padx=50,pady=50)

# Labels
miles_label = tkinter.Label(text="Miles")
is_equal_label = tkinter.Label(text="is equal to")
output_label = tkinter.Label(text="0")
km_label = tkinter.Label(text="Km")

# Entry
entry = tkinter.Entry(width=7)

def mile_to_km():
    mile_value = float(entry.get())
    km_value = round((mile_value * 1.60934), 2)
    output_label['text'] = km_value

# Button
button = tkinter.Button(text="Calculate", command=mile_to_km)

# Placing Items on Screen    
entry.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
is_equal_label.grid(row=1, column=0)
output_label.grid(row=1, column=1)
km_label.grid(row=1, column=2)
button.grid(row=2, column=1)

window.mainloop()
