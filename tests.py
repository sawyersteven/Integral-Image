import unittest
from integral_image import IntegralImage


orig = [[5, 2, 3, 4, 1],
        [1, 5, 4, 2, 3],
        [2, 2, 1, 3, 4],
        [3, 5, 6, 4, 5],
        [4, 1, 3, 2, 6]]

image = [[5, 7, 10, 14, 15],
         [6, 13, 20, 26, 30],
         [8, 17, 25, 34, 42],
         [11, 25, 39, 52, 65],
         [15, 30, 47, 62, 81]]


class TestIntegralImage(unittest.TestCase):

    def test_create(self):
        ii = IntegralImage(orig)
        self.assertEqual(ii.table, image)

    def test_box_sum(self):
        ii = IntegralImage(orig)
        self.assertEqual(ii.box_sum(1, 1, 3, 2), 17)

if __name__ == '__main__':
    unittest.main()
