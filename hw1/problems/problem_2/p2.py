'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
    if not intervals:
            return []
    
    # 1. Sort intervals by start time
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    
    # 2. Setup variables
    final_intervals = []
    i = 0
    end = 0 #stores the last endpoint of our intervals in final_interval
    
    # 3. While the final_intervals end point is less than the end of our larger interval
    while end < M:
        best_end = end
        best_interval_index = 0 #stores the index of the interval

        #4. iterate through each interval that starts <= endpoint of final_intervals (no gaps)
        while i < len(intervals) and intervals[i][0] <= end:
            
            # 5. if the interval ends after our best, make it our new best 
            if intervals[i][1] > best_end:
                best_interval_index = i
                best_end = intervals[i][1]
            i += 1

        # 6. append our best interval 
        final_intervals.append(intervals[best_interval_index])
        end = best_end

    return final_intervals


#     remaining = []
#     # 1. sort intervals by start time asc, if start times equal, then sort by end time desc
#     intervals.sort(key=lambda x: (x[0], -x[1]))
   
#    # 2. add first interval to our output
#     remaining.append(intervals[0])
#     # 3. traverse intervals     
#     for i in range(1,len(intervals)):
#         current = intervals[i]
#         prev_remaining = remaining[-1]
#         # 4. check if current is covered by our set of remaining intervals
#         if current[0] >= prev_remaining[0] and current[1] <= prev_remaining[1]:
#             continue
#         else: # 5. check if current is covered by the future interval
#             remaining.append(current)
#             if i < len(intervals) - 1:
#                 future = intervals[i+1]
#                 if prev_remaining[1] >= future[0] and future[1] >= current[1]:
#                     remaining.remove(current)
        
#     return remaining