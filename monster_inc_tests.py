# from inheritance class import *

# T0. Setup for testing monster()
name = 'Paul'
skills = ['scary', 'hairy', 'loud']
monster(name,skills)

# T1. Test if monster have the right attributes and skills assigned
print(' T1.1 Test if monster has the right name')
print(' Test results:   ', monster.name() == 'Paul', 'Output:   ', name)

print(' \nT1.1 Test if monster has the right skills')
counter = 0
for skill in skills:
    print(' Test result: ','Skill', counter+1, '.   ',skills[counter] in monster.skills())
    counter += 1

# T2. Test if monster can sleep
print(' \nT2. Test if monster can sleep')
print(' Results:   ', monster_1.sleep() == 'zzzz', 'Output: ', monster_1.sleep())

# T3. Test if monster can scare_attack
print(' \nT3. Test if monster can scare attack')
print(' Test results:   ', monster_1.scare_attack() == 'RAAAHHH', 'Ouput:   ', monster_1.scare_attack())