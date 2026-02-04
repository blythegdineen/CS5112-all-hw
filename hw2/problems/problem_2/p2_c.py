'''
Problem 2c
'''

import math
from collections import defaultdict

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def closest_pair(points):
    if len(points) < 2:
        return []
    
    best_dist = d(points[0],points[1])
    closest = [points[0],points[1]]
    subsquares = defaultdict(list)

    def get_subsquare(point,dist):
        return (int(point[0] // dist), int(point[1] // dist))
    
    subsquares[get_subsquare(points[0],best_dist)].append(points[0])
    subsquares[get_subsquare(points[1],best_dist)].append(points[1])


    for i in range(2,len(points)):
        point_i = points[i]
        
        #determine subsquare sst containing pi
        pi_x, pi_y = get_subsquare(point_i, best_dist)

        # look up the 25 subsquares close to pi
        near_points = []
        for x in range(-2,3):
            for y in range(-2,3):
                subsq = (pi_x+x, pi_y+y)
                if subsq in subsquares:
                    near_points.extend(subsquares[subsq])

        # if there is a point pj (j<i) st that d' = d(pj, pi) < d:
        for point_j in near_points:
            if point_j == point_i:
                continue
            dist = d(point_i, point_j)
            if dist < best_dist:
                # update best points  
                best_dist = dist
                closest = [point_i, point_j]      
                # delete current dict
                subsquares.clear()
                # make dict for storing subsquares
                for k in range(i+1):
                    subsquares[get_subsquare(points[k],best_dist)].append(points[k])
                break
        
        # else insert pi into the currect dictionary
        else:
            subsquares[get_subsquare(point_i,best_dist)].append(point_i)
    
    return closest
