check_N = False
n = input(
    "Количество спичек(не менее 4):")
# Игра не имеет смысла если спичек будет менее 4, так как тогда победждать сможет только первый игрок
while not check_N:
    if (n.isdigit()) and (int(n) > 3):
        check_N = True
    else:
        print("Введено не корректное значение!")
        n = input("Колличество спичек(не менее 4):")
quantity = int(n)


# Вычисление номера игрока
def player(move):
    p = 1
    if move % 2 == 0:
        p = 2
    return p


# Проверка введеного количества спичек
def check_input(inp, quantity):
    if (inp.isdigit()) and (0 < int(inp) <= quantity) and (0 < int(inp) < 4):
        return True
    else:
        return False


moves = 1
while quantity != 0:
    print("Спичек осталось:", quantity)
    print("Ход игрока", player(moves))
    x = input("Взять спичек:")
    while not check_input(x, quantity):
        print("Введено не корректное значение!")
        x = input("Взять спичек:")
    quantity = quantity - int(x)
    moves = moves + 1
print("Победил игрок", player(moves))
