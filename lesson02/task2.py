list_of_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
correct_list = []

for el in list_of_words:
    if el[0] == '-':
        sign = '-'
    elif el[0] == '+':
        sign = '+'
        if el[1:].isdigit():
            correct_list.append('"')
            correct_list.append(sign + el[1:].rjust(2, '0'))
            correct_list.append('"')
            continue
    if el.isdigit():
        correct_list.append('"')
        correct_list.append(el.rjust(2, '0'))
        correct_list.append('"')
        continue
    correct_list.append(el)

sign_control = 0

result = ''
for i in range(len(correct_list)):
    if sign_control:
        sign_control -= 1
        continue
    result += correct_list[i]
    if correct_list[i] == '"':
        result = result + correct_list[i + 1] + correct_list[i + 2]
        sign_control = 2
    result += ' '

print(result)
