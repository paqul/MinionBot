import sys
import csv
import time
import discord
from rolls import roll, roll_bonus_penalty, penalty_bonus_roll_dnd
from rolls import dices, penalty_bonus_dices, penalty_bonus_dices_dnd

list_of_dices = list(range(1, 100))

def handle_response(msg, author, author_id) -> str:
    msg = msg.lower()
    lst_KnownUsers = []
    with open("WelcomedUserIDs.csv", newline="\n") as csvfile_read:
        reader = csv.reader(csvfile_read, delimiter=";")
        for row in reader:
            lst_KnownUsers.append(row[0])
    #Welcome
    hello = ["czesc", "cześć", "czesć", "cześc", "hej", "dzien dobry", "dzień dobry", "dziendob", "yo", "witaj", "witam", "dobry", "siema", "joł", "elo", "czolem", "czołem", "siema", "siemka", "siemano"]
    for hi in hello:
        if msg.startswith(hi) and str(author_id) not in lst_KnownUsers:
            with open("WelcomedUserIDs.csv","a", newline="\n",) as csvfile_write:
                writer = csv.writer(csvfile_write, delimiter=";")
                writer.writerow([str(author_id), str(author)])
            return "W imieniu dyrekcji bardzo serdecznie chciałbym powitać Cię na serwerze Władcy Kości"
        else:
            continue
    #Dices
    if msg[-1] in "ad": #Dnd5 (Dis)Advantage
        if msg[0].isdigit() and (msg[1] == "k") and msg[2:-1].isdigit():
                amount_of_rolls = int(msg[0])
                dice = int(msg[2:-1])
                bonus = msg[-1]
                roll_response = penalty_bonus_roll_dnd(author, amount_of_rolls, dice, bonus)
                return roll_response
        elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k") and msg[3:-1].isdigit():
                amount_of_rolls = int(msg[0] + msg[1])
                dice = int(msg[3:-1])
                bonus = msg[-1]
                roll_response = penalty_bonus_roll_dnd(author, amount_of_rolls, dice, bonus)
                return roll_response
    else: pass #Call of Cthulu BonusPenalty dice
    if msg[-1] in "kp":
        if msg[-2] in "kp" and msg[-3].isdigit(): #dobule bonus/fault dice
            if msg[0].isdigit() and (msg[1] == "k") and msg[2:-2].isdigit():
                amount_of_rolls = int(msg[0])
                dice = int(msg[2:-2])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], True)
                return roll_response
            elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k") and msg[3:-2].isdigit():
                amount_of_rolls = int(msg[0] + msg[1])
                dice = int(msg[3:-2])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], True)
                return roll_response
        elif msg[-2].isdigit(): #normal funciton one bonus of fault dice
            if msg[0].isdigit() and (msg[1] == "k") and msg[2:-1].isdigit():
                amount_of_rolls = int(msg[0])
                dice = int(msg[2:-1])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], False)
                return roll_response
            elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k") and msg[3:-1].isdigit():
                amount_of_rolls = int(msg[0] + msg[1])
                dice = int(msg[3:-1])
                roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, msg[-1], False)
                return roll_response       
        else:
            pass #normal roll
    if msg[0].isdigit() and (msg[1] == "k") and msg[2:].isdigit():
        amount_of_rolls = int(msg[0])
        dice = int(msg[2:])
        roll_response = roll(author, amount_of_rolls, dice)
        return roll_response
    elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k") and msg[3:].isdigit():
        amount_of_rolls = int(msg[0]+msg[1])
        dice = int(msg[3:])
        roll_response = roll(author, amount_of_rolls, dice)
        return roll_response
    #Rest
    elif msg == "help":
        return "Aby uzyskać wynik rzutu kością rzuć np. 1k100, 3k20, 2k10, itp. (zasada poprawnych rzutów: <ilość_kości>k<ilość_ściań_kości>)"
    elif msg == "promotion":
        return "Moje najszczersze gratulacje z okazji awansu! Mam nadzieję że spełnisz się w swojej nowej roli, trzymam kciuki i życzę powodzenia!"
    elif msg == "negative":
        return "Dzień Dobry, Chciałym poinformować, że jesteś osobą która nie jest milie widziana na tym kanale, wobec tego administracja kanału uprasza o nie podejmowanie kolejnych prób dołączenia. Z góry dziękuję, życzę miłego dnia."
    elif msg == "welcome":
        return f"{author} witamy na serwerze 'Władcy Kości'!"
    else:
        pass #do rest


def handle_name_response(name_msg) -> str:
    if name_msg == "<@1055576642254286938> znikaj":
        sys.exit()
    elif name_msg == "<@1055576642254286938> autotest":
        return autotest_feature_positive()      
    else:
        return "Proszę o wybaczanie, aczkolwiek mój zasób usług którę oferuje jest bardzo ograniczony, Przepraszam"
    
#Autotest - Allows to test all current rolls 

roll_amounts = [1,3,10,99]
def autotest_feature_positive() -> str:
    channel = '1099995730518745128'
    channel.message.send(f"Autotest Commencing")
    rollscount = 0
    for current_dice in dices: 
        for current_roll_amount in roll_amounts:
            message = str(str(current_roll_amount) + "k" + str(current_dice))
            rollscount += 1
            time.sleep(2)
            print(message)   
            channel.message.send(f"{message}")
    return channel.message.send(f"Autotest Finished - I have rolled a total of "+ {str(rollscount)} + " rolls")