# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a=int(input("Введите число : "))
b=a%10
c=a//10 % 10
d=a//100
f=b+c+d
print(f)

