def greedy_solution(cost_matrix):
  n = len(cost_matrix)
  min_edge_cost = float('inf')
  min_i = None
  min_j = None
  for i in range(n):
    for j in range(n):
      if min_edge_cost > cost_matrix[i][j]:
        min_i, min_j = i, j
        min_edge_cost = cost_matrix[i][j]
  sequence = [min_i, min_j]
  r = min_j
  for _ in range(n - 2):
    # print(sequence)
    min_entry = float('inf')
    min_col = None
    for j in range(n):
      if j not in sequence and min_entry > cost_matrix[r][j]:
        min_entry = cost_matrix[r][j]
        min_col = j
    sequence.append(min_col)
    r = min_col
  return [i+1 for i in sequence]

import os
def cost_matrix_greedy_approach():  
  cost_matrix = []
  cur_path = os.path.dirname(__file__)
  with open(os.path.join(cur_path, 'p3_a.txt'), 'r') as f:
    for line in f.readlines():
      cost_matrix.append(line.strip().split(','))
  n = len(cost_matrix)
  for i in range(n):
    for j in range(n):
      if 'inf' in cost_matrix[i][j]:
        cost_matrix[i][j] = float('inf')
      else:
        cost_matrix[i][j] = float(cost_matrix[i][j].strip())
  return cost_matrix


def compute_cost(cost_matrix, sequence):
  sum = 0
  for i in range(len(sequence) - 1):
    sum += cost_matrix[sequence[i] - 1][sequence[i+1] - 1]
  return sum