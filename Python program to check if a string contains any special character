import re

def check_specialcharacters(test):
  string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')

  if(string_check.search(test) == None): 
        print("String does not contain Special Characters.")
  else:
    print("String contains Special Characters.") 

if __name__ == '__main__':
  test =str(input("enter the string:"))
  check_specialcharacters(test)    
