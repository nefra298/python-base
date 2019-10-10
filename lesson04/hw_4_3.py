def text_stat(inp,*args):
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

    def word_filter(inp, args):
        f=[]
        for i in args:
            if isinstance(i,list):
                f.extend(i)
            else:
                f.append(i)

        for word in f:
             while word in inp:
                inp.remove(word)
        print(f, inp)
        return inp

    text_string = get_string(inp)
    filter_list=list(args)
    if filter_list[0] is not None:
        word_string= word_filter(words_list(text_string), filter_list)
        text_string=get_string(word_string)
    else:
        word_string = words_list(text_string)

    out = {}
    out["words_stat"] = stats(word_string)
    out["chars_stat"] = stats(text_string)
    out["digit"] = calc_digit(text_string)
    out["lines"] = calc_lines(inp)
    return out


def input_text(welcome):
    text = []
    print(welcome)
    while True:
        inp = input()
        if inp is not "":
            text.append(inp)
        else:
            break
    return text


def output_view(inp):
    def view_stat(inp):
        list_keys = list(inp.keys())
        list_keys.sort()
        for item in list_keys:
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
    welcome_text="Введите произвольный текст(пустая строка завершает ввод):"
    text = input_text(welcome_text)
    welcome_text ="""Введите слова или фразы для фильтра. 
Каждое слово или фраза в отдельной строке, пустая строка завершает ввод:"""
    text_filter=input_text(welcome_text)
    stat_dict = text_stat(text,text_filter)
    output_view(stat_dict)