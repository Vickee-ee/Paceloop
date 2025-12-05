#to find the factorial of a given number 
num=int(input("Enter the number to find the factorial : "))
count = 1
fact = 1
for i in range(1,num+1):
    fact=fact*count
    count+=1
print("The Factorial of the given number is : ",fact)