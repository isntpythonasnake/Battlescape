# IMPORT ALL PACKAGES & MODULES
import random


# MAIN CLASS
class Characters:
    def __init__(self, class_type, class_name):  # INITIALISE AN INSTANCE
        self.class_type = class_type
        self.class_name = class_name
        self.hp = 100
        self.at = 0
        self.df = 0
        self.xp = 0
        self.lv = 0
        self.dmg = 0

        if class_type.lower() == 'w':
            self.setup_warrior()
        elif class_type.lower() == 't':
            self.setup_tank()

    def setup_warrior(self):  # SETS UP WARRIOR
        self.at = random.randint(5, 20)
        self.df = random.randint(1, 10)
        self.class_type = 'Warrior'  # AS CHARACTER IS CALLED WITH 'w', SET ACTUAL NAME TO WARRIOR

    def setup_tank(self):  # SETS UP TANK
        self.at = random.randint(1, 10)
        self.df = random.randint(5, 15)
        self.class_type = 'Tank'  # AS CHARACTER IS CALLED WITH 't', SET ACTUAL NAME TO TANK

    def attack(self, target):  # DEFINES ATTACK FUNCTION
        if isinstance(target, Characters):  # CHECKS IF INSTANCE IS CREATED IN MAIN.PY
            dmg = max(0, self.at - target.df + random.randint(-5, 10))  # MATH FOR TARGET DAMAGE
            target.hp -= dmg  # DEDUCTS TARGET HP WITH DAMAGE
            self.dmg = dmg  # SETS DAMAGE AS SELF.DMG SO IT CAN BE REFERENCED IN MAIN.PY
            if target.hp <= 0 and not target.dead:  # IF TARGET HP IS 0, SET TARGET AS DEAD
                target.dead = True
            else:  # CHECKS IF NOT DEAD
                target.dead = False
                target.xp += target.df  # SETS TARGET XP BASED ON TARGET'S DEFENSE VALUE
                self.xp += dmg  # SETS SELF XP BASED ON SELF'S DAMAGE VALUE
                if dmg > 10:  # CHECKS IF SELF DAMAGE IS MORE THAN 10, MULTIPLY BY 1.2 AND ROUND UP TARGET XP
                    target.xp *= 1.2
                    target.xp = round(target.xp)
                elif dmg <= 0:  # CHECKS IF SELF DAMAGE IS MORE THAN AND EQUAL TO 0, MULTIPLY BY 1.5 AND ROUND UP TARGET XP
                    target.xp *= 1.5
                    target.xp = round(target.xp)
                if self.xp >= 100:  # CHECKS IF SELF XP IS MORE THAN 100, LEVEL UP SELF AND REMOVE 100 XP
                    self.lv += 1
                    self.xp -= 100
                    print(f'UNIT {self.class_type} | {self.class_name} LEVELED UP!')
                elif target.xp >= 100:  # CHECKS IF TARGET XP IS MORE THAN 100, LEVEL UP TARGET AND REMOVE 100 XP
                    target.lv += 1
                    target.xp -= 100
                    print(f'UNIT {target.class_type} | {target.class_name} LEVELED UP!')

        else:  # CHECKS IF IT'S NOT AN INSTANCE
            print(f'{target} is invalid for attack.')

