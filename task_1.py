"""1 homerwork"""
""""Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |"""

number = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третьее число: "))
number_result = number + number_2 + number_3
print(f"Сумма цифр  трехзначного числа: {number}{number_2}{number_3}", "->",
      number_result, f"({number} + {number_2} + {number_3})")