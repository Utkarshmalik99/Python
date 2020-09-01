n=int(input("enter the n'th natural number:"))

def cubesum(n):
  sum=0
  for n in range(1,n+1):
    sum+=(n*n*n)
  return sum

print("Sum of cube of first n entered natural numbers is",cubesum(n))


