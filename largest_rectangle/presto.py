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
from grid import Column, Reader, Grid, Rectangle, Row

def main():
    reader = Reader('city_grid.txt')
    grid = reader.get_grid()
    print '--------------------------------------------------------------------------------------------'
    print 'Original Grid Dimensions'
    print 'width=%d, height=%d' % (grid.width, grid.height)
    print '--------------------------------------------------------------------------------------------'
    print 'Score the Grid'
    # print grid.scored
    grid.score()
    print 'scored',
    print grid.scored
    print '--------------------------------------------------------------------------------------------'
    print 'Get dimensions for biggest rectangle on Grid'
    print 'width  height'
    best = grid.best_grid_rectangle()
    print best.width,
    print '    ',
    print best.height
    print '--------------------------------------------------------------------------------------------'
    print 'Best Rectangle: area=',
    print best.area

if __name__ == '__main__':
    main()

