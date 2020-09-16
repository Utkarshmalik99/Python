a=int(input("enter the lower range:"))
b=int(input("enter the lower range:"))

for num in range(a,b+1):
  if num>1:
    for n in range(2, num):
      # If num is divisible by any number
      # between 2 and val, it is not prime
      if (num % n) == 0:
        break
    else:
         print(num)
