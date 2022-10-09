lower = int(input("Please enter lower limit: "))
upper = int(input("Please enter upper limit: "))
num1 = int(input("num to be divided pls enter that one: "))

for i in range(lower, upper+1):
    if(i%num1==0):
        print(i)