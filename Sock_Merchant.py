from collections import Counter
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = Counter(ar)
    pairs = 0
    for key in count:
        if count[key]%2 == 0:
            pairs += (count[key]/2)
        else:
            pairs += ((count[key]-1)/2)
    return int(pairs)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
