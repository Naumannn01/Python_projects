# print('''Yeah boi star pattern using while loop
# *
# * *
# * * *
# * * * *
# * * * * *
# ''')
def pyramid_while(n):
    a=0;b=1
    while(a<=n):
        while(b<=a-1):
            print("* ",end="")
            b+=1
        print("\r")
        a+=1;b=0
pyramid_while(5)


exit()
# ----------------------------------

# print('''Yeah boi star pattern using recursion (without loops)
# *
# * *
# * * *
# * * * *
# * * * * *
# ''')
#faster than loops 
def pyramid_recursion(n):
    if n==0:
        return
    else:
        pyramid_recursion(n-1)
        print("* "*n)
pyramid_recursion(5)  

exit()
# ----------------------------------
# print('''Yeah boi star pattern using list
# *
# * *
# * * *
# * * * *
# * * * * *
# ''')
def pyramidlist(n):
    myList=[]
    for i in range(1,n+1):
        myList.append("* "*i)
    print("\n".join(myList))
pyramidlist(5)    

exit()
# ----------------------------------
# print('''Yeah boi star pattern using for loops
# *
# * *
# * * *
# * * * *
# * * * * *
# ''')
def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):  
            print("* ",end="")
        print("\r") 
pyramid(5)


    