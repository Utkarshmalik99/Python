n=int(input("enter the n'th natural number:"))

def squareSum(n):
  sum=0
  for n in range(1,n+1):
    sum+=(n*n)
  return sum

print("Sum of squares of first n entered natural numbers is",squaresum(n))


