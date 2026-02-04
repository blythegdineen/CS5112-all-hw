from p2_a import closest_pair as closest_pair_a
from p2_b import closest_pair as closest_pair_b
from p2_c import closest_pair as closest_pair_c

import time
import numpy as np
import matplotlib.pyplot as plt
import random
from typing import List, Tuple
from statistics import median

def generate_test_points(n):
    #generates worst case scenario for nlogn
    points = []
    sqrt_n = int(np.sqrt(n))
    for i in range(n):
        row = i // sqrt_n
        col = i % sqrt_n
        x = col + (0.5 if row % 2 == 0 else 0.0)
        y = row
        points.append([x, y])
    return points

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

def performance_analysis():
    input_sizes = [10,50,100,500,1000,2500,5000]
    p2a_times = []
    p2b_times = []
    p2c_times = []
    
    for n in input_sizes:
        take_median_2atimes = []
        take_median_2btimes = []
        take_median_2ctimes = []
        for _ in range(10):
            points = generate_test_points(n)
            p2a_time = measure_time(closest_pair_a,points)
            take_median_2atimes.append(p2a_time)
            
            p2b_time = measure_time(closest_pair_b,points)
            take_median_2btimes.append(p2b_time)

            p2c_time = measure_time(closest_pair_c,points)
            take_median_2ctimes.append(p2c_time)

        p2a_times.append(median(take_median_2atimes))
        p2b_times.append(median(take_median_2btimes))
        p2c_times.append(median(take_median_2ctimes))

    return input_sizes, p2a_times, p2b_times, p2c_times

def plot_performance(input_sizes, p2a_times, p2b_times, p2c_times):
    plt.plot(input_sizes, p2a_times, label='P2A Runtimes (O(n²))')
    plt.plot(input_sizes, p2b_times, label='P2B Runtimes (O(nlogn))')
    plt.plot(input_sizes, p2c_times, label='P2C Runtimes (O(n))')
    #plt.yscale('log')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Median of Execution Time Over 10 Attempts (seconds)')
    plt.legend()
    plt.show()

def main():
    input_sizes, p2a_times, p2b_times, p2c_times = performance_analysis()
    plot_performance(input_sizes, p2a_times, p2b_times, p2c_times)

if __name__ == "__main__":
    main()
