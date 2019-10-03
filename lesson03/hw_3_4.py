def tonumeric_ext(inp):
    try:
        val = int(inp)
    except ValueError:
        try:
            val = float(inp)
        except ValueError:
            try:
                val = complex(inp)
            except ValueError:
                val = None
    return val


def calc(inp):
    n = 0
    for i in inp:
        if i.isdigit():
            n = n + 1
    return n


if __name__ == '__main__':
    while True:
        a = input("Введите число или q для выхода:")
        if (a == "q"):
            exit()
        elif tonumeric_ext(a) is not None:
            print("Количество цифер в числе:", calc(a))
        else:
            continue
