import math
def perfect_square(x):
  s=int(math.sqrt(x))
  return s*s==x

n=int(input("enter the number:"))
result1=5*(n*n)+4
result2=5*(n*n)-4

if perfect_square(result1) or perfect_square(result2):
  print(n,"is a fibonacci number")
else:
  print(n,"is not a fibonacci number")
