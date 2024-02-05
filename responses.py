from rolls import roll, roll_with_modifier,  roll_bonus_penalty, penalty_bonus_roll_dnd, roll_dnd_stat_block
import sys, time
import csv 

list_of_dices = list(range(1, 100))
dices = [2, 3, 4, 6, 8, 10, 12, 16, 20, 100, 1000]


def handle_response(msg, author, author_id) -> str:
    msg = msg.lower()
    
    #Legacy code for welcoming users on the server on first msg from hello list
    #lst_KnownUsers = []
    #with open("WelcomedUserIDs.csv", newline="\n") as csvfile_read:
        #reader = csv.reader(csvfile_read, delimiter=";")
        #for row in reader:
            #lst_KnownUsers.append(row[0])
    #Welcome
    #hello = ["czesc", "cześć", "czesć", "cześc", "hej", "dzien dobry", "dzień dobry", "dziendob", "yo", "witaj", "witam", "dobry", "siema", "joł", "elo", "czolem", "czołem", "siema", "siemka", "siemano"]
    #for hi in hello:
        #if msg.startswith(hi) and str(author_id) not in lst_KnownUsers:
            #with open("WelcomedUserIDs.csv","a", newline="\n",) as csvfile_write:
                #writer = csv.writer(csvfile_write, delimiter=";")
                #writer.writerow([str(author_id), str(author)])
            #return "W imieniu dyrekcji bardzo serdecznie chciałbym powitać Cię na serwerze Władcy Kości"
        #else:
            #continue
    #Legacy code for welcoming users on the server on first msg from hello list

    #Dices
    if msg[-1] in "ad": #Dnd5 (Dis)Advantage
        if msg[0].isdigit() and (msg[1] == "k" or msg[1] == "d") and msg[2:-1].isdigit():
                amount_of_rolls = int(msg[0])
                dice = int(msg[2:-1])
                bonus = msg[-1]
                roll_response = penalty_bonus_roll_dnd(author, amount_of_rolls, dice, bonus)
                return roll_response
        elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k" or msg[2] == "d") and msg[3:-1].isdigit():
                amount_of_rolls = int(msg[0] + msg[1])
                dice = int(msg[3:-1])
                bonus = msg[-1]
                roll_response = penalty_bonus_roll_dnd(author, amount_of_rolls, dice, bonus)
                return roll_response
    else: pass #Call of Cthulu BonusPenalty dice
    if msg[-1] in "kp":
        if msg[-2] in "kp" and msg[-3].isdigit(): #dobule bonus/fault dice
            if msg[0].isdigit() and (msg[1] == "k" or msg[1] == "d") and msg[2:-2].isdigit():
                amount_of_rolls = int(msg[0])
                dice = int(msg[2:-2])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], True)
                return roll_response
            elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k" or msg[2] == "d") and msg[3:-2].isdigit():
                amount_of_rolls = int(msg[0] + msg[1])
                dice = int(msg[3:-2])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], True)
                return roll_response
        elif msg[-2].isdigit(): #normal funciton one bonus of fault dice
            if msg[0].isdigit() and (msg[1] == "k" or msg[1] == "d") and msg[2:-1].isdigit():
                amount_of_rolls = int(msg[0])
                dice = int(msg[2:-1])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], False)
                return roll_response
            elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k" or msg[2] == "d") and msg[3:-1].isdigit():
                amount_of_rolls = int(msg[0] + msg[1])
                dice = int(msg[3:-1])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], False)
                return roll_response       
        else:
            pass #normal roll
    if "+" in msg or "-" in msg or "*" in msg:
        modifier_type = None
        msg_index_of_modifier = None
        if msg.find("+") != -1:
            msg_index_of_modifier = msg.find("+")
            modifier_type = "+"
        elif msg.find("-") != -1:
            msg_index_of_modifier = msg.find("-")
            modifier_type = "-"
        elif msg.find("*") != -1:
            msg_index_of_modifier = msg.find("*")
            modifier_type = "*"
        if msg[0].isdigit() and (msg[1] == "k" or msg[1] == "d") and msg[2:msg_index_of_modifier].isdigit():
            amount_of_rolls = int(msg[0])
            dice = int(msg[2:msg_index_of_modifier])
            roll_response = roll_with_modifier(author, amount_of_rolls, dice, modifier_type, msg[msg_index_of_modifier+1:])
            return roll_response
        elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k" or msg[2] == "d") and msg[3:msg_index_of_modifier].isdigit():
            amount_of_rolls = int(msg[0] + msg[1])
            dice = int(msg[3:msg_index_of_modifier])
            roll_response = roll_with_modifier(author, amount_of_rolls, dice, modifier_type, msg[msg_index_of_modifier+1:])
            return roll_response
    elif msg[0].isdigit() and (msg[1] == "k" or msg[1] == "d") and msg[2:].isdigit():
        amount_of_rolls = int(msg[0])
        dice = int(msg[2:])
        roll_response = roll(author, amount_of_rolls, dice)
        return roll_response
    elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k" or msg[2] == "d") and msg[3:].isdigit():
        amount_of_rolls = int(msg[0]+msg[1])
        dice = int(msg[3:])
        roll_response = roll(author, amount_of_rolls, dice)
        return roll_response

    elif msg == "autotest":
        # autotest()
        # return autotest()
        time.sleep(2)
        return "1k10"
    elif msg == "midjourney":
        # autotest()
        # return autotest()
        return "/imagine\x0bNight City, city of dreams"
    #Rest
    elif msg == "help":
        return "Aby uzyskać wynik rzutu kością rzuć np. 1k100, 3k20, 2k10, itp. (zasada poprawnych rzutów: <ilość_kości>k<ilość_ściań_kości>) Obecnie wspierane kości [2, 3, 4, 6, 8, 10, 12, 16, 20, 100, 1000]"
    # elif msg == "promotion":
    #     return "Moje najszczersze gratulacje z okazji awansu! Mam nadzieję że spełnisz się w swojej nowej roli, trzymam kciuki i życzę powodzenia!"
    # elif msg == "negative":
    #     return "Dzień Dobry, Chciałym poinformować, że jesteś osobą która nie jest milie widziana na tym kanale, wobec tego administracja kanału uprasza o nie podejmowanie kolejnych prób dołączenia. Z góry dziękuję, życzę miłego dnia."
    # elif msg == "welcome":
    #     return f"{author} witamy na serwerze 'Władcy Kości'!"
    elif msg == "statystyki_dnd":
        return roll_dnd_stat_block(author)
    else:
        pass #do rest


def handle_name_response(name_msg) -> str:
    if name_msg == "<@1055576642254286938> znikaj":
        sys.exit()
    else:
        return "Proszę o wybaczanie, aczkolwiek mój zasób usług którę oferuje jest bardzo ograniczony, Przepraszam"