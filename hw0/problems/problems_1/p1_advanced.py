def manage_queue(operations):
    """
    Manage a queue system for a customer service desk.
    
    The queue is represented as a list where the first element is the first person in line. 
    Implement the following operations:
    - Enqueue: Add a person to the end of the queue.
    - Dequeue: Remove and return the name of the first person in line.
    - Remove Person: Given a person's name, remove them from the queue.
    - Jump the Queue: A person has a quick question and is allowed to jump to the front of the queue, 
      but not in front of the very first person.
    
    Parameters:
    - operations (list): A list of tuples where the first element of each tuple is the operation 
      (either "enqueue", "dequeue", "remove", or "jump") and the second element (if applicable) is the person's name.
    
    Returns:
    - list: The state of the queue after performing all the operations.
    
    Example:
    
    Input: 
    [("enqueue", "Alice"), ("enqueue", "Bob"), ("enqueue", "Charlie"), ("dequeue",), ("jump", "Eve"), ("remove", "Bob")]
    
    Output:
    ["Eve", "Charlie"]
    """
    queue = []
    for o in operations:
        if o[0] == "enqueue":
            queue.append(o[1]) 
        elif o[0] == "dequeue":
            if len(queue) > 0:
              queue.pop(0)
        elif o[0] == "remove":
            if o[1] in queue:
                queue.remove(o[1])
        elif o[0] == "jump":
            if len(queue) > 0:
              if o[1] in queue:
                queue.remove(o[1])
              queue.insert(1,o[1])
            else:
              pass
        else: 
            pass
    return queue

def factorial_dp(n, memo={}):
    """
    Returns the factorial of n using dynamic programming (memoization).
    """
    if n == 0:
      return 1
    if n not in memo:
      memo[n] = n * factorial_dp(n-1, memo)
    return memo[n]

def linear_search(lst, target):
    """
    Perform a linear search on the list to find the index of the target element.

    Parameters:
    - lst (list): A list of elements.
    - target: The element to search for.

    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    index = -1
    for l in lst:
       if l == target:
          index = lst.index(l)
    return index

def binary_search(lst, target):
    """
    Perform a binary search on the sorted list to find the index of the target element.

    Parameters:
    - lst (list): A sorted list of elements.
    - target: The element to search for.

    Returns:
    - int: The index of the target element if found, otherwise -1.
    """

    lst.sort()
    low = 0
    high = len(lst) - 1

    while low <= high:
      middle = round(high-low/2) + low
      if lst[middle] == target:
        return middle
      if lst[middle] < target:
         low = middle + 1
      if lst[middle] > target:
         high = middle - 1

    return -1
