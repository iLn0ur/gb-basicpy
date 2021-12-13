class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('draw stationery')


class Pen(Stationery):

    def draw(self):
        print(f'draw pen by {self.title}')


class Pencil(Stationery):

    def draw(self):
        print('draw pencil')


class Handle(Stationery):

    def draw(self):
        print('draw Handle')


pen = Pen('hb')
pen.draw()
pencil = Pencil('bic')
pencil.draw()
handle = Handle('immanent')
handle.draw()
