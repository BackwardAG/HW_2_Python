# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх 
# решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Enter the amount of coins: "))
eagle = 0
tails = 0

for i in range(n):
    coins = int(input(f'enter 0 or 1 for {i+1} coin side\n'))
    if coins == 0:
        eagle += 1
    else:
        tails += 1
print("0 - eagle, 1 - tails")

if eagle > tails:
    print(f"We have {tails} tails, so Turn tails over")
else:
    print(f"We have {eagle} eagles, so Turn eagles over")