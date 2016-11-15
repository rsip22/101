# Listar números primos de 1 a 100
num = []

num.extend(range(1, 100))

print("Números primos de 1 a 100:")

for item in num:
    if (item == 1):
        continue
    else:
        divisor = 2
        while (item % divisor != 0):
            divisor += 1

        if (item == divisor):
            primo = item
            print(primo)
        else:
            continue
