import unittest
import sys
sys.path.append("..")


from problem_1.p1_a import is_bipartite
from problem_1.p1_b import maximal_bipartite_match


class TestProblem1(unittest.TestCase):
    ### Public tests for 1a
    def test_correctness_public_a1(self):
        """Public test """
        g_l = {0: [2, 4], 1: [4, 7], 2: [7], 3: [6], 4: [6], 5: [6], 6: [], 7: []}
        # sort g_l by key

        
        self.assertEqual(is_bipartite(g_l), False)
        # pass

    def test_correctness_public_a2(self):
        """Public test """
        g_l = {0: [1], 1: [3, 6, 7], 2: [4, 6], 3: [4], 4: [8], 5: [8], 6: [7], 7: [8], 8: []}
        # sort g_l by key
        
        self.assertEqual(is_bipartite(g_l), False)
        # pass

    def test_correctness_public_a3(self):
        """Public test """
        g_l = {0: [2], 1: [3], 2: [], 3: []}
        self.assertEqual(is_bipartite(g_l), True)
        # pass

    def test_correctness_public_a4(self):
        """Public test """
        g_l = {0: [1, 3, 4], 1: [7], 2: [3, 6], 3: [6], 4: [5, 7], 5: [], 6: [], 7: []}
        # sort g_l by key
        self.assertEqual(is_bipartite(g_l), False)
        # pass

    def test_correctness_public_a5(self):
        """Public test """
        g_l = {0: [2, 3], 1: [3], 2: [6, 7], 3: [], 4: [6, 7], 5: [8], 6: [], 7: [], 8: []}
        # sort g_l by key
        
        self.assertEqual(is_bipartite(g_l), True)
        # pass

    def test_correctness_public_a6(self):
        """Public test """
        g_l = {0: [2], 1: [6], 2: [3], 3: [], 4: [5], 5: [], 6: []}
        # sort g_l by key
        
        self.assertEqual(is_bipartite(g_l), True)

    def test_correctness_public_a7(self):
        """Public test """
        g_l = {0: [1, 3, 8], 1: [2, 4, 5, 6, 8], 2: [4, 5], 3: [4, 6], 4: [6], 5: [], 6: [], 7: [8], 8: []} 
        # sort g_l by key
        
        self.assertEqual(is_bipartite(g_l), False)

    def test_correctness_public_a8(self):
        """Public test """
        g_l = {0: [2, 3, 4], 1: [4, 6], 2: [3, 5, 6], 3: [], 4: [6], 5: [6], 6: []}
        # sort g_l by key
        
        self.assertEqual(is_bipartite(g_l), False)

    def test_correctness_public_a9(self):
        """Public test """
        g_l = {0: [4, 5, 6, 7], 1: [6, 7], 2: [4, 6, 7], 3: [4, 5, 6], 4: [], 5: [], 6: [], 7: []}
        # sort g_l by key
        
        self.assertEqual(is_bipartite(g_l), True)
    #     # pass

    ### Public tests for 1b
    def test_correctness_public_b1(self):
        """Public test """
        g_l = [[0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
        self.assertEqual(maximal_bipartite_match(g_l), 4)

    def test_correctness_public_b2(self):
        """Public test """
        g_l = [[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 3)
        
    def test_correctness_public_b3(self):
        """Public test """
        g_l = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 5)
        
    def test_correctness_public_b4(self):
        """Public test """
        g_l = [[0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 2)
        
    def test_correctness_public_b5(self):
        """Public test """
        g_l = [[1, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 4)
        
    def test_correctness_public_b6(self):
        """Public test """
        g_l = [[0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 3)
        
    def test_correctness_public_b7(self):
        """Public test """
        g_l = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 2)
        
if __name__ == '__main__':
    unittest.main()
