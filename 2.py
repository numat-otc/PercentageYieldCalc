from tkinter import *  # tkinter library

root = Tk()
root.title("")  # empty title ("tk" by default)

Label(text="Annual Interest Investment Calculator").grid(column=2) # title

initial_text = Label(text="Initial investment:").grid(column=2)
initial_input = Entry().grid(column=2)

rate_text = Label(text="Annual rate: (e.g 8.5)").grid(column=2)
rate_input = Entry().grid(column=2)

period_text = Label(text="Amount of years:").grid(column=2)
period_input = Entry().grid(column=2)

reinvest_text = Label(text="Reinvestment per year:").grid(column=2)
reinvest_input = Entry().grid(column=2)

# calculate function
def Calculate():
    print("TBD")


calculate_button = Button(text="Calculate", command=Calculate).grid(column=2)

root.mainloop()
