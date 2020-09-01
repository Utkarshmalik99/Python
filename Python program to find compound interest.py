def compoundInterest(p, r, t):
    ci = p * (pow((1 + r / 100), t)) 
    return ci
   
  
p = float(input("Enter the principal amount : "))
 
t = float(input("Enter the number of years : "))
 
r = float(input("Enter the rate of interest : "))
 
#call compound interest
ci =  compoundInterest(p, r, t) 
 
#print
print("Compound interest is: {}".format(ci))
