import time
import random
import matplotlib.pyplot as plt
from p1_advanced import linear_search, binary_search
import statistics

# List sizes
sizes = [10, 100, 1000, 10000, 100000, 1000000]

# Lists to store times
linear_times = []
binary_times = []

# Profile the functions
for s in sizes:
    test_data = random.shuffle(list(range(s)))
    print(test_data)
    linear_time = []
    binary_time = []
    for i in range(10):
        target = random.randint(0,s)
        start_time = time.perf_counter()
        linear_search(test_data,target)
        end_time = time.perf_counter()
        linear_time.append(end_time - start_time)

        start_time = time.perf_counter()
        binary_search(test_data,target)
        end_time = time.perf_counter()
        binary_time.append(end_time - start_time)
    linear_times.append(statistics.median(linear_time))
    binary_times.append(statistics.median(binary_time))


# Plotting

plt.plot(sizes, linear_times, label = "line 1")
plt.plot(sizes, binary_times, label = "line 2")
plt.legend()
plt.show()