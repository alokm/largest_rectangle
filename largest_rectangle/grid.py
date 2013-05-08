#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Presto Grid - objects and utilities for operating on Presto 

class Reader(object):
    # reads a file and returns an input grid object containing raw data
    def __init__(self, filename='sample.txt'):
        self.file = open(filename, 'r')

    def get_chars(self, line):
        for char in line:
            yield char

    def get_line(self):
        while True:
            raw_line = self.file.readline()
            line_data = raw_line.replace(' ', '').strip()
            if not line_data:
                break
            line = [ char for char in line_data ]
            yield line

    def get_grid(self):
        lines = [ line for line in self.get_line() ]
        return Grid(lines)


class Column(object):
    def __init__(self, values=[]):
        self.values = [ value for value in values ]
        self.repeats = []
        self.scored = False

    def __repr__(self):
        return 'Column([values]) Scored =%s' % self.scored

    def count_repeats(self):
        repeats = 0  # int count of repeated 'P', reset on 'O'
        for offset, el in enumerate(reversed(self.values)):
            index = len(self.values) - offset - 1
            if el == 'P':
                repeats += 1
            else:
                repeats = 0
            # inserts are slow; I should fix.
            self.repeats.insert(0, repeats)
        self.scored = True
        return self.repeats


class Row(object):
    def __init__(self, row_id, scores=[]):
        self.row_id = row_id
        self.scores = [ score for score in scores ]
        self.best_rectangle = None

    def __repr__(self):
        return 'Row(%d)' % self.row_id

    def _get_best_rectangle_at_offset(self, offset):
        # find the biggest rectangle for a row at offset
        # import ipdb; ipdb.set_trace()
        width = 1 
        height = self.scores[offset]
        best_rectangle = Rectangle(width, height)
        for score in self.scores[offset:]:
            if score is not 0:
                height = min(height, score)
                rectangle = Rectangle(width, height)
                if rectangle.area > best_rectangle.area:
                    best_rectangle = rectangle
            else:
                break
            width += 1
        return best_rectangle

    def get_best_rectangle(self):
        # find the best rectangle for a given offset
        best_rectangle = Rectangle(1,1)
        for offset, score in enumerate(self.scores):
           rectangle = self._get_best_rectangle_at_offset(offset)
           if rectangle.area > best_rectangle.area:
                best_rectangle = rectangle
        self.best_rectangle = best_rectangle
        return best_rectangle


class Rectangle(object):
    def __init__(self, width, height): 
        self.width = width
        self.height = height
        self.area = self.get_area()

    def __repr__(self):
        return "Rectangle()"

    def get_area(self):
        self.area = self.height * self.width
        return self.area


class Grid(object):
    def __init__(self, data=[]):
        self.data = data # stores the raw data as nested list
        self.width = self.get_width()
        self.height = self.get_height()
        self.scores = [ [0] * self.width for row in self.data ] # rows are created by score_column methods
        self.scored = False
        

    def __repr__(self):
        return "Grid(w=%d, h=%d)" % (self.width, self.height)

    def get_width(self):
        self.width = len(self.data[0])
        return self.width

    def get_height(self):
        self.height = len(self.data)
        return self.height

    def _get_column(self, offset):
        col_data = [ self.data[row_id][offset] for row_id, data in enumerate(self.data) ]
        return Column(col_data)

    def _score_column(self, offset):
        column = self._get_column(offset)
        repeats = column.count_repeats()
        for index, row in enumerate(self.scores):
            self.scores[index][offset] = repeats.pop(0) #first element
        return True

    def score(self):
        for offset in range(self.width):
            self._score_column(offset)
        self.scored = True
        return self.scored

    def _get_best_row_rectangle(self, row_id):
        if self.scored == True:
            row = Row(row_id, self.scores[row_id])
            best_rectangle = row.get_best_rectangle()
            return best_rectangle

    def best_grid_rectangle(self):
        # import ipdb; ipdb.set_trace()
        best_rectangle = Rectangle(1,1)
        for row_id in range(self.height):
            rectangle = self._get_best_row_rectangle(row_id)
            if rectangle.area > best_rectangle.area:
                best_rectangle = rectangle
        return best_rectangle

