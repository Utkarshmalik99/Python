s=str(input("enter a string:"))

if(s==s[::-1]):
  print("The entered string is a palindrome")
else:
  print("The entered string is not a palindrome")

#In the above program, first take input from the user (using input() method) to check for palindrome.
#Then using slice operation [start:end:step], check whether the string is reversed or not. 
#Here, step value of -1 reverses a string. If yes, it prints a palindrome else, not a palindrome.
