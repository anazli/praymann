import unittest

import numpy as np

from montyray.math_tools.vector2d import Vector2D


class TestVector2D(unittest.TestCase):

    def test_init_with_invalid_data(self):
        with self.assertRaises(TypeError):
            v = Vector2D("[1, 2]")

        with self.assertRaises(TypeError):
            v = Vector2D(np.array([0, 1, 2]))

        with self.assertRaises(TypeError):
            v = Vector2D("1", "2")

    def test_length(self):
        v = Vector2D(np.array([2, -3]))
        self.assertEqual(3.605551275463989, v.length())

    def test_normalized(self):
        v = Vector2D(np.array([-1, 2]))
        vn = v.normalized()
        self.assertAlmostEqual(-0.4472136, vn[0])
        self.assertAlmostEqual(0.89442719, vn[1])

    def test_operators(self):
        a = Vector2D(-1.55, 6.243)
        b = Vector2D(5, -6)
        c = Vector2D(-0.7, -0.232)
        res = -a + b - c * np.abs(a)
        self.assertAlmostEqual(7.635, res.x)
        self.assertAlmostEqual(-10.794624, res.y)

    def test_coordinate_modifiers(self):
        v = Vector2D()
        with self.assertRaises(TypeError):
            v.coordinates = ["2", "3", "4"]
        with self.assertRaises(TypeError):
            v.x = "1"
        with self.assertRaises(TypeError):
            v.y = "2"


if __name__ == "__main__":
    unittest.main()
