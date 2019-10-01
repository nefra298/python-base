def tonumeric(inp):
    try:
        val = int(inp)
        return val
    except ValueError:
        try:
            val = float(inp)
            return val
        except ValueError:
            val = None
            return val


def positive(inp):
    if inp > 0:
        x = inp + 1
    else:
        x = 1
    return x


inp1 = input("Введите первое число:")
inp2 = input("Введите второе число:")
a = tonumeric(inp1)
b = tonumeric(inp2)
while a is None:
    print("Введено не число!")
    inp1 = input("Введите первое число:")
    a = tonumeric(inp1)
while b is None:
    print("Введено не число!")
    inp2 = input("Введите второе число:")
    b = tonumeric(inp2)
a = int(a)
b = int(b)
list = []
i = 0
if (a < 0 and b < 0) or (a == b) or (a + 1 == b) or (b + 1 == a) or (a == 1 and b < 0) or (b == 1 and a < 0):
    print("Натуральных чисел нет")
else:
    if a < b:
        list.append(positive(a))
        while list[i] != b - 1:
            list.append(list[i] + 1)
            i = i + 1
    else:
        list.append(positive(b))
        while list[i] != a - 1:
            list.append(list[i] + 1)
            i = i + 1
    print(list)
