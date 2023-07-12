questions=[
    ["Which language was used to create facebook? ","Python","French","Javascript","Php","None",4],
["Who is the owner of Twitter? ","Elon","Modi","Mark","Newton","None",1],
["Who is the owner of Threads? ","Elon","Modi","Mark","Newton","None",3],
["Who is the prime minister of India? ","Modi","Putin","Shinde","Manmohan","None",1],
["Who is the prime minister of Russia? ","Modi","Putin","Shinde","Manmohan","None",2],["Which language was used to create facebook? ","Python","French","Javascript","Php","None",4],
["Who is the owner of Twitter? ","Elon","Modi","Mark","Newton","None",1],
["Who is the owner of Threads? ","Elon","Modi","Mark","Newton","None",3],
["Who is the prime minister of India? ","Modi","Putin","Shinde","Manmohan","None",1],
["Who is the prime minister of Russia? ","Modi","Putin","Shinde","Manmohan","None",2],["Who is the owner of Twitter? ","Elon","Modi","Mark","Newton","None",1],
["Who is the owner of Threads? ","Elon","Modi","Mark","Newton","None",3],
["Who is the prime minister of India? ","Modi","Putin","Shinde","Manmohan","None",1],
["Who is the prime minister of Russia? ","Modi","Putin","Shinde","Manmohan","None",2]
]

levels=[1000,2000,3000,5000,10000,20000,30000,50000,100000,200000,300000,500000]
money=0
#iterate the list questions
i=0
for i in range(0,len(questions)): 
    question=questions[i]
    print(f"\n Question for Rs. {levels[i]}-------\n\n{question[0]}")
    print(f"a.{question[1]}           b. {question[2]}")
    print(f"c.{question[3]}           d. {question[4]}")
    reply=int(input("Enter your answer (1-4) :"))
    if (reply==question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if (i==4):
            money=10000
        elif (i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
         print("Wrong answer")
         break
# print(i)
print(f"Your take home money is {money} /-------")


