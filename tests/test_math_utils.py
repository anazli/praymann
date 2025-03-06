import unittest
import numpy as np

from raymann.math_tools.math_utils import *
from raymann.math_tools.vector4d import Vector4D
from raymann.math_tools.vector3d import Vector3D
from raymann.math_tools.vector2d import Vector2D
from raymann.math_tools.point3d import Point3D


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

    def test_translation_matrix(self):
        p = Point3D(-3, 4, 5)
        m = translation_matrix(5, -3, 2)
        res = m * p
        self.assertEqual(Point3D(2, 1, 7), res)

        m = m.inverse
        res = m * p
        self.assertEqual(Point3D(-8, 7, 3), res)

    def test_scale_matrix(self):
        p = Point3D(-4, 6, 8)
        m = scale_matrix(2, 3, 4)
        res = m * p
        self.assertEqual(Point3D(-8, 18, 32), res)

        m = m.inverse
        res = m * p
        self.assertEqual(Point3D(-2, 2, 2), res)

    def test_x_rot_matrix(self):
        p = Point3D(0, 1, 0)
        m = x_rot_matrix(np.pi / 4.0)
        res = m * p
        self.assertAlmostEqual(0, res.x)
        self.assertAlmostEqual(np.sqrt(2) / 2.0, res.y)
        self.assertAlmostEqual(np.sqrt(2) / 2.0, res.z)

        m = m.inverse
        res = m * p
        self.assertAlmostEqual(0, res.x)
        self.assertAlmostEqual(np.sqrt(2) / 2.0, res.y)
        self.assertAlmostEqual(-np.sqrt(2) / 2.0, res.z)

    def test_y_rot_matrix(self):
        p = Point3D(0, 0, 1)
        m = y_rot_matrix(np.pi / 4.0)
        res = m * p
        self.assertAlmostEqual(np.sqrt(2) / 2.0, res.x)
        self.assertAlmostEqual(0, res.y)
        self.assertAlmostEqual(np.sqrt(2) / 2.0, res.z)

    def test_z_rot_matrix(self):
        p = Point3D(0, 1, 0)
        m = z_rot_matrix(np.pi / 4.0)
        res = m * p
        self.assertAlmostEqual(-np.sqrt(2) / 2.0, res.x)
        self.assertAlmostEqual(np.sqrt(2) / 2.0, res.y)
        self.assertAlmostEqual(0, res.z)

    def test_transformation_chaining(self):
        p = Point3D(1, 0, 1)
        a = x_rot_matrix(np.pi / 2.0)
        b = scale_matrix(5, 5, 5)
        c = translation_matrix(10, 5, 7)

        m = c * b * a
        res = m * p
        self.assertEqual(Point3D(15, 0, 7), res)
