"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks
with matching colors there are.

For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2] . There is one pair of
color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
"""


from collections import Counter

"""
Task:

Complete the sockMerchant function in the editor below. It must return an integer representing 
the number of matching pairs of socks that are available. Create 3 test cases.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
"""


def sockMerchant(n, ar):
    count = Counter(ar)
    pairs = 0
    for key in count:
        if count[key]%2 == 0:
            pairs += (count[key]/2)
        else:
            pairs += ((count[key]-1)/2)
    return int(pairs)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =        Test cases           =
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


test1 = [2, 2, 3, 3, 4, 4, 1]
assert sockMerchant(7, test1) == 3, "PASS"

test2 = [2, 5, 3, 3, 4, 4, 1]
assert sockMerchant(7, test2) == 2, "PASS"

test3 = [2, 2, 3, 3, 4, 4, 1, 2, 2, 3, 3, 4, 4]
assert sockMerchant(7, test3) == 6, "PASS"

print("All test cases passed.")