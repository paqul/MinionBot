from rolls import roll, roll_bonus_penalty, penalty_bonus_roll_dnd, roll_dnd_stat_block, roll_with_modifier, dices 
import sys, re
#MSG Variables
dices_imported = str(dices)
sorry_response = "Proszę o wybaczanie ale nie posiadam takiej funkcji. Mój zasób usług jest ograniczony, przepraszam. Po wiecej informacji i pomoc napisz komendę help"
help_response = "Aby uzyskać wynik rzutu kością rzuć np. 1k100, 3k20, 2k10, itp. (zasada poprawnych rzutów: <ilość_kości>k<ilość_ściań_kości>) Obecnie wspierane kości" + dices_imported + ".\nDostępne Funkcje dodatkowe:\n- Rzut Przewaga/Utrudnienie D&D 5e: 1k20a lub 1k20d\n- Rzut Premiowy/Karny Call Of Cthulu: 1k100p lub 1k100k\n- Podwójny Rzut Premiowy/Karny Call Of Cthulu: 1k100pp lub 1k100kk\n- Rzut do Statystyk D&D 3e & 5e: statyki_dnd"
#Add limiter for lenght to 2000 char.
def handle_response(msg, author, author_id) -> str:
    msg = msg.lower()
    roll_response = None
    #Regular Roll Patttern
    regular_roll_pattern = r'(\d+)[kd](\d+)$'
    regular_roll_pattern_match = re.match(regular_roll_pattern, msg)
    if regular_roll_pattern_match:
        amount_of_rolls = int(regular_roll_pattern_match.group(1))
        dice = int(regular_roll_pattern_match.group(2))
        roll_response = roll(author, amount_of_rolls, dice)
    #Roll with Modifier
    modifier_roll_pattern = r'(\d+)[kd](\d+)([\+\-\*])(.*)'
    modifier_roll_pattern_match = re.match(modifier_roll_pattern, msg)
    if modifier_roll_pattern_match:
        amount_of_rolls = int(modifier_roll_pattern_match.group(1))
        dice = int(modifier_roll_pattern_match.group(2))
        operator = modifier_roll_pattern_match.group(3)
        equation = modifier_roll_pattern_match.group(4)
        roll_response = roll_with_modifier(author, amount_of_rolls, dice, operator, equation)
    #Advantage/Disadvantage Roll Matching
    dnd5_ad_roll_pattern = r'(\d+)[kd](20)([ad])$'
    dnd5_ad_roll_pattern_match = re.match(dnd5_ad_roll_pattern, msg)
    if dnd5_ad_roll_pattern_match:
        amount_of_rolls = int(dnd5_ad_roll_pattern_match.group(1))
        dice = int(dnd5_ad_roll_pattern_match.group(2))
        bonus = dnd5_ad_roll_pattern_match.group(3)
        roll_response = penalty_bonus_roll_dnd(author, amount_of_rolls, dice, bonus)
    # Call of Cthulu BonusPenalty Dice
    callofcthulu_kp_roll_pattern = r'(\d+)([kd])(\d+)([kp])([kp]?)$'
    callofcthulu_kp_roll_pattern_match = re.match(callofcthulu_kp_roll_pattern, msg)
    if callofcthulu_kp_roll_pattern_match:
        amount_of_rolls = int(callofcthulu_kp_roll_pattern_match.group(1))
        dice = int(callofcthulu_kp_roll_pattern_match.group(3))
        bonus_or_penalty = callofcthulu_kp_roll_pattern_match.group(4)
        double_bonus_or_penalty = callofcthulu_kp_roll_pattern_match.group(5)
        double = False if not double_bonus_or_penalty else True
        roll_response = roll_bonus_penalty(author, amount_of_rolls, dice, bonus_or_penalty, double) 
    if roll_response and len(roll_response) > 1999:
        roll_response = roll_response[:1898] +" " + "-" + "Rzut przekroczył dozwolony limit znaków w wiadomości discord, spróbuj zmniejszyć ilość rzutów" + "**" # Truncate and add explanation
        return roll_response 
    if roll_response is not None:
        return roll_response
    elif msg == "help":
        return help_response
    elif msg == "statystyki_dnd":
        roll_response = roll_dnd_stat_block(author)
        return roll_response
    elif roll_response is None:
        return sorry_response
    else:
        pass #do nothing if previous conditions did not match
    
def handle_name_response(name_msg) -> str:
    if name_msg == "<@1055576642254286938> znikaj":
        sys.exit()
    else:
        return sorry_response