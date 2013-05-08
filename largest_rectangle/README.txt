This program implements an algorithm to efficiently search through a large two-dimensional boolean grid consisting of 'P' and 'O' characters.
The algorithm is designed to find the area of the largest rectangle consisting of contiguous 'P' characters within the grid.

Dependencies: 
There should be no dependencies required other than Python 2.6+

Instructions:
To start the program simply run 'python presto.py' from the command line.

The algorithm works by pre-computing a scored grid. On the first pass the grid scores each element of each column starting at the bottom and counting the repeated uninterrupted instances of 'P'. On the second pass the algorithm computes the largest rectangle possible for each element in each row using the grid scores to dramatically reduce extra computation.

The result is an O(N) solution (actually 2 * O(N) operations)

Software written by Alok Mohindra alok.mohindra@gmail.com
Licensed under GPLv3 (see http://www.gnu.org/licenses/gpl.html)
