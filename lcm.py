a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1
    
    
#Take in both the integers and store it in separate variables.
#Find which of the integer among the two is smaller and store it in a separate variable.
#Use a while loop whose condition is always True until break is used.
#Use an if statement to check if both the numbers are divisible by the minimum number and increment otherwise.
#Print the final LCM.
#Exit.
