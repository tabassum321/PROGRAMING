print("                              Solving queueing model M/M/1/∞/∞               ")

x= input("Enter the arrival rate/hour = ")
y= input("Enter the service rate/hour = ")
x = float(x)
y = float(y)
print("The following results for the model is given below : ")
def result():
    row = x/y
    c = 1- row
    lenns = row/c
    lenq = lenns - row
    times = lenns/x
    timeq= lenq/x
    c= "{:.2f}".format(c)
    lenns = "{:.2f}".format(lenns)
    lenq = "{:.2f}".format(lenq)
    times = "{:.2f}".format(times)
    timeq = "{:.2f}".format(timeq)
  
    print("The probability of no person is Po =  ",c)
    print("The length of the system is Ls =  ", lenns)
    print("The length of the queue is  Lq = ", lenq)
    print("The waiting time in the system is Ws(hour) =  ", times)
    print("The waiting time in the queue is  Wq(hour) = ", timeq)

result()

