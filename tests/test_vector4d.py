# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import unittest

import numpy as np

from raymann.math_tools.vector4d import Vector4D


class TestVector4D(unittest.TestCase):

    def test_init_with_invalid_data(self):
        with self.assertRaises(TypeError):
            v = Vector4D("[1, 2, 3, 4]")

        with self.assertRaises(TypeError):
            v = Vector4D(np.array([0, 1, 2, 3]))

    def test_length(self):
        v = Vector4D(1, 2, -3, -0.92785)
        self.assertEqual(3.8549845165058705, v.length())

    def test_normalized(self):
        v = Vector4D(-1, 2, 3, -45.32)
        vn = v.normalized()
        self.assertAlmostEqual(-0.02199049, vn.x)
        self.assertAlmostEqual(0.04398099, vn.y)
        self.assertAlmostEqual(0.06597148, vn.z)
        self.assertAlmostEqual(-0.99660918, vn.w)

    def test_operators(self):
        a = Vector4D(1, 2, 3, 4)
        b = Vector4D(5, 6, 7, 8)
        c = Vector4D(-0.7, 4.5, -0.232, 0.0)
        res = -a + b - c * np.abs(a)
        self.assertAlmostEqual(4.7, res.x)
        self.assertAlmostEqual(-5.0, res.y)
        self.assertAlmostEqual(4.696, res.z)
        self.assertAlmostEqual(4.0, res.w)

    def test_coordinate_modifiers(self):
        v = Vector4D()
        with self.assertRaises(TypeError):
            v.coordinates = ["2", "3", "4", "5", "6"]
        with self.assertRaises(TypeError):
            v.x = "1"
        with self.assertRaises(TypeError):
            v.y = "2"
        with self.assertRaises(TypeError):
            v.z = "3"
        with self.assertRaises(TypeError):
            v.z = ","


if __name__ == "__main__":
    unittest.main()
