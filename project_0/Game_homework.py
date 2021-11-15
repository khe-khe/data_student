import random

random = random.randint(1,100)
count = 0
a = 50
b = 50
print(random)
while True:
    count += 1
    if a < random:
        a = round(a + b)
        b /= 2

    if a > random:
        a = round(a - b)
        b /= 2
    if a == random:
        print('Это число: ' + str(a) + ', попыток было: ' + str(count))
        break