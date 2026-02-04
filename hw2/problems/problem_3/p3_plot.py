from p3_a import Node, LinkedList
from p3_b import Node, SkipList

import time
import numpy as np
import matplotlib.pyplot as plt
import random
from typing import List, Tuple
from statistics import median

def generate_linked_list(n):
    """Generate a linked list with n random elements and return a random element to search/delete"""
    ll = LinkedList()
    values = random.sample(range(n * 10), n)  # n unique random values
    
    for val in values:
        ll.insert(val)
    
    # Return a random element that exists in the list
    x = random.choice(values)
    return ll, x

def generate_linked_list_worst_case(n):
    """Generate worst case: search/delete last element"""
    ll = LinkedList()
    values = list(range(n))
    
    for val in values:
        ll.insert(val)
    
    # Return the last element (worst case for search/delete)
    x = n - 1
    return ll, x

def generate_skip_list(n):
    """Generate a skip list with n random elements and return a random element to search/delete"""
    max_level = int(np.log2(n)) + 1 if n > 0 else 1
    sl = SkipList(max_level=max_level, p=0.5)
    
    values = random.sample(range(n * 10), n)  # n unique random values
    
    for val in values:
        sl.insert(val)
    
    # Return a random element that exists in the list
    x = random.choice(values)
    return sl, x

def generate_skip_list_worst_case(n):
    """Generate worst case skip list: all nodes at lowest level only"""
    max_level = int(np.log2(n)) + 1 if n > 0 else 1
    sl = SkipList(max_level=max_level, p=0.5)
    
    values = list(range(n))
    
    # Force worst case by setting random seed to create flat structure
    random.seed(42)
    for val in values:
        sl.insert(val)
    random.seed()  # Reset seed
    
    # Return the last element
    x = n - 1
    return sl, x

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

def performance_analysis():
    input_sizes = [10,50,100,500,1000,2500,5000]
    
    linked_search_times = []
    linked_insert_times = []
    linked_delete_times = []
    
    skip_search_times = []
    skip_insert_times = []
    skip_delete_times = []
    
    for n in input_sizes:
        median_linked_search_times = []
        median_linked_insert_times = []
        median_linked_delete_times = []
        
        median_skip_search_times = []
        median_skip_insert_times = []
        median_skip_delete_times = []
        
        for _ in range(10):
            linked_list, x = generate_linked_list_worst_case(n)
            
            linked_search_time = measure_time(LinkedList.search,linked_list,x)
            median_linked_search_times.append(linked_search_time)

            linked_delete_time = measure_time(LinkedList.delete,linked_list,x)
            median_linked_delete_times.append(linked_delete_time)

            linked_insert_time = measure_time(LinkedList.insert,linked_list,x)
            median_linked_insert_times.append(linked_insert_time)

            skip_list, x = generate_skip_list_worst_case(n)

            skip_search_time = measure_time(SkipList.search,skip_list,x)
            median_skip_search_times.append(skip_search_time)

            skip_delete_time = measure_time(SkipList.delete,skip_list,x)
            median_skip_delete_times.append(skip_delete_time)

            skip_insert_time = measure_time(SkipList.insert,skip_list,x)
            median_skip_insert_times.append(skip_insert_time)

        linked_search_times.append(median(median_linked_search_times))
        linked_delete_times.append(median(median_linked_delete_times))
        linked_insert_times.append(median(median_linked_insert_times))

        skip_search_times.append(median(median_skip_search_times))
        skip_delete_times.append(median(median_skip_delete_times))
        skip_insert_times.append(median(median_skip_insert_times))
    return input_sizes, linked_search_times, linked_delete_times, linked_insert_times, skip_search_times, skip_delete_times, skip_insert_times

def plot_performance(input_sizes, linked_times, skip_times, type):
    plt.figure(figsize=(10, 6))  # Create new figure for each plot
    plt.plot(input_sizes, linked_times, marker='o', label='LinkedList Runtimes (Worst Case)')
    plt.plot(input_sizes, skip_times, marker='s', label='SkipList Runtimes (Worst Case)')
    #plt.yscale('log')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Median of Execution Time Over 10 Attempts (seconds)')
    plt.title('Median Execution Time (Worst Case) for LinkedList vs SkipList for '+type)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

def main():
    input_sizes, linked_search_times, linked_delete_times, linked_insert_times, skip_search_times, skip_delete_times, skip_insert_times  = performance_analysis()
    plot_performance(input_sizes, linked_search_times, skip_search_times, "Search")
    plot_performance(input_sizes, linked_insert_times, skip_insert_times, "Insert")
    plot_performance(input_sizes, linked_delete_times, skip_delete_times, "Delete")
    plt.show() 
if __name__ == "__main__":
    main()