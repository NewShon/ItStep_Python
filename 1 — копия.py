import random, os

def tutorial():
    print("""Добро пожаловать в игру Кости!
Каждый игрок делает ставку и пытвется угадать
какие выпадут номера костей и их сумму.
Побеждает тот, кто угадал большее количество номеров.
\n\t\tУдачи!!!\n\n""")

def aponent_choice():
    print("Выберите с кем хотите сыграть:\n"+
          "1 - С компьютером\n"+
          "2 - С друзьями\n"+
          "0 - Выход")
    choice = 0
    while choice != 1 and choice !=2:
        choice = int(input("Ваш выбор: "))
    return choice



fuck = 2
while fuck != 0:
    a = random.randint(1,6)
    b = random.randint(1,6)
    total = a+b

    a1 = int(input("Ваша ставка на кость: "))
    b1 = int(input("Ваша ставка на кость: "))
    total1 = int(input("Ваша ставка на сумму костей: "))

    list1 = [a,b,total]
    list2 = [a1,b1,total1]

    print("\nПервая кость - ",a,"\nВторая - ", b,"\nИтого - ",total,"\n")
    for x in list1:
        if x in list2:
            print("Красава, сыграла ставка: ", x)

    while fuck != 1:
        fuck = int(input("Еще раз? 1 - да  0 - нет: "))
    fuck+=1
    #os.system("clear")
