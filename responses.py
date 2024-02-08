from rolls import roll, roll_bonus_penalty, penalty_bonus_roll_dnd, roll_dnd_stat_block
import sys, re

def handle_response(msg, author, author_id) -> str:
    msg = msg.lower()
    #Regular Roll Patttern
    regular_roll_pattern = r'(\d+)[kd](\d+)$'
    regular_roll_pattern_match = re.match(regular_roll_pattern, msg)
    if regular_roll_pattern_match:
        amount_of_rolls = int(regular_roll_pattern_match.group(1))
        dice = int(regular_roll_pattern_match.group(2))
        roll_response = roll(author, amount_of_rolls, dice)
        return roll_response
    #Advantage/Disadvantage Roll Matching
    dnd5_ad_roll_pattern = r'(\d+)[kd](\d+)[ad]$'
    dnd5_ad_roll_pattern_match = re.match(dnd5_ad_roll_pattern, msg)
    if dnd5_ad_roll_pattern_match:
        amount_of_rolls = int(dnd5_ad_roll_pattern_match.group(1))
        dice = int(dnd5_ad_roll_pattern_match.group(3))
        bonus = dnd5_ad_roll_pattern_match.group(4)
    else:
        return "Aby uzyskać wynik rzutu kością rzuć np. 1k100, 3k20, 2k10, itp. (zasada poprawnych rzutów: <ilość_kości>k<ilość_ściań_kości> lub <ilość_kości>d<ilość_ściań_kości>). Aby modyfikować rzuty dla "
    
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
            pass
    if "+" in msg or "-" in msg or "*" in msg:
        modifier_expression = None
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
        
         #normal roll
    if msg[0].isdigit() and (msg[1] == "k" or msg[1] == "d") and msg[2:].isdigit():
        amount_of_rolls = int(msg[0])
        dice = int(msg[2:])
        roll_response = roll(author, amount_of_rolls, dice)
        return roll_response
    elif msg[0].isdigit() and msg[1].isdigit() and (msg[2] == "k" or msg[2] == "d") and msg[3:].isdigit():
        amount_of_rolls = int(msg[0]+msg[1])
        dice = int(msg[3:])
        roll_response = roll(author, amount_of_rolls, dice)
        return roll_response
    elif msg == "help":
        return "Aby uzyskać wynik rzutu kością rzuć np. 1k100, 3k20, 2k10, itp. (zasada poprawnych rzutów: <ilość_kości>k<ilość_ściań_kości>) Obecnie wspierane kości [2, 3, 4, 6, 8, 10, 12, 16, 20, 100, 1000]"
    elif msg == "statystyki_dnd":
        return roll_dnd_stat_block(author)
    else:
        pass #do rest


def handle_name_response(name_msg) -> str:
    if name_msg == "<@1055576642254286938> znikaj":
        sys.exit()
    else:
        return "Proszę o wybaczanie, aczkolwiek mój zasób usług którę oferuje jest bardzo ograniczony, Przepraszam"