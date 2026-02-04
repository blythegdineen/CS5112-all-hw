import unittest
import json
import sys
import itertools
sys.path.append("..")

import problem_3.p3_a as p3_a
import problem_3.p3_b as p3_b


class TestProblem3(unittest.TestCase):
    ### Public tests for 3a
    def test_correctness_public_a1(self):
        """Public test """
        self.assertEqual(1, 4)
        cost_matrix = p3_a.cost_matrix_greedy_approach()
        self.assertEqual(len(cost_matrix), 4)

    ### Public tests for 3a
    def test_correctness_public_a2(self):
        """Public test """
        self.assertEqual(1, 4)
        cost_matrix = p3_a.cost_matrix_greedy_approach()
        self.assertEqual(len(cost_matrix[0]), 4)

    ## Public tests for 3a
    def test_correctness_public_a3(self):
        """Public test """
        cost_matrix = p3_a.cost_matrix_greedy_approach()
        seq_to_cost = {}
        greedy_sol = tuple(p3_a.greedy_solution(cost_matrix))
        for sequence in list(itertools.permutations(list(range(1, 5, 1)), 4)):
          seq_to_cost[sequence] = p3_a.compute_cost(cost_matrix, sequence)
        self.assertAlmostEqual(seq_to_cost[greedy_sol], max(seq_to_cost.values()))

    def test_correctness_public_a1(self):
        """Public test """
        cost_matrix = [
          [float('inf'), 3, 5],
          [3, float('inf'), 7],
          [5, 7, float('inf')]]
        
        self.assertEqual(p3_b.local_search_2opt(cost_matrix, (2, 3, 1)),
                        (2, 1, 3))

    def test_correctness_public_a2(self):
        """Public test """
        cost_matrix = [
          [float('inf'), 3, 5],
          [3, float('inf'), 7],
          [5, 7, float('inf')]]
        cost_matrix = [
          [ float('inf'), 17,  3, 13, 13,  6, 14, 18],
          [17, float('inf'),  8, 10,  3, 12, 11, 16],
          [ 3,  8,  float('inf'), 13, 12,  3, 18,  9],
          [13, 10, 13, float('inf'), 10, 17, 17, 10],
          [13,  3, 12, 10, float('inf'),  5,  9,  9],
          [ 6, 12,  3, 17,  5, float('inf'),  9, 18],
          [14, 11, 18, 17,  9,  9, float('inf'),  3],
          [18, 16,  9, 10,  9, 18,  3, float('inf')]]
        self.assertEqual(
          p3_b.local_search_2opt(cost_matrix, (6, 1, 2, 5, 3, 8, 7, 4)),
          (2, 5, 6, 1, 3, 8, 7, 4))


if __name__ == '__main__':
    unittest.main()
