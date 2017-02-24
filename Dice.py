import random, os



def menu():
    cubes()
    choice = 3
    while choice != 1 and choice != 0:
        choice = int(input("Выш выбор: "))
    os.system("cls")
        
    if choice == 0: exit()
    else: game_with_computer()



def players_list():
    answer = '0'
    while answer != 'y':
        answer = '0'
        people_quantity = int(input("Сколько людей желает принять участие в игре: "))
        while answer != 'y' and answer != 'n':
            answer = input("Вы уверены (y/n): ")
    print("\n")

    players = [] 
    for i in range(1,people_quantity+1):
        print("Введите имя ",i," игрока: ")
        
        name = input()
        cash = 1000
        
        player = [name,cash]
        players.append(player)

    os.system("cls")
    return players



def computers_list():
    answer = '0'
    while answer != 'y':
        enemy_comp = int(input("Cкольки компьютеров будет играть: "))
        while answer != 'y' and answer != 'n':
            answer = input("Вы уверены (y/n): ")
            answer.lower()
    print("\n")

    computers = [] 
    for i in range(1,enemy_comp+1): 
        name = "Компьютер " + str(i)
        cash = 1000
        
        computer = [name,cash]
        computers.append(computer)

    os.system("cls")
    return computers



def throw():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1+die2
    throw_list = [die1, die2, total]

    print("Первая кость - ", throw_list[0],
            "\nВторая кость - ", throw_list[1],
            "\nСумма костей - ", throw_list[2],"\n")
        
    return throw_list    



def player_guess(real_players):
    players_guess = [] #содержит имена и догадки
    bet = 0 #Ставки игроков
    for player in real_players:
        print("\n",player[0], "\nНаличка:", str(player[1])+"$")
        
        while True:#ставка
            bet = int(input("Сколько желаете поставить: "))
            if bet > 0 and bet <= player[1]:
                player[1]-=bet
                break
        
        player_die1 = int(input("\nПервая кость: "))
        player_die2 = int(input("Вторая кость: "))
        player_total = int(input("Сумма костей: "))
            
        guess = (player[0], player_die1, player_die2, player_total,bet)
        players_guess.append(guess)

    return players_guess



def computer_guess(comp_players):
    computers_guess = [] #содержит имена и догадки
    
    for computer in comp_players:
        print("\n",computer[0],"\nНаличка:", str(computer[1])+"$")

        comp_bet = 0
        while True:#ставка
            comp_bet = int((0.05*computer[1])+(0.3*(0.05*computer[1]))+random.randint(-40,30))
            if comp_bet > 0 and comp_bet <= computer[1]:
                print("Ставка:",comp_bet)
                computer[1]-=comp_bet
                print()
                break

        computer_dice = throw()
        
        guess = (computer[0], computer_dice[0], computer_dice[1], computer_dice[2], comp_bet)
        computers_guess.append(guess)

    return computers_guess


    
def tutorial():
    print("""Добро пожаловать в игру Кости!
Каждый игрок делает ставку и пытается угадать
какие выпадут номера костей и их сумму.
Побеждает тот, кто угадал больше всех.
\n\t\tУдачи!!!\n\n""")



def guess_dice(whole_players, random_throw, whole_guess):
    winners = []#сколько угаданных костей у каждого игрока
    for player in range(len(whole_players)):
        counter = 0
        for i in range(3):
            if whole_guess[player][i+1] == random_throw[i]:
                counter+=1
        print(whole_players[player][0], " угадал ", counter, " ставки")
        winners.append(counter)
            
    return winners



def game_with_computer():
    real_players = players_list() #содержит имена и cash
    comp_players = computers_list() #содержит имена и cash

    stop = 2
    while stop != 0:
        os.system("cls")
        tutorial()

        players_guess = player_guess(real_players) #содержит имена, догадки и ставки
        computers_guess = computer_guess(comp_players) #содержит имена, догадки и ставки
        
        input("Для броска нажмите Enter...")
        print("\nПосле броска кости выпали так:")
        random_throw = throw() #содержит бросок
        
        whole_players = real_players + comp_players #содержит все имена и cash
        whole_guess = players_guess + computers_guess #содержит все имена, догадки и ставки

        
        winners = guess_dice(whole_players, random_throw, whole_guess)#сколько угаданных костей у каждого игрока
        
        bets_sum = 0#подсчет общей суммы ставок
        for player in whole_guess:
            bets_sum += player[4]


        winners_bets = 0# подсчет суммы ставок победителей
        winners_list = []#список победителей, по нему будем раздавать выйгрыш
        lose_list = [] #список проигравших
        counter = 0
        for player in whole_guess:
            if 3 in winners:
                if winners[counter] == 3:
                    winners_bets += player[4]
                    player_id = counter#будем возвращать награду по id
                    winners_list.append(player_id)
                else:
                    lose_list.append(counter)
                        
            elif 2 in winners:
                if winners[counter] == 2:
                    winners_bets += player[4]
                    player_id = counter
                    winners_list.append(player_id)
                else: lose_list.append(counter)

            elif 1 in winners:
                if winners[counter] == 1:
                    winners_bets += player[4]
                    player_id = counter
                    winners_list.append(player_id)
                else:
                    lose_list.append(counter)

            else:
                if winners[counter] == 0:
                    winners_bets += player[4]
                    player_id = counter
                    lose_list.append(player_id)

            counter += 1


        #распределение награды для победителей
        lose_sum = bets_sum #подсчет остатка ставок
        counter = 0
        if winners_list:
            for player in range(len(whole_players)):
                if player == winners_list[counter]:
                    award = int(whole_guess[player][4]/winners_bets*bets_sum)
        
                    if award > (whole_guess[player][4]*len(whole_players)):
                        award = (whole_guess[player][4]*len(whole_players))
                                            
                    whole_players[player][1] += award
                    lose_sum -= award
                    counter += 1
                if counter == len(winners_list): break
			
			
	#остаток для проигравших
	if lose_list:
		counter = 0
		for player in range(len(whole_players)):
		    if player == lose_list[counter]:
			award = int(whole_guess[player][4]/bets_sum*lose_sum)

			whole_players[player][1] += award
			counter += 1
		    if counter == len(winners_list): break
        

        #кик проигравших
        for player in real_players:
            if player[1] == 0:
                real_players.remove(player)
                
        for player in comp_players:
            if player[1] == 0:
                comp_players.remove(player)
        
            
        print("\n")
        stop = ''
        while stop != '1' and stop!= '0':
            stop = input("Еще раз? 1 - да  0 - нет: ")
        stop = int(stop)

       
    os.system("cls")
    menu()



def cubes():
    print("x_x\tDICE\tx_x")
    print("\t\t\t\t       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
    print("1 - Играть\t\t\t      ¶¶ ¶               ¶¶")
    print("0 - Выход\t\t\t     ¶¶ ¶                 ¶¶")
    
    print("""\t                            ¶¶   ¶  §§§§    §§§§   ¶¶
                                   ¶¶     ¶  §§§§    §§§§   ¶¶
                                  ¶¶       ¶                 ¶¶
                                 ¶¶         ¶  §§§§    §§§§   ¶¶
                                ¶¶           ¶  §§§§    §§§§   ¶¶
                               ¶¶    §§§§     ¶                 ¶¶
                              ¶     §§§§       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                               ¶¶            ¶¶§§§§     §§§§ ¶¶
                                ¶¶          ¶¶§§§§     §§§§ ¶¶
                                 ¶¶¶¶      ¶¶     §§§§     ¶¶
                             ¶¶¶¶¶¶¶¶¶¶¶  ¶¶     §§§§     ¶¶
                          ¶¶¶¶¶       ¶¶¶¶¶§§§      §§§§ ¶¶
                       ¶¶¶¶¶             ¶¶¶¶§§    §§§§ ¶¶
                     ¶¶¶¶        §§§§        ¶¶¶¶¶¶¶¶¶¶¶¶
                    ¶¶¶           §§§§        ¶¶¶
                    ¶ ¶¶¶¶¶                ¶¶¶¶ ¶
                    ¶     ¶¶¶¶          ¶¶¶¶¶   ¶
                    ¶ §§§§ ¶¶¶¶¶    ¶¶¶¶   §§§§ ¶
                    ¶  §§§§    ¶¶¶¶¶¶¶    §§§§  ¶
                    ¶             ¶¶            ¶
                    ¶             ¶     §§§§    ¶
                    ¶             ¶    §§§§     ¶
                    ¶       §§§§  ¶             ¶
                    ¶¶¶      §ü§§ ¶ §§§§      ¶¶¶
                      ¶¶¶¶        ¶§§§§    ¶¶¶¶¶
                       ¶¶¶¶¶     ¶     ¶¶¶¶¶
                           ¶¶¶¶¶¶ ¶ ¶¶¶¶¶¶
                              ¶¶¶¶¶¶¶¶¶""")

   

menu()












