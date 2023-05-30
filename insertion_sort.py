import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(len(arr)):
        d=len(arr)-1
        e=arr[len(arr)-1]
        for y in range(len(arr),1,-1):
            if(e<arr[y-2]):
                d-=1
                arr[y-1]=arr[y-2]
                for z in arr:
                    print(z,end=" ")
                print()
        arr[d]=e   
    for z in arr:
        print(z,end=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
