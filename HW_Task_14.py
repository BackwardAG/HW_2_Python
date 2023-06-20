# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N

n = int(input("Enter a number N (must be a maximum for 2 in power): "))
i = 0

while 2 ** i <= n:
    print(f' 2 in power {i} equals {2 ** i}')
    i += 1

