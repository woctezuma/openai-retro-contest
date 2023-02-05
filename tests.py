import unittest

import random_agent


class TestRandomAgentMethods(unittest.TestCase):
    def test_run(self):
        self.assertTrue(random_agent.run(display_on_screen=False, num_steps=400))


if __name__ == '__main__':
    unittest.main()
