import unittest

from montyray.math_tools.math_utils import dot, cross
from montyray.math_tools.vector3d import Vector3D
from montyray.math_tools.vector2d import Vector2D


class TestMathUtils(unittest.TestCase):
    def test_dot_product(self):
        with self.assertRaises(TypeError):
            d = dot(Vector3D(1, 2, 3), Vector2D(3, 4))
        a = dot(Vector3D(1, 2, 3), Vector3D(3, 4, 5))
        self.assertEqual(26, a)
