# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.


for x in range(2):
        for y in range(2):
            for z in range(2):
                if not(x or y or z) == (not x and not y and not z):
                    print(f'{x}\t{y}\t{z}\t{not(x or y or z) == (not x and not y and not z)}')

# не писать выражение в строку вывода!!

# не (х или у или з) == не х и не у и не з
# print(f'{x}\t{y}\{z}\t{}')
# 0    0    1    1
# только в конце единичка всегда

