class IntegralImage(object):
    def __init__(self, original):
        '''
        original list[list]: 2d array containing original table data
        '''
        width = len(original[0])
        height = len(original)
        self.table = [[0 for _ in range(width)] for _ in range(height)]

        for y in range(height):
            for x in range(width):
                self.table[y][x] = original[y][x] + self.get(x - 1, y) + self.get(x, y - 1) - self.get(x - 1, y - 1)

    def get(self, x, y):
        ''' Returns value of cell at x, y
        x (int): x position of cell
        y (int): y position of cell

        All rows/columns are zero-indexed from top-left
        If requested cell is out of range 0 will be returned

        Returns int
        '''
        if x < 0 or y < 0 or x >= len(self.table[0]) or y >= len(self.table):
            return 0
        else:
            return self.table[y][x]

    def box_sum(self, x, y, w, h):
        ''' Sums a box at x, y with width w and height h
        x (int): x position of cell
        y (int): y position of cell
        w (int): width of box to sum
        h (int): height of box to sum

        Returns int
        '''
        y += h - 1
        x += w - 1
        return self.get(x, y) - self.get(x, y - h) - self.get(x - w, y) + self.get(x - w, y - h)

    def __repr__(self):
        return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.table])
