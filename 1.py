import os

while True: # repeat
    os.system("cls") # clear screen
    i=int(input("Initial Investment: $")) # starting amount, can be 0
    r=float(input("Annual percentage yield: (e.g: 8.5): ")) # APY, e.g 8.5% interest per year so 108.5% so x1.085
    p=int(input("Over How Many Years: ")) # time period (in years)
    a=int(input("Reinvestment Amount: (at the end of period) ")) # The amount added to the total at the end of the year (reinvestment)

    record = [i] # value at the end of each year list
    RATE = r/100+1 # converts rate from 8.5% to x1.085
    T = i*RATE # first year
    for x in range(1,p): # repeat
        T=T*RATE+a # Total = (previous total) X (Annual Percentage Yield) + (reinvestment amount)
        record.append(round(T,2)) # add Total to a record, rounded to 2 dp
    T = round(T,2) # Round total to 2 dp

    os.system("cls") # clear screen
    print("TOTAL: ${}".format(T)) # print all variables with context
    print("Initial Investment: ${}".format(i))
    print("Annual Interest Rate: {}%".format(r))
    print("Years: {}".format(p))
    print("After period reinvestment amount: ${}".format(a))
    print("Record: {}".format(record))
    input()

    # this program is a proof of concept and allows me to develop a better version