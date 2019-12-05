# Monster Inc Run file
from monster_inc_class import *

# Code to set user's monster name and skills
monster_name = input('Give a name for a monster:    ')
monster_skills = input('Enter skills for the monster (separate each skill with a comma):    ').strip().split(',')
user_monster = Monster(monster_name, monster_skills)

# Code to execute monster's name
print('#########################MONSTER##INC#########################')
print('\nMONSTER NAME:        ', user_monster.name.upper())
print('--------------------------------------------------------------')
print('MONSTER ATTRIBUTES')
print('--------------------------------------------------------------')
counter = 1
for skill in monster_skills:
    print(' SKILL', counter,':    ', skill)
    counter += 1
print('--------------------------------------------------------------')
print('MONSTER BEHAVIORS')
print('--------------------------------------------------------------')
print(' SLEEPING STYLE:  ', user_monster.sleep())
print(' EATING STYLE:    ', user_monster.eat())
print(' SCARE ATTACK:    ', user_monster.scare_attack())
print('\n#########################MONSTER##INC#########################')