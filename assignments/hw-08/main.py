'''
### Description

This README is intended to guide the user in how to use HW-08.

The assignment is hosted on github here:

https://github.com/DavisVaughan/uncc-math-6204/tree/master/assignments/hw-08

### General

* Author   - Davis Vaughan
* Date     - 11/15/2017
* Homework - 08

### Purpose

The purpose of this HW is to calculate the solution to a linear system Ax = b
using the Thomas Algorithm where A is a tridiagonal matrix.

### Thoughts on numerical accuracy

This is an exact and efficient method to solve a linear system. It is
better than taking an inverse for this sparse matrix.

### Numerical methods used

The Thomas algorithm is used as an efficient method of solving this system.
See the documentation of the thomas_solver function for a description of the algo.

### Included files

`main.py` - (DRIVER) Thomas algorithm example.

`thomas.py` - Contains functions that solve the system using the thomas algo.

### How to run

Because the main.py file includes the code:


if __name__ == "__main__":
    print(main())


the easiest way to run the example is from the terminal.

Within your command line / terminal, navigate to the folder containing the main.py script, and just run:

python3 main.py

^ Note that this homework actually uses python3 not python2 as I normally do.

A numpy array should output:

[ 4.54545455  0.90909091  3.63636364  1.81818182  2.72727273  2.72727273
  1.81818182  3.63636364  0.90909091  4.54545455]

'''

import numpy as np
from scipy.sparse import spdiags
from thomas import thomas_solver

def main():

    size = 10

    # Set up to create A
    main_diag = 2 * np.ones(size)
    sub_diag  = np.ones(size)
    sup_diag  = np.ones(size)
    A_data = np.array([main_diag, sub_diag, sup_diag])
    tri_set = np.array([0, -1, 1])

    # Create A and b
    A = spdiags(A_data, tri_set, size, size).toarray()
    b = 10 * np.ones(size)

    # Solve the system
    x = thomas_solver(A, b)

    return x


if __name__ == "__main__":
    print(main())