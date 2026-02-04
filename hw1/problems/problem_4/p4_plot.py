from p4_b import most_frequent_difference_b
from p4_c import most_frequent_difference_c
import time
import numpy as np
import matplotlib.pyplot as plt
import random
from typing import List, Tuple
from statistics import median

def generate_test(n):
    values = [random.randint(1, 20) for _ in range(n)]
    return values, random.randint(1, 10)

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

def performance_analysis():
    input_sizes = [0,5,10,25,50,100,500,1000]
    p1b_times = []
    p1c_times = []
    
    for n in input_sizes:
        take_median_1btimes = []
        take_median_1ctimes = []
        for _ in range(10):
            values, d_mode = generate_test(n)
            p1b_time = measure_time(most_frequent_difference_b,values,d_mode)
            take_median_1btimes.append(p1b_time)
            p1c_time = measure_time(most_frequent_difference_c,values,d_mode)
            take_median_1ctimes.append(p1c_time)
        p1b_times.append(median(take_median_1btimes))
        p1c_times.append(median(take_median_1ctimes))

    return input_sizes, p1b_times, p1c_times

def plot_performance(input_sizes, p1b_times, p1c_times):
    plt.plot(input_sizes, p1b_times, label='P4b Times O(nlogn)')
    plt.plot(input_sizes, p1c_times, label='P4c Times O(n)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Median of Execution Time Over 10 Attempts (seconds)')
    plt.legend()
    plt.show()


def main():
    input_sizes, p1b_times, p1c_times = performance_analysis()
    plot_performance(input_sizes, p1b_times, p1c_times)

if __name__ == "__main__":
    main()
