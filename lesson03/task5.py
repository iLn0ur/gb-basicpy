from random import choice


def get_jokes(n, flag_repeat=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(int(n)):
        print(choice(nouns), choice(adverbs), choice(adjectives))


get_jokes(input('введите количество шуток: '))
