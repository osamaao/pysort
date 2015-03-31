#!/usr/bin/python
''' Insertion Sort: Python 
insertion sort (A, n): sorts A[1..n]
    for i <-- 2 to n
        j <-- i 
        while (j > 0 and A[j] < A[i])
            swap A[i], A[j]
            j <-- j-1 
'''

import math
import time
import random
import sys
import plotly.plotly as py
from plotly.graph_objs import *

def populate_with_random_numbers(input, size):
    random.seed()
    for i in range(size):
        input.append(int(random.random() * 100000))

def insertion_sort(input):
    for i in range(1, len(input)):
        j = i
        while (j > 0 and input[j] < input[j-1]):
            tmp = input[j-1]
            input[j-1] = input[j]
            input[j] = tmp
            j = j-1


size_range = [10, 50, 100, 500, 1000, 5000, 10000]
time_points = []
print("Insertion Sort...")
for size in size_range:
    input = []
    populate_with_random_numbers(input, size);
    t1 = int(round(time.time() * 1000))
    insertion_sort(input);
    t2 = int(round(time.time() * 1000))
    required_time = t2 - t1
    time_points.append(required_time)
    print("{size: " + str(size) + ",\ttime: " + str(required_time) + "}")

trace0 = Scatter(
    x=size_range,
    y=time_points
)
data = Data([trace0])
unique_url = py.plot(data, filename = 'insertion-sort')