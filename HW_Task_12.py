# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
# и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# X и Y (X,Y≤1000)
# Max summ = 2000
# Max multi = 1000000

S = int(input("Enter a summ of two numbers: "))
M = int(input("Enter a multiplication result of two numbers: "))

x = 0
y = 0

if S <= 2000 and M <= 1000000:
    for x in range(1001):
        for y in range(1001):
            if S == x + y and M == x * y:
                print(f"x = {x}, y = {y}")                 
               
else:
    print("Peter is cheating!")