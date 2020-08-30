import unittest
import expo_sum
import expo_sum2

class TestRenumber(unittest.TestCase):

    def test_expo_sum(self):
        assert(expo_sum.expo_sum(3, 5) == 3**5)
        assert(expo_sum.expo_sum(0, 5) == 0)
        assert(expo_sum.expo_sum(2, 0) == 1)

    def test_expo_sum2(self):
        assert(expo_sum2.expo_sum(3, 5) == 3**5)
        assert(expo_sum2.expo_sum(0, 5) == 0)
        assert(expo_sum2.expo_sum(2, 0) == 1)

if __name__ == "__main__":
    unittest.main()
