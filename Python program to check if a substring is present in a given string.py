import re
string_1=str(input("enter the first string:"))
string_2=str(input("enter the second string:"))
if (re.search(string_2,string_1)):
  print("YES,string '{0}' is present in string '{1}' " .format(string_2,string_1))
else:
  print("NO,string '{0}' is not present in string {1} " .format(string_2,string_1) )  

