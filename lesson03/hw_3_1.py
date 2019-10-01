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


def input_check_int(inp, msg=False):
    x = tonumeric(inp)
    if type(x) is int:
        return True
    else:
        if msg:
            print("Вы ввели не целое число",id)
        return False


def calc(inp):
    n = 0
    for i in inp:
        if i.isdigit():
            n = n + 1
    return n


if __name__ == '__main__':
    while True:
        a = input("Введите целое число или q для выхода:")
        if (a == "q"):
            exit()
        elif input_check_int(a, True):
            print("Количество цифер в числе:", calc(a))
        else:
            continue
