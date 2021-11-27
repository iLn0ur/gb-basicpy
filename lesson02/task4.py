hr_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']


for count, el in enumerate(hr_list):
    temp_hr = ' '.join(el.split(' ')[0:-1:])
    temp_hr = temp_hr + ' ' + el.split(' ')[-1].title()
    hr_list[count] = temp_hr
    print(f'Привет, {temp_hr.split(" ")[-1]}!')
