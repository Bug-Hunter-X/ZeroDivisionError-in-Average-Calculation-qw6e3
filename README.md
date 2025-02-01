# Python Average Calculation Bug

This repository demonstrates a common error in Python code that involves calculating the average of a list of numbers. The bug arises when the input list is empty, leading to a `ZeroDivisionError`.

The `bug.py` file contains the erroneous code. The `bugSolution.py` file provides a corrected version that handles the empty list case gracefully.

## How to reproduce
1. Clone the repository.
2. Run `bug.py` with an empty list as input. Observe the `ZeroDivisionError`.
3. Run `bugSolution.py` with an empty list. Observe that it returns 0 as expected.