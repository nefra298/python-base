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


def input_check_int(inp, msg=False, id=""):
    x = tonumeric(inp)
    if type(x) is int:
        return True
    else:
        if msg:
            print("Вы ввели не целое число",id)
        return False

def nok (a,b):
    i = 1
    if a>b:
        x=a
        while x%b!=0:
            i=i+1
            x=a*i
    else:
        x=b
        while x%a!=0:
            i=i+1
            x=b*i
    return x

if __name__ == '__main__':
    while True:
        a = input("Введите целое число А:")
        b = input("Введите второе целое число В или q для выхода:")
        if (b == "q"):
            exit()
        elif input_check_int(a, True, "A") and input_check_int(b, True, "B"):
            print("Наименьшее общее кратное:", nok(int(a), int(b)))
        else:
            continue
