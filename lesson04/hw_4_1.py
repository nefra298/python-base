def text_stat(inp):
    def get_string(inp):
        sep = '\n'
        text_string = sep.join(inp)
        return text_string.lower()

    def calc_digit(inp):
        n = 0
        for i in inp:
            if i.isdigit():
                n = n + 1
        return n

    def calc_lines(inp):
        n = len(inp)
        return n

    def stats(inp):
        stat = {}
        for item in inp:
            if item in stat:
                stat[item] += 1
            else:
                stat[item] = 1
        return stat

    def words_list(inp):
        sep_set = ['.', ',', ':', ';', '!', '?', '(', ')']
        word_list = inp.split()
        i = 0
        for word in word_list:
            if word[-1] in sep_set:
                word_list[i] = word[:-1]
                word = word_list[i]
            if word[0] in sep_set:
                word_list[i] = word[1:]
            i += 1
        return word_list

    text_string = get_string(inp)
    out = {}
    out["words_stat"] = stats(words_list(text_string))
    out["chars_stat"] = stats(text_string)
    out["digit"] = calc_digit(text_string)
    out["lines"] = calc_lines(inp)
    return out


def input_text():
    text = []
    print("Введите произвольный текст")
    while True:
        inp = input()
        if inp is not "":
            text.append(inp)
        else:
            break
    return text


def output_view(inp):
    def view_stat(inp):
        for item in inp:
            print(repr(item), "=", repr(inp[item]))

    for item in inp:
        if 'words_stat' in item:
            print("<-----Статистика слов----->")
            view_stat(inp['words_stat'])
            print("<-----Статистика слов----->")
        elif 'chars_stat' in item:
            print("<-----Статистика символов----->")
            view_stat(inp['chars_stat'])
            print("<-----Статистика символов----->")
        elif 'digit' in item:
            print("Всего цифр:", inp['digit'])
        elif 'lines' in item:
            print("Всего строк:", inp['lines'])
        else:
            print(inp[item])


if __name__ == '__main__':
    text = input_text()
    stat_dict = text_stat(text)
    output_view(stat_dict)
