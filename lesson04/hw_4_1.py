def calc_digit(inp):
    n = 0
    for i in inp:
        if i.isdigit():
            n = n + 1
    return n


def calc_lines(inp):
    n = len(inp)
    return n


def char_stats(inp):
    chars = {}
    for char in inp:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def word_stats(inp):
    pass

def get_string(inp):
    sep = '\n'
    return sep.join(inp)


if __name__ == '__main__':
    text = []
    print("Введите произвольный текст")
    while True:
        inp = input()
        if inp is not "":
            text.append(inp)
        else:
            break

text_string = get_string(text)
print("Всего строк:", calc_lines(text))
print("Всего цифр в тексте:", calc_digit(text_string))


