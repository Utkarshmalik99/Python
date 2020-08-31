n=int(input("enter the n'th number:"))
def fibonacci(n):
  if n <= 1:
       return n
  else:
       return(fibonacci(n-1) + fibonacci(n-2))
print("N'th fibonacci number is ",fibonacci(n))    
    
