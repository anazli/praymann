# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import unittest

import numpy as np

from raymann.math_tools.point3d import Point3D


class TestPoint3D(unittest.TestCase):

    def test_init_with_invalid_data(self):
        with self.assertRaises(TypeError):
            p = Point3D("[1, 2, 3]")

        with self.assertRaises(TypeError):
            p = Point3D(np.array([0, 1, 2]))

    def test_operators(self):
        a = Point3D(1, 2, 3)
        b = Point3D(5, 6, 7)
        c = Point3D(-0.7, 4.5, -0.232)
        res = -a + b - c * np.abs(a)
        self.assertAlmostEqual(4.7, res.x)
        self.assertAlmostEqual(-5.0, res.y)
        self.assertAlmostEqual(4.696, res.z)

    def test_coordinate_modifiers(self):
        v = Point3D()
        with self.assertRaises(TypeError):
            v.coordinates = ["2", "3"]
        with self.assertRaises(TypeError):
            v.x = "1"
        with self.assertRaises(TypeError):
            v.y = "2"
        with self.assertRaises(TypeError):
            v.z = "3"


if __name__ == "__main__":
    unittest.main()
