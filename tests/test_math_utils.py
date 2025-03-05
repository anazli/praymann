import unittest
import numpy as np

from montyray.math_tools.math_utils import dot, cross
from montyray.math_tools.vector3d import Vector3D
from montyray.math_tools.vector2d import Vector2D
from montyray.math_tools.point3d import Point3D


class TestMathUtils(unittest.TestCase):
    def test_dot_product(self):
        with self.assertRaises(TypeError):
            d = dot(Vector3D(1, 2, 3), Vector2D(3, 4))
        a = dot(Vector3D(1, 2, 3), Vector3D(3, 4, 5))
        self.assertEqual(26, a)

    def test_cross_product(self):
        with self.assertRaises(TypeError):
            c = cross(Vector3D(), Point3D())

        c = cross(Vector3D(4.5, -0.68, 7.3), Vector3D(0.0, -13.4, -0.44))
        self.assertAlmostEqual(98.1192, c.coordinates[0])
        self.assertAlmostEqual(1.98, c.coordinates[1])
        self.assertAlmostEqual(-60.3, c.coordinates[2])
