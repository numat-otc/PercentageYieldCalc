import os

while True:
    os.system("cls")
    i=int(input("Initial Investment: $"))
    r=int(input("Annual Interest Rate (%): "))
    p=int(input("Over How Many Years: "))
    a=int(input("Reinvestment Amount (at the end of period): "))
    f=int(input("Reinvestment Frequency: "))

    os.system("cls")
    RATE = r/100+1
    T = i*RATE
    for x in range(1,p):
        T=T*RATE+a
    T = round(T,2)
    print("TOTAL: ${}".format(T))
    print("Initial Investment: ${}".format(i))
    print("Annual Interest Rate: {}%".format(r))
    print("After period reinvestment amount: ${}".format(a))
    print("reinvestment frequency (per period): {}".format(f))
    input()