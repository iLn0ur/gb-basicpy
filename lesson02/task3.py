list_of_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

sign_control = 0

for count, el in enumerate(list_of_words):
    if sign_control:
        sign_control -= 1
        continue
    if el[0] == '-':
        sign = '-'
    elif el[0] == '+':
        sign = '+'
        if el[1:].isdigit():
            temp_el = el
            list_of_words.insert(count, '"')
            list_of_words[count + 1] = sign + temp_el[1:].rjust(2, '0')
            list_of_words.insert(count + 2, '"')
            sign_control = 2
            continue
    if el.isdigit():
        temp_el = el
        list_of_words.insert(count, '"')
        list_of_words[count + 1] = temp_el.rjust(2, '0')
        list_of_words.insert(count + 2, '"')
        sign_control = 2
        continue

result = ''
for i in range(len(list_of_words)):
    if sign_control:
        sign_control -= 1
        continue
    result += list_of_words[i]
    if list_of_words[i] == '"':
        result = result + list_of_words[i + 1] + list_of_words[i + 2]
        sign_control = 2
    result += ' '

print(result)
