from p1_b import stable_matching_1b
from p1_c import stable_matching_1c
import time
import numpy as np
import matplotlib.pyplot as plt
import random
from typing import List, Tuple
from statistics import median

def generate_test_file(n):
    with open("test.txt", 'w') as f:
        f.write(f"{n}\n")
        for i in range(n):
            preferences = list(range(n))
            f.write(" ".join(map(str, preferences)) + "\n")
        for i in range(n):
            preferences = list(range(n))
            f.write(" ".join(map(str, preferences[::-1])) + "\n")

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
            file = generate_test_file(n)
            p1b_time = measure_time(stable_matching_1b,"test.txt")
            take_median_1btimes.append(p1b_time)
            p1c_time = measure_time(stable_matching_1c,"test.txt")
            take_median_1ctimes.append(p1c_time)
        p1b_times.append(median(take_median_1btimes))
        p1c_times.append(median(take_median_1ctimes))

    return input_sizes, p1b_times, p1c_times

def plot_performance(input_sizes, p1b_times, p1c_times):
    n_squared = [i ** 2 for i in input_sizes]
    n_cubed = [i ** 3 for i in input_sizes]
    plt.plot(input_sizes, p1b_times, label='P1B Times O(n³)')
    plt.plot(input_sizes, p1c_times, label='P1C Times O(n²)')
    #plt.plot(input_sizes, n_squared, label='n²')
    #plt.plot(input_sizes, n_cubed, label='n³')
    plt.xlabel('Input Size (n)')
    plt.ylabel('median of Execution Time Over 10 Attempts (seconds)')
    plt.legend()
    plt.show()


def main():
    input_sizes, p1b_times, p1c_times = performance_analysis()
    plot_performance(input_sizes, p1b_times, p1c_times)

if __name__ == "__main__":
    main()
