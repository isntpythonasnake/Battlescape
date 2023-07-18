#########
# PSB BATTLE GAME
# CREATED BY:
# # 1. isntpythonasnake
##########

# IMPORT ALL PACKAGES & MODULES
import random
from datetime import datetime
import characters as char
import logging as log
import asciiart

# SET VARIABLES
player_units = []
ai_units = []
ai_names = 'AI_'
game_over = False
pl_gold = 0
ai_gold = 0
rounds = 1

asciiart.intro()  # PRINTS AN ASCII ART AND CREDITS FROM INTRO MODULE

# GET CURRENT TIME
time = datetime.now()
dt = time.strftime('%d-%m-%y %H_%M_%S')
# CREATE A LOG FILE EACH STARTUP WITH CURRENT TIME IN LOG FILE NAME
log.basicConfig(filename=f'logs/log-{dt}.txt',
                level=log.INFO,
                format='%(asctime)-8s : %(levelname)-5s : %(message)s',
                datefmt='%d-%m-%y %H:%M',
                filemode='w')


# LOGS TO LOGS/LOG.TXT FOR EVENT LOG REQUIREMENT
def to_log(logs):
    log.info(f'{logs}')


# DISPLAYS UPDATED UNITS LIST WHEN CALLED
def update_list():
    print('==============')  # DIVIDER
    print('YOUR UNITS:')
    for i, e in enumerate(player_units):
        print(f'[{i + 1}] 🟢 {e.class_type} | {e.class_name} :: Health: {e.hp}, Attack: {e.at}, '
              f'Defence: {e.df}, EXP: {e.xp}, Level: {e.lv}')
        to_log(f'[{i + 1}]{e.class_type} | {e.class_name} :: Health: {e.hp}, Attack: {e.at}, '
               f'Defence: {e.df}, EXP: {e.xp}, Level: {e.lv}')

    print('AI UNITS:')
    for i, e in enumerate(ai_units):
        print(f'[{i + 1}] 🔴 {e.class_type} | {e.class_name} :: Health: {e.hp}, Attack: {e.at}, '
              f'Defence: {e.df}, EXP: {e.xp}, Level: {e.lv}')
        to_log(f'[{i + 1}] {e.class_type} | {e.class_name} :: Health: {e.hp}, Attack: {e.at}, '
               f'Defence: {e.df}, EXP: {e.xp}, Level: {e.lv}')


# SETS GOLD EARNED FOR UNIT IF IT ATTACKS
def gold(unit, target):
    global ai_gold, pl_gold

    income1 = unit.dmg * 5  # ADDS GOLD 5*SELF DMG TO SELF
    income2 = target.df * 3  # ADDS GOLD 3*TARGET DEFENSE TO TARGET

    if ai_names in unit.class_name:
        ai_gold += income1
        pl_gold += income2

        print(f'AI GOLD EARNED: {income1}🪙. AI GOLD BALANCE: {ai_gold}🪙')
        to_log(f'AI GOLD EARNED: {income1}. AI GOLD BALANCE: {ai_gold}')
        print(f'PLAYER GOLD EARNED: {income2}🪙. PLAYER GOLD BALANCE: {pl_gold}🪙')
        to_log(f'PLAYER GOLD EARNED: {income2}. PLAYER GOLD BALANCE: {pl_gold}')

    else:
        ai_gold += income2
        pl_gold += income1

        print(f'AI GOLD EARNED: {income2}🪙. AI GOLD BALANCE: {ai_gold}🪙')
        to_log(f'AI GOLD EARNED: {income2}. AI GOLD BALANCE: {ai_gold}')
        print(f'PLAYER GOLD EARNED: {income1}🪙. PLAYER GOLD BALANCE: {pl_gold}🪙')
        to_log(f'PLAYER GOLD EARNED: {income1}. PLAYER GOLD BALANCE: {pl_gold}')


# SETS GOLD EARNED FOR ATTACKER UNIT IF TARGET DIES
def gold_dead(unit):
    global pl_gold, ai_gold

    income1 = unit.dmg * 7

    if ai_names in unit.class_name:
        ai_gold += income1

        print(f'GOLD EARNED: {income1}🪙. GOLD BALANCE: {ai_gold}🪙')
        to_log(f'GOLD EARNED: {income1}. GOLD BALANCE: {ai_gold}')
    else:
        pl_gold += income1

        print(f'GOLD EARNED: {income1}🪙. GOLD BALANCE: {pl_gold}🪙')
        to_log(f'GOLD EARNED: {income1}. GOLD BALANCE: {pl_gold}')


# MAIN FUNCTION
def main():
    global pl_gold, ai_gold, rounds  # GETS GLOBAL VARIABLES
    print('ENTER YOUR CHARACTER CHOICES!')
    print('==============')  # DIVIDER
    # SETUP PLAYER UNITS
    for i in range(3):
        while True:
            char_type = input(f'Unit {i + 1}: Enter unit type [w/t]: ')
            char_name = input(f'Unit {i + 1}: Enter unit name: ')
            print(f'---')
            if char_type.lower() not in ['w', 't'] or char_type == '' or char_name == '':
                print('Invalid input! Please enter either \'w\' or \'t\'!')
            else:
                to_log(f'User chose :: Unit Type: {char_type}, Unit Name: {char_name}')
                unit1 = char.Characters(char_type, char_name)
                player_units.append(unit1)
                break

    # SETUP AI UNITS
    for i in range(3):
        char_type = random.choice(['w', 't'])
        char_name = str(ai_names) + str(random.randint(1, 10))
        to_log(f'AI chose :: Unit Type: {char_type}, Unit Name: {char_name}')
        ai1 = char.Characters(char_type, char_name)
        ai_units.append(ai1)

    update_list()  # CALLS THE UPDATE_LIST() FUNCTION ABOVE TO UPDATE AND DISPLAY ALL UNITS

    # MAIN GAME LOOP
    while not game_over:

        if not player_units:  # CHECKS IF ALL PLAYER UNITS HAVE BEEN KILLED
            print('💀 ALL YOUR UNITS HAVE BEEN DEFEATED! YOU LOST!')
            to_log('All of user\'s units have been killed. User has lost the game.')
            asciiart.lose()
            print('||=====================||')
            asciiart.ending()
            break  # BREAKS THE LOOP AND ENDS THE GAME

        if not ai_units:  # CHECKS IF ALL AI UNITS HAVE BEEN DEFEATED
            print('💀 ALL ENEMIES HAVE BEEN DEFEATED! YOU WON THE GAME!')
            to_log('All enemies were defeated. User has won the game!')
            asciiart.win()
            print('||=====================||')
            asciiart.ending()
            break  # BREAKS THE LOOP AND ENDS THE GAME

        if rounds % 2 == 1:  # PLAYER ROUNDS
            print('==============')  # DIVIDER
            print(f'ROUND {int(rounds / 2 + 1)}')  # DISPLAYS ROUNDS PER ROUND
            print(f'YOUR GOLD: {pl_gold}🪙')  # DISPLAYS PLAYER TEAM'S GOLD
            to_log(f'USER GOLD: {pl_gold}')  # DISPLAYS PLAYER TEAM'S GOLD
            choice1 = input('⚔ Enter unit to use [1-3]: ')
            choice2 = input('⚔ Enter AI unit to attack [1-3]: ')
            if not choice1.isdigit() or not choice2.isdigit():  # CHECKS IF CHOICE1 OR CHOICE2 IS NOT AN INT
                print("❌ Invalid choice. Please enter a value between 1 and 3.")
            else:  # IF BOTH ARE INTS
                to_log(f'User chose :: Player Unit: {choice1}, AI Unit: {choice2}')  # TO EVENT LOG
                choice1 = int(choice1)  # CONVERTS BOTH CHOICE1 AND 2 INTO INT
                choice2 = int(choice2)
                if 0 <= choice1 <= 3 and 0 <= choice2 <= 3:  # AS INDEXES START AT 0
                    choice1 -= 1
                    choice2 -= 1
                    # CHECKS IF PLAYER INPUT IS LESS THAN THE AMOUNT IN THE LIST
                    if 0 <= choice2 < len(ai_units) and 0 <= choice1 < len(player_units):
                        # CHECKS IF USER INPUT IS MORE THAN AMOUNT IN LIST
                        if choice2 > len(ai_units) and choice1 > len(player_units):
                            print("❌ Invalid choice. Please enter a value between 1 and 3.")
                            to_log("Invalid choice. Please enter a value between 1 and 3.")
                        else:  # CHECKS IF NONE OF THE CONDITIONS ARE MET ABOVE
                            pl_choice = player_units[choice1]
                            ai_choice = ai_units[choice2]
                            pl_choice.attack(ai_choice)  # CREATES INSTANCE OF PLAYER AS SELF AND AI AS TARGET
                            gold(pl_choice, ai_choice)  # CALLS GOLD() ABOVE
                            print(f'🗡️ YOUR UNIT [{pl_choice.class_type} | {pl_choice.class_name}] ATTACKED '
                                  f'[{ai_choice.class_type} | {ai_choice.class_name}] AND DEALT '
                                  f'{pl_choice.dmg} DAMAGE!')
                            to_log(f'YOUR UNIT [{pl_choice.class_type} | {pl_choice.class_name}] ATTACKED '
                                   f'[{ai_choice.class_type} | {ai_choice.class_name}] AND DEALT '
                                   f'{pl_choice.dmg} DAMAGE!')  # TO EVENT LOG

                            if ai_choice.dead:  # CHECKS IF TARGET IS DEAD
                                print('==============')  # DIVIDER
                                print(f'💀 AI UNIT: [{ai_choice.class_type} | {ai_choice.class_name}] HAS BEEN DEFEATED!')
                                # TO EVENT LOG
                                to_log(f'AI UNIT: [{ai_choice.class_type} | {ai_choice.class_name}] HAS BEEN DEFEATED!')
                                gold_dead(pl_choice)  # CALLS GOLD_DEAD_PL() ABOVE
                                ai_units.pop(choice2)  # REMOVES THE TARGET FROM THE LIST SO IT DOESN'T DISPLAY

                            if pl_choice.hp < 25:  # CHECKS IF PLAYER UNIT IS LESS THAN 25
                                heal_input = input("💊 WOULD YOU LIKE TO HEAL YOUR UNIT FOR 200 GOLD? (Y/N): ")
                                if heal_input.lower() == 'y' and pl_gold >= 200:  # CHECKS IF INPUT IS Y AND GOLD IS MET
                                    pl_gold -= 200  # DEDUCTS GOLD FROM PLAYER
                                    pl_choice.hp += 50  # ADDS HP TO PLAYER'S SELECTED UNIT
                                    to_log(f'💊 User healed [{pl_choice.class_type} | {pl_choice.class_name}] '
                                           f'for 200 pl_gold! Gold balance: {pl_gold}')  # TO EVENT LOG
                                    print(f'Healed [{pl_choice.class_type} | {pl_choice.class_name}] '
                                          f'for 200 pl_gold! Gold balance: {pl_gold}')
                                elif pl_gold < 200:  # CHECKS IF PLAYER GOLD IS LESS THAN 200
                                    print(f"❌ HEALING CANCELLED. NOT ENOUGH GOLD!!")
                                    to_log(f"Healing cancelled. Not enough gold!")  # TO EVENT LOG
                                else:  # CHECKS IF CONDITIONS ABOVE AREN'T MET
                                    print("❌ HEALING CANCELLED.")
                                    to_log("Healing cancelled.")  # TO EVENT LOG
                else:  # CHECKS IF INDEX DOESN'T START AT 0
                    print("❌ Invalid choice. Please enter a value between 1 and 3.")
                    to_log("Invalid choice. Please enter a value between 1 and 3.")  # TO EVENT LOG

        else:  # AI ROUNDS
            print('==============')  # DIVIDER
            print('RUNNING AI ROUND...')
            ai_auto = random.choice(ai_units)
            pl_auto = random.choice(player_units)
            ai_auto.attack(pl_auto)  # CREATES INSTANCE OF AI AS SELF AND PLAYER AS TARGET
            index = player_units.index(pl_auto)  # AS AI SELECTS FROM A LIST NOT INDEX, SET INDEX TO THE ITEM
            print(f'AI GOLD: {ai_gold}🪙')  # DISPLAYS PLAYER TEAM'S GOLD
            to_log(f'AI GOLD: {ai_gold}')  # DISPLAYS PLAYER TEAM'S GOLD
            gold(ai_auto, pl_auto)  # CALLS GOLD() ABOVE
            print(f'🗡️ AI UNIT [{ai_auto.class_type} | {ai_auto.class_name}] ATTACKED '
                  f'[{pl_auto.class_type} | {pl_auto.class_name}] AND DEALT '
                  f'{ai_auto.dmg} DAMAGE!')
            to_log(f'AI UNIT [{ai_auto.class_type} | {ai_auto.class_name}] ATTACKED '
                   f'[{pl_auto.class_type} | {pl_auto.class_name}] AND DEALT '
                   f'{ai_auto.dmg} DAMAGE!')

            if pl_auto.dead:  # CHECKS IF TARGET PLAYER IS DEAD
                print('==============')  # DIVIDER
                print(f'💀 YOUR UNIT: [{pl_auto.class_type} | {pl_auto.class_name}] HAS BEEN DEFEATED!')
                to_log(f'YOUR UNIT: [{pl_auto.class_type} | {pl_auto.class_name}] HAS BEEN DEFEATED!')
                gold_dead(ai_auto)  # CALLS GOLD_DEAD_AI ABOVE()
                player_units.pop(index)  # REMOVES TARGET PLAYER UNIT

            if ai_auto.hp < 25:  # CHECKS IF SELECTED AI UNIT IS BELOW 25
                auto_selection = random.randint(0, 1)  # SETS A RANDOM VARIABLE. 0 = NO, 1 = YES
                if auto_selection == 1 and ai_gold >= 200: # CHECKS IF VARIABLE = 1 AND GOLD IS MET
                    ai_gold -= 200  # DEDUCT GOLD FROM AI TEAM
                    ai_auto.hp += 50  # ADDS HEALTH TO SELECTED AI UNIT
                    to_log(f'💊 AI HEALED [{ai_auto.class_type} | {ai_auto.class_name}] '
                           f'FOR 200! GOLD BALANCE: {ai_gold}')  # TO EVENT LOG
                    print(f'Healed [{ai_auto.class_type} | {ai_auto.class_name}] '
                          f'for 200! Gold balance: {ai_gold}')
                elif ai_gold < 200:  # CHECKS IF AI TEAM GOLD IS LESS THAN 200
                    to_log(f'❌ AI DOESN\'T HAVE ENOUGH GOLD TO HEAL! GOLD BALANCE: {ai_gold}')  # TO EVENT LOG
                    print(f'AI DOESN\'T HAVE ENOUGH GOLD TO HEAL! GOLD BALANCE: {ai_gold}')
                else:  # CHECKS IF NONE OF THE ABOVE REQUIREMENTS WERE MET
                    to_log(f'❌ AI CANCELLED HEALING! GOLD BALANCE: {ai_gold}')  # TO EVENT LOG
                    print(f'AI CANCELLED HEALING! GOLD BALANCE: {ai_gold}')

            update_list()  # DISPLAYS UPDATED LIST AT THE END OF EACH ROUND
        rounds += 1  # ADDS ROUND NUMBER PER ROUND


main()  # RUNS MAIN FUNCTION
