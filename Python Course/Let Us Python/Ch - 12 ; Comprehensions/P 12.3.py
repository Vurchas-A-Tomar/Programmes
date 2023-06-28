import random

set_rand = {(random.randint(15, 45)) for num in range(10)}
print(set_rand)

count = {numb for numb in set_rand if numb < 30}
print(len(count))
print(set_rand - count)
