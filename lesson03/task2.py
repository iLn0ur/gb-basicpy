def num_translate(num):
    """
       функция осуществляет перевод числа, если число присутствует в словаре или возвращает None
       c учётом регистра
       :param num: значение на английском
       :return: перевод или None
       """
    nums = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}

    if num.lower() in nums.keys():
        if num[0].isupper():
            print(nums[num.lower()].capitalize())
        else:
            print(nums[num])
    else:
        print(None)


num_translate(input('Enter num '))
