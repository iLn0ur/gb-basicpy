class Datecls:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    @classmethod
    def date_to_int(cls, datastr: str):
        separ = ''
        i = 1
        while separ == '':
            if datastr[i].isdigit():
                i += 1
            else:
                separ = datastr[i]
        date, month, year = datastr.split(separ)
        return cls(int(date), int(month), int(year))

    @staticmethod
    def datevali(day, month, year):
        if 0 < day < 32:
            print('day is correct')
        else:
            print('day is not correct')
        if 0 < month < 13:
            print('month is correct')
        else:
            print('month is not correct')
        if year:
            print('year is always correct')

    def __str__(self):
        return f'date={self.date}\nmonth={self.month}\nyear{self.year}'


datestr = input('введите дату: ')
datestrcls = Datecls.date_to_int(datestr)
print(datestrcls)
Datecls.datevali(datestrcls.date, datestrcls.month, datestrcls.year)
