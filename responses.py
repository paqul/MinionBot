from rolls import roll, roll_bonus_penalty, penalty_bonus_roll_dnd
import sys

list_of_dices = list(range(1, 100))
dices = [2, 3, 4, 6, 8, 10, 12, 16, 20, 100, 1000]


def handle_response(msg, author) -> str:
    msg = msg.lower()
    #Welcome
    hello = ["czesc", "cześć", "czesć", "cześc", "hej", "dzien dobry", "dzień dobry", "dziendob", "yo", "witaj", "witam", "dobry"]
    for hi in hello:
        if msg.startswith(hi):
            return "W imieniu dyrekcji bardzo serdecznie chciałbym powitać Cię na serwerze Władcy Kości"
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
    else:
        return "Proszę o wybaczanie, aczkolwiek mój zasób usług którę oferuje jest bardzo ograniczony, Przepraszam"