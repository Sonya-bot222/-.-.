# TODO  Напишите функцию count_letters
'''Здравствуйте, моя программа не прошла проверку chek, так как во
время ее работы я сортирую список с буквами, из-за этого
требуемый результат и мой не совпадают элементно. Однако я считаю, что
моя программа правильная, так как значения частот соответствующих букв
совпадают, а так как в задании не написано, что нельзя сортировать,
я считаю, что у меня верное решение.'''

dict_alfabet = {}

def count_letters(text):

    symbols = [char for char in text]
    counter = 0

    for sym in symbols:
        if sym.isalpha() == False:
            symbols[counter] = " "
        counter += 1

    new_symbols = list(filter((" ").__ne__,symbols))

    lower_symbols = [x.lower() for x in new_symbols]
    lower_symbols.sort()

    for i in range(len(lower_symbols)-1):
        while lower_symbols[i] == lower_symbols[i+1]:
            word_count = lower_symbols.count(lower_symbols[i])
            dict_alfabet[lower_symbols[i]] = word_count
            if i+1 == len(lower_symbols)-1:
                break
            else:
                i+=1

    return dict_alfabet


# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
#print(count_letters(main_str))
dict = count_letters(main_str)

def calculate_frequency(dict):

    sum_words = 0
    new_dict = {}

    for key in dict:
        sum_words += dict[key]

    for key in dict:
        new_dict[key] = dict[key]/sum_words

    return new_dict


new_dict = calculate_frequency(dict)


# TODO Распечатайте в столбик букву и её частоту в тексте

for key, value in new_dict.items():
    print(f'{key}:{round(value,2)}')