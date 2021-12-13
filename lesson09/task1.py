import time


class TrafficLight:
    def __init__(self):
        self.__color = {'red': 7, 'yellow': 2, 'green': 7}

    def on_off_liqht(self, color):
        i = 10
        while i > 0:
            if color in self.__color:
                print(color)
                time.sleep(self.__color[color])
                if color == 'red':
                    color = 'yellow'
                    check = False
                elif color == 'yellow':
                    if check:
                        color = 'red'
                    else:
                        color = 'green'
                elif color == 'green':
                    color = 'yellow'
                    check = True
                i -= 1
            else:
                raise ValueError("неверный цвет светофора")


shine = TrafficLight()
shine.on_off_liqht('black')
