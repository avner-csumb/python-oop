import random

dice_thing_1 = random.randint(1, 6)

dice_thing_2 = random.randint(1, 6)

print(dice_thing_1)
print(dice_thing_2)

if(dice_thing_1 == dice_thing_2):
    print('Doubles! Move {0} spaces and roll again'.format(dice_thing_1 * 2))
else:
    print('Move {0} spaces. Next player\'s turn!'.format(dice_thing_1 + dice_thing_2))
