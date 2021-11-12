from tkinter import *  # tkinter library

root = Tk()
root.title("")  # empty title ("tk" by default)

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
    i=int(initial_input.get())
    r=int(rate_input.get())
    p=int(period_input.get())
    a=int(reinvest_input.get())

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
    result3 =Label(text="{}".format(Record)).grid(row=13, column=2)


calculate_button = Button(text="Calculate", command=Calculate).grid(column=2)

root.mainloop()
