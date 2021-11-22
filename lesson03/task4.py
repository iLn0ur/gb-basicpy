def thesaurus_adv(*args):
    """
    возвращает словарь из словаря списков, в котором ключами являются первые буквы
    фамилии, а во вложенном словаре ключи - первые буквы имени
    :param args: список слов
    :return: словарь из словарей со списками
    """
    full_name_dict = {}

    for word in args:
        name_dict = {}
        name_dict[word.split()[0][0]] = [word]
        if not word.split()[1][0] in full_name_dict:
            full_name_dict[word.split()[1][0]] = name_dict
        elif not word.split()[0][0] in full_name_dict[word.split()[1][0]]:
            full_name_dict[word.split()[1][0]].update(name_dict)
        else:
            full_name_dict[word.split()[1][0]][word.split()[0][0]] += [word]
    for key, values in full_name_dict.items():
        print(f'{key}: {values}')


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
