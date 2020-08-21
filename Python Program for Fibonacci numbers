def fib_recursion(n):
  if n<=1:
    return n
  else:
    return fib_recursion(n-1) + fib_recursion(n-2)

nterms=int(input("enter the number of terms: "))

if nterms<=0:
  print("please enter a positive integer")
else:
  print("fibonacci sequence")
  for i in range(nterms):
    print(fib_recursion(i))
