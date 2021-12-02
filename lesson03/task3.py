def thesaurus(*args):
    """
    возвращает словарь из списка, в котором ключами являются первые буквы
    :param args: список слов
    :return: словарь
    """
    a = {}
    for word in args:
        if not word[0] in a:
            a[word[0]] = [word]
        else:
            a[word[0]] += [word]

    print(a)


thesaurus("Иван", "Мария", "Петр", "Илья")
