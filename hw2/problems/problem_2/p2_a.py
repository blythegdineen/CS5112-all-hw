'''
Problem 2a
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    closest = []
    best_dist = math.inf
    for pt_a in points:
        for pt_b in points:
            if pt_a != pt_b:
                dist = d(pt_a,pt_b)
                if dist < best_dist:
                    best_dist = dist
                    closest = [pt_a,pt_b]
    
    return closest
