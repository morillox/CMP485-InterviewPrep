"""
A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left.
For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].
Given an array of n integers and a number, d, perform d left rotations on the array. Then print the updated
array as a single line of space-separated integers.
"""


def rotate(a, n, d):
    rotated = a[d::] + a[:d:]
    done = (" ".join(str(x) for x in rotated))
    return done

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =             Test Cases                  =
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


test1 = [1, 2, 3, 4, 5]
rot1 = 2
assert rotate(test1, 5, 2) == '3 4 5 1 2', "Error not passed."

test2 = [1, 2, 3, 4, 5, 6, 7]
rot2 = 2
assert rotate(test2, 7, 2) == '3 4 5 6 7 1 2', "Error not passed."

test3 = [3, 4, 5, 6, 7, 8, 9]
rot3 = 2
assert rotate(test3, 5, 5) == '8 9 3 4 5 6 7', "Error not passed."
