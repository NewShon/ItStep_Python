import random, os

name1 = 'Death'
health1 = 100

name2 = "Fury"
health2 = 100

body = ("глову","живот","ноги")

while health1 > 0 and health2 > 0:

    damage1 = random.randint(50, 60)
    damage2 = random.randint(50, 60)

    print(name1,"\n","Health: ",health1)
    print(name2, "\n", "Health: ", health2)

    print("\n",name1)
    print("Куда бить:",
          "\n1 - В голову",
          "\n2 - В живот",
          "\n3 - По ногам")
    hit1 = int(input("Ваш выбор: "))

    print("\nЧто блокировать:",
          "\n1 - Голову",
          "\n2 - Живот",
          "\n3 - Ноги")
    block1 = int(input("Ваш выбор: "))


    print("\n\n",name2)
    hit2 = random.randint(1,3)
    block2 = random.randint(1,3)
    print("Удар в ", body[hit2-1], "\nБлокирует  ", body[block2-1],"\n\n")



    if hit1 != block2:
        print(name1, "Проводит атаку на,", damage1, "урона")
        health2 -= damage1
    else:
        print(name2," блокирует удар")

    if hit2 != block1:
        print(name2, "Проводит атаку на,", damage2, "урона")
        health1 -= damage2
    else:
        print(name1," блокирует удар")
        

    input("\n\nEnter, чтобы продолжить")
    os.system("cls")




print("\n\n",name1,"\n","Health: ",health1)
print(name2, "\n", "Health: ", health2)
if health1 < 0:
    print(name1, "повержен,","победитель",name2)
else:
    print(name2, "повержен,","победитель",name1)


input("Enter")
