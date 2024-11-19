from typing import TextIO

from rolls import roll, bonus_penalty_callofcthulu_roll, dis_advantage_dnd_roll, roll_dnd_stat_block, roll_with_modifier,morkborg_roll , dices
import sys, re
#MSG Variables
dices_imported = str(dices)
sorry_response = (
"Proszę o wybaczenie, ale nie posiadam takiej funkcji. Moje możliwości są ograniczone, przepraszam.\n"
"Po więcej informacji i pomoc, napisz komendę ***help***."
)
help_response = (
    "Aby uzyskać wynik rzutu kością wpisz komendę ***<ilość kości>k<ilość ściań kości>*** (np. *1k100, 3k20, 2k10* itp.).\n"
    "Maksymalna <ilość kości> to 9999.\n"
    "Obecnie wspierane kości ***" + dices_imported + "***.\n"
    "Dostępne Funkcje dodatkowe:\n"
    "- Rzut z modyfikatorem: ***1k10+2-5*** dozwolone działania +,-,*. \n"
    "  Nie wszystkie funkcje obsługują równania, tylko te gdzie ma to sens w zasadach gry.\n"
    "  Nie zapominaj o kolejności wykonywania działań. ;)\n"
    "- Rzut Przewaga/Utrudnienie D&D 5e: ***1k20a*** lub ***1k20d***. Działa również z modyfikatorem.\n"
    "- Rzut Premiowy/Karny Call Of Cthulu: ***1k100p*** lub ***1k100k***.\n"
    "- Podwójny Rzut Premiowy/Karny Call Of Cthulu: ***1k100pp*** lub ***1k100kk***.\n"
    "- Rzut Specjalny k66 Mork Borg: ***1k66*** (rzut 2k6 gdzie jedna kość to dziesiątki a druga jedności).\n"
    "- Rzut na zestaw Statystyk D&D 3e & 5e: ***statystyki_dnd*** - generuje 6 rzutów wg zasady 4k6, odrzucająć najniższy.\n"
    "  Przerzuca cały zestaw jeżeli suma modyfikatorów wynosi 0 lub gdy najwyższy rzut to 13\n"
    "- Pomoc: komenda ***help***."
)
character_limit_response = (
"- Przepraszam ale wynik przekroczył dozwolony limit znaków w wiadomości Discord, więc część rzutów została usunięta.\n"
"Spróbuj zmniejszyć ilość rzutów." + "**"
)
max_amountofrolls_message = (
"Maksymalna <ilość kości> to 9999.\n"
"Po więcej informacji i pomoc, napisz komendę ***help***."
)
import os

import discord
import io

# from rolls import roll, roll_with_modifier,  roll_bonus_penalty, penalty_bonus_roll_dnd, roll_dnd_stat_block
import sys, time
import csv
from OSE.general import *
from OSE.ose_utility_functions import *

list_of_dices = list(range(1, 100))
dices = [2, 3, 4, 6, 8, 10, 12, 16, 20, 100, 1000]


def handle_response(msg, author, author_id) -> TextIO:
    msg = msg.lower()
    roll_response = sorry_response

    #MorkBorg k66 (This needs to be first as its the most specific roll and otherwise would be caught incorrectly by regular roll pattern)
    if re.match(r'(\d+)[kd](66)$', msg):
        morkborg_roll_pattern_match = re.match(r'(\d+)[kd](66)$', msg)
        amount_of_rolls = int(morkborg_roll_pattern_match.group(1))
        if amount_of_rolls > 9999:
            return max_amountofrolls_message
        dice = int(morkborg_roll_pattern_match.group(2))
        roll_response = morkborg_roll(author, amount_of_rolls, dice)

    #Regular Roll Pattern (Keep this after the Mork Borg check to avoid misassignment to this function for morkborg rolls)
    elif re.match(r'(\d+)[kd](\d+)$', msg):
        regular_roll_pattern_match = re.match(r'(\d+)[kd](\d+)$', msg)
        amount_of_rolls = int(regular_roll_pattern_match.group(1))
        if amount_of_rolls > 9999:
            return max_amountofrolls_message
        dice = int(regular_roll_pattern_match.group(2))
        roll_response = roll(author, amount_of_rolls, dice)
    #Roll with Modifier
    elif re.match(r'(\d+)[kd](\d+)([\+\-\*\/])(.*)', msg):
        modifier_roll_pattern_match = re.match(r'(\d+)[kd](\d+)([\+\-\*\/])(.*)', msg)
        amount_of_rolls = int(modifier_roll_pattern_match.group(1))
        if amount_of_rolls > 9999:
            return max_amountofrolls_message
        dice = int(modifier_roll_pattern_match.group(2))
        operator = modifier_roll_pattern_match.group(3)
        equation = modifier_roll_pattern_match.group(4)
        roll_response = roll_with_modifier(author, amount_of_rolls, dice, operator, equation)

    #Advantage/Disadvantage Roll Matching
    elif re.match(r'(\d+)[kd](20)([ad])(?:([\+\-\*\/])(.*))?', msg):
        dnd5_ad_roll_pattern_match = re.match(r'(\d+)[kd](20)([ad])(?:([\+\-\*\/])(.*))?', msg)
        amount_of_rolls = int(dnd5_ad_roll_pattern_match.group(1))
        if amount_of_rolls > 9999:
            return max_amountofrolls_message
        dice = int(dnd5_ad_roll_pattern_match.group(2))
        bonus = dnd5_ad_roll_pattern_match.group(3)
        operator = dnd5_ad_roll_pattern_match.group(4) if dnd5_ad_roll_pattern_match.group(4) else None
        equation = dnd5_ad_roll_pattern_match.group(5) if dnd5_ad_roll_pattern_match.group(5) else None
        roll_response = dis_advantage_dnd_roll(author, amount_of_rolls, dice, bonus, operator, equation)

    # Call of Cthulu BonusPenalty Dice
    elif re.match(r'(\d+)([kd])(\d+)([kp])([kp]?)$', msg):
        callofcthulu_kp_roll_pattern_match = re.match(r'(\d+)([kd])(\d+)([kp])([kp]?)$', msg)
        amount_of_rolls = int(callofcthulu_kp_roll_pattern_match.group(1))
        if amount_of_rolls > 9999:
            return max_amountofrolls_message
        dice = int(callofcthulu_kp_roll_pattern_match.group(3))
        bonus_or_penalty = callofcthulu_kp_roll_pattern_match.group(4)
        double_bonus_or_penalty = callofcthulu_kp_roll_pattern_match.group(5)
        twice = False if not double_bonus_or_penalty else True
        if bonus_or_penalty == double_bonus_or_penalty and twice == True:
            roll_response = bonus_penalty_callofcthulu_roll(author, amount_of_rolls, dice, bonus_or_penalty, twice)
        elif bonus_or_penalty != double_bonus_or_penalty and twice == False:
            roll_response = bonus_penalty_callofcthulu_roll(author, amount_of_rolls, dice, bonus_or_penalty, twice)
        else:
            roll_response = None

    # Truncate if response exceeds character limit
    if roll_response and len(roll_response) > 1999:
        roll_response = roll_response[:1999-(len(character_limit_response))] + " " + character_limit_response
        return roll_response

    # Return response handling for all above
    if roll_response is not None and roll_response != sorry_response:
        return roll_response
    elif msg.startswith("ose"):
        data_stats = []
        file_path_name = None
        files_in_ose = os.listdir(os.path.join(os.getcwd(), "OSE"))
        print("FILES:::::", files_in_ose)
        #### Cearfully to check - sometimes deletes .py_files
        for file_name in files_in_ose:
            name_to_delete = check_if_file_exist(file_name)
            if name_to_delete in files_in_ose:
                os.remove(os.path.join(os.getcwd(), "OSE", name_to_delete))
        ######################################################
        print("Generating...")  # start generating
        if msg.endswith(ose_file_names[0]):
            data_stats = generate_hero()
            # import OSE.randomize_statistics
            # data_stats = OSE.randomize_statistics.generate_full_character()
            file_path_name = "OSE//char_card.csv"
            print("character")
        # elif msg.endswith(ose_file_names[1]):
        #     data_stats = generate_hero(ose_file_names[1])
        #     file_path_name = "OSE//fighter.csv"
        #     print("fighter")
        # elif msg.endswith(ose_file_names[2]):
        #     data_stats = generate_hero(ose_file_names[2])
        #     file_path_name = "OSE//magic_user.csv"
        #     print("magicuser")
        # elif msg.endswith(ose_file_names[3]):
        #     data_stats = generate_hero(ose_file_names[3])
        #     file_path_name = "OSE//thief.csv"
        #     print("thief")
        with open(file_path_name, "a+", encoding="utf-8") as file:
            for text in data_stats:
                file.write(str(text)+"\n")
        data_stats = None
        return file
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
        return help_response
    elif msg == "statystyki_dnd":
        roll_response = roll_dnd_stat_block(author)
        return roll_response
    #Return Sorry message on error or when roll response is set to None
    elif roll_response is None:
        return sorry_response
    else:
        pass #do nothing if previous conditions did not match

def handle_name_response(name_msg,bot_self_mention_string, author) -> str:
    if name_msg == bot_self_mention_string +" znikaj":
        sys.exit()
    else:
        return sorry_response