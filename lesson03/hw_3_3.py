def triangle(a, b, c):
    if (a is not None) and (b is not None) and (c is not None):
        if (a < b + c) and (b < a + c) and (c < a + b):
            p = (a + b + c) / 2
            area = round((p * (p - a) * (p - b) * (p - c)) ** 0.51, 2)
            print("Площать треугольника:", area)
        else:
            print("Треугольник не существует!")


def circle(r):
    import math
    area = round(math.pi * r * r, 2)
    print("Площать круга:", area)


def rect(a, b):
    print("Площать прямоугольника:", round(a * b, 2))


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


if __name__ == '__main__':
    while True:
        print(
            """Виберите необходимое действие:
            1. Расчет площади треугольника
            2. Расчет прощади круга
            3. Расчет площади прямоугольника
            4. Выход
            """)
        menu_item = input("Действие(1-4):")
        if (menu_item == "4"):
            exit()
        elif menu_item == "1":
            print("Расчет площади треугольника")
            a = input("Введите длинну стороны А:")
            b = input("Введите длинну стороны B:")
            c = input("Введите длинну стороны C:")
            if (tonumeric(a) is not None) and (tonumeric(b) is not None) and (tonumeric(c) is not None):
                triangle(float(a), float(b), float(c))
                input("Нажмите любую кнопку что бы продолжить")
            else:
                print("Введены не корректные значения")
        elif menu_item == "2":
            print("Расчет площади круга")
            r = input("Введите радиус круга:")
            if (tonumeric(r) is not None):
                circle(float(r))
                input("Нажмите любую кнопку что бы продолжить")
            else:
                print("Введены не корректные значения")
        elif menu_item == "3":
            print("Расчет площади прямоугольника")
            a = input("Введите длинну стороны А:")
            b = input("Введите длинну стороны B:")
            if (tonumeric(a) is not None) and (tonumeric(b) is not None):
                rect(float(a), float(b))
                input("Нажмите любую кнопку что бы продолжить")
            else:
                print("Введены не корректные значения")
        else:
            print("Не верно укзан пункт меню")
            continue
