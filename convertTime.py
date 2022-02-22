# Python program to create a simple GUI
# weight converter using Tkinter


from tkinter import *

# Create a GUI window
gui = Tk()


# Function to convert time
# given in minute to second, mili second, and hour
def from_minute():
    # convert minute to second
    second = float(e2_value.get()) * 60

    # convert minute to mili second
    mili = float(e2_value.get()) * 60000

    # convert minute to hour
    hour = float(e2_value.get()) * 0.0166666666667

    # Enters the converted time to
    # the text time
    t1.delete("1.0", END)
    t1.insert(END, second)

    t2.delete("1.0", END)
    t2.insert(END, mili)

    t3.delete("1.0", END)
    t3.insert(END, hour)

# set the background colour of GUI window
gui.configure(background="light green")

# set the title of GUI window
gui.title("Conversion time")

# set the configuration of GUI window
gui.geometry("500x130")

# Create the Label times
e1 = Label(gui, text="Enter the time in minute")
e2_value = StringVar()
e2 = Entry(gui, textvariable=e2_value)
e3 = Label(gui, text='Second')
e4 = Label(gui, text='mili Second')
e5 = Label(gui, text='Hour')

# Create the Text times
t1 = Text(gui, height=3, width=20)
t2 = Text(gui, height=3, width=20)
t3 = Text(gui, height=3, width=20)

# Create the Button
b1 = Button(gui, text="Convert", fg='black', bg='red', command=from_minute)

# grid method is used for placing
# the time at respective positions
# in table like structure
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

# Start the GUI
gui.mainloop()
