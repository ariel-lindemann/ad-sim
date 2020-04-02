import unittest

import environment

class TestEnvironment(unittest.TestCase):

    def test_environment_init(self):
        env = environment.Environment()

        # TODO

    def test_bounded_environment_init(self):
        x = [0, 100]
        y = [-50, 50]
        
        benv = environment.BoundedEnvironment(x, y)

        self.assertEqual(benv.x_min, x[0])
        self.assertEqual(benv.x_max, x[1])
        self.assertEqual(benv.y_min, y[0])
        self.assertEqual(benv.y_max, y[1])