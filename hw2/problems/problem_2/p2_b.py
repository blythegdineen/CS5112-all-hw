'''
Problem 2b
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    # sort points by x axis    
    sorted_points = sorted(points, key=lambda x: (x[0], x[1]))

    # build recursion
    def dc_closest_pair(points, left, right):
        closest = []
        best_dist =  math.inf

        #set base case
        if right - left <=3:
            for i in range(left,right):
                for j in range(i+1,right):
                    dist =  d(points[i],points[j])
                    if dist < best_dist:
                        best_dist = dist
                        closest = [points[i],points[j]]
            return closest

        midpoint = (left + right) //2
        mid_x = points[midpoint][0]
        
        # recurse on both sides
        closest_left = dc_closest_pair(points,left,midpoint)
        closest_right = dc_closest_pair(points,midpoint,right)
        
        if closest_left:
            closest_left_dist = d(closest_left[0],closest_left[1])
            if closest_left_dist < best_dist:
                best_dist = closest_left_dist
                closest = closest_left
        if closest_right:
            closest_right_dist = d(closest_right[0],closest_right[1])
            if closest_right_dist < best_dist:
                best_dist = closest_right_dist
                closest = closest_right

        #find closest in the strip
        strip = []
        for i in range(left,right):
            if abs(points[i][0] - mid_x) < best_dist:
                strip.append(points[i])
        
        # sort strip by y
        strip.sort(key=lambda x: x[1])

        # update best dist and closest based on strip brute force
        for i in range(len(strip)):
            for j in range(i+1, min(i+8, len(strip))): #limit to 8 closest points for efficiency
                dist = d(strip[i],strip[j])
                if  dist < best_dist:
                    best_dist = dist
                    closest = [strip[i],strip[j]]
        return closest
    
    # run recursion
    return dc_closest_pair(sorted_points,0,len(sorted_points))