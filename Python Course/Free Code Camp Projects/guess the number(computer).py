import random as r

print('---------- GUESS THE NUMBER (1 - 10) ----------')
print('')

r_num = r.randint(1, 10)
i = 1
while i <= 3:
    g_num = int(input('Guess the Number: '))
    if g_num == r_num:
        print(f'YOU WON. THE SECRET NUMBER WAS {r_num}')
        break
    else:
        print('Wrong answer. Try Again!')
        i += 1
else:
    print(f'YOU LOST! THE SECRET NUMBER WAS {r_num}')
