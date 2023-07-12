import string
import random

user_input=input("Select code or decode? :")
if user_input=="code":
  code=input("Enter the sentence to code? :")
  if len(code)<4:
    coded=code[::-1]
  else:
     coded=code[::-1]
     res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
     res2 =''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
     print(f"{res}{coded}{res2}")
elif user_input=="decode":
  decode=input("Enter the sentence to de-code? :")
  if len(decode)<4:
    decoded=decode[::-1] 
  else:
    decoded=decode[::-1]
    b=decoded[3:]
    c=b[:-3]
    print(c)

 

