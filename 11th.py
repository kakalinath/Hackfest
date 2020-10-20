#Fibo Simple
Limit = input("Enter Limits >> ")
try:
    Limit = int(Limit)
    n1,n2 = 0,1
    count = 0
    if Limit < 0 :
        print("Fibonacci Series is 0 !")
    elif Limit==1:
        print("Fibonacci Series is :", n2)
    else:
        print("Fibonacci Series >> ")
        while count < Limit:
            print(n1)
            next = n1 + n2
            n1 = n2
            n2 = next
            count = count + 1
except:
    print("Stop it and Start Again !")
