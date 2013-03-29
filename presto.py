#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Presto
# This grid shows the restaurants in Hamburg which have E la Carte units 
# ("Prestos") installed in them. The Ps in the grid represent restaurants 
# with Prestos installed ("Prestorants"). Os represent restaurants without 
# prestos.
#
# Count the number of restaurants in the largest contiguous rectangular 
# block of Prestorants.


class Reader(object):
    # reads a file and returns a grid
    def __init__(self, filename='sample.txt'):
        self.file = open(filename, 'r')

    def get_line(self):
        while True:
            raw_line = self.file.readline()
            line = raw_line.replace(' ', '').strip()
            if not line:
                break
            yield line

    def get_grid(self):
        rows = [ line for line in self.get_line() ]
        return Grid(rows)


class Rectangle(object):
    def __init__(self, row=0, offset=0, width=0, height=0):
        self.row = row # in which row it starts
        self.offset = offset # in which column it starts
        self.width = width
        self.height = height
        self.size = None

    def __repr__(self):
        return "Rectangle(offset=%d, w=%d, h=%d)" % (self.offset, 
                                                             self.width, 
                                                             self.height)

    def get_size(self):
        if not self.size:
            self.size = self.height * self.width
        return self.size


class Row(object):
    def __init__(self, data=''):
        self.data = data
        self.rectangles = []

    def _get_width(self, offset):
        # computes and returns width of rectangle of Ps to the right of offset
        width = 0
        for char in self.data[offset:]:
            if char == 'P':
                width += 1
            else:
                break
        return width or None
 
    def make_rectangles(self):
        offset = 0
        while offset < len(self.data):
            char = self.data[offset]
            if char == 'P':
                width = self._get_width(offset)
                self.rectangles.append(Rectangle(row=None, offset=offset, 
                                               width=width, height=1))
                offset += width
            offset += 1
        return self.rectangles

    def get_best_rectangle(self, rectangle=Rectangle(), row=None):
        pass


class Grid(object):
    def __init__(self, rows=[]):
        self.rows = [ Row(row) for row in rows ]

    def process_row(self, row):
        return self.rows[row].make_rectangles()

    def get_candidates(self, base_rect=Rectangle, start_row=0):
        best_candidate = base_rect

        for index, row in enumerate(self.rows[start_row:]):
            if not self.rows[index+1]:
                break
            else:
                candidates = self.process_row(index+1)
                while candidates:
                    print index+1, candidates
        return self.process_row(row)
        
    def compare_rectangles(self, base=Rectangle, test=Rectangle):
        # test if rectangles overlap, if so return a new rectangle
        bstart, bend = base.offset, base.offset + base.width
        tstart, tend = test.offset, test.offset + test.width

        new_start = max(bstart, tstart)
        new_width = min(bend-bstart, tend-tstart)
        new_height = base.height + test.height
        new_rectangle = Rectangle(row=None, offset=new_start, width=new_width, height=new_height)
        return new_rectangle


def main():
    reader = Reader('small_sample.txt')
    
    grid = reader.get_grid()

    print grid.rows[0].data, grid.rows[0].make_rectangles()
    print grid.rows[1].data, grid.rows[1].make_rectangles()

if __name__ == '__main__':
    main()