from tkinter import *  # tkinter library
import os # windows terminal commands

root = Tk()
root.title("")  # empty title ("tk" by default)

# GUI
Label(text="Annual Interest Investment Calculator").grid(column=2) # title

initial_text            = Label(text="Initial investment:").grid(column=2)
initial_input           = Entry(); initial_input.grid(column=2)

rate_text               = Label(text="Annual rate: (e.g 8.5)").grid(column=2)
rate_input              = Entry(); rate_input.grid(column=2)

period_text             = Label(text="Amount of years:").grid(column=2)
period_input            = Entry(); period_input.grid(column=2)

reinvest_text           = Label(text="Reinvestment per year:").grid(column=2)
reinvest_input          = Entry(); reinvest_input.grid(column=2)

# calculate function
def Calculate():
    # check if all variables are valid types
    try:
        i=float(initial_input.get())
        r=float(rate_input.get())
        p=int(period_input.get())
        a=float(reinvest_input.get())
    except:
        os.system('msg "%username%" Error: value(s) invalid, must be a number.')
        return

    #error messages
    if i not in range(1000001): # 0 - 1,000,000
        os.system('msg "%username%" Error: [Initial investment] value invalid, range: (0 - 1,000,000).')
        return
    if r not in range(10001): # 0 - 10,000
        os.system('msg "%username%" Error: [Annual rate] value invalid, range: (0 - 10,000).')
        return
    if p not in range(1,101): # 1 - 100
        os.system('msg "%username%" Error: [Amount of years] value invalid, range: (1 - 100).')
        return
    if a not in range(-100000,100001): # -100,000 - 100,000
        os.system('msg "%username%" Error: [Reinvestment per year] value invalid, range: (-100,000 - 100,000).')
        return

    # same 'algorithm' as in version 1
    Record = [i]
    RATE = r / 100 + 1  # converts rate from 8.5% to x1.085
    T = i * RATE  # first year
    for x in range(1, p):  # repeat
        T = T * RATE + a  # Total = (previous total) X (Annual Percentage Yield) + (reinvestment amount)
        Record.append(round(T, 2))  # add Total to a record, rounded to 2 dp
    T = round(T, 2)  # Round total to 2 dp


    result1 = Label(text="Total: ${}, Over {} years, at an interest of {}%/year".format(T,p,r)).grid(row=11, column=2)
    result2 = Label(text="with an annual reinvestment of {}".format(a)).grid(row=12, column=2)
    result3 =Label(text="History {}".format(Record)).grid(row=13, column=2)


calculate_button = Button(text="Calculate", command=Calculate).grid(column=2)

root.mainloop()
