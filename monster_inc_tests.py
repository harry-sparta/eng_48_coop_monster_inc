from monster_inc_class import *

# T0. Setup for testing monster()
name = 'Paul'
skills = ['scary', 'hairy', 'loud']
monster_1 = Monster(name, skills)

# T1. Test if monster have the right attributes and skills assigned
# T1.1 Test if monster have the right name
print(' T1.1 Test if monster has the right name')
print(' Test results: ', monster_1.name == 'Paul', '    Output:', name)

# T1.2 Test if monster have the right skills
print(' \nT1.1 Test if monster has the right skills')
counter = 0
for skill in skills:
    print(' Test result: ', 'Skill', counter + 1,'.', skill in monster_1.skills, '      Output: ', monster_1.skills[counter])
    counter += 1

# T2. Test if monster can sleep
print(' \nT2. Test if monster can sleep')
print(' Results: ', monster_1.sleep() == 'zzzz', '      Output: ', monster_1.sleep())

# T3. Test if monster can scare_attack
print(' \nT3. Test if monster can scare attack')
print(' Test results: ', monster_1.scare_attack() == 'RAAAHHH', '       Output: ', monster_1.scare_attack())