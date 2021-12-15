class Matrix:
    def __init__(self, m: list):
        self.m = m

    def __str__(self):
        a: str = ''
        for i in self.m:
            for j in i:
                a += str(j)
                a += ' '
            a += '\n'
        return a

    def __add__(self, other):
        r_m: list = []
        for i, row in enumerate(self.m):
            r_row = []
            for j, col in enumerate(row):
                r_row += [self.m[i][j] + other.m[i][j]]
            r_m += [r_row]
        return Matrix(r_m)


m_sample = [[1, 2], [3, 4], [5, 1]]
m_matrix = Matrix(m_sample)
m_second = Matrix(m_sample[::-1])
print(m_second)
print(m_matrix)
m_third = m_matrix + m_second
print(m_third)
