"""Задача 8: Требуется определить, можно ли от шоколадки размером n × m
долек отломить k долек, если разрешается сделать один разлом по прямой
между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no"""

first_part_chocolate = int(input("Введите размер шоколадки в длину: "))
second_part_chocolate = int(input("Введите размер шоколадки в ширину: "))
full_result = first_part_chocolate * second_part_chocolate - 2
if full_result > 2:
    print(f"{full_result}", "Норм, можно пополам")
else:
    print("Плохая идея")

#Честно задачку не понял, пришлось решить как попало =(

