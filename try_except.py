n=input("Enter a number : ")
def tables(n):
 try:
  for i in range(1,11):
    print(f"{int(n)} X {i} ={int(n)*i}")
 except:
    print(f"The table of {n} is an invalid input ")

    
tables(n)
print("hey! Champ")

exit()
# --------------------
#Zero division error from the python docs
#Docs is always a good solution
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

exit()
# -----------------
#Value error
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

exit()

#Go to docs for other different exceptions
#this was jst try and except practice