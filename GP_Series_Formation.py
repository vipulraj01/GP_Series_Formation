a = int(input("Enter First Term:  "))
b = int(input("Enter Common Ratio: "))
c = int(input("Enter Number of Terms: "))
for i in range(1,c+1):
    Result = a * b**(i-1)
    print(Result)
