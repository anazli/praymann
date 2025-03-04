import unittest

import numpy as np

from montyray.math_tools.vector3d import Vector3D


class TestVector3D(unittest.TestCase):

    def test_init_with_invalid_data(self):
        with self.assertRaises(TypeError):
            v = Vector3D("[1, 2, 3]")

        with self.assertRaises(TypeError):
            v = Vector3D(np.array([0, 1, 2, 3]))

        with self.assertRaises(TypeError):
            v = Vector3D("1", "2", "3")

    def test_length(self):
        v = Vector3D(np.array([1, 2, -3]))
        self.assertEqual(3.7416573867739413, v.length())

    def test_normalized(self):
        v = Vector3D(np.array([-1, 2, 3]))
        vn = v.normalized()
        self.assertAlmostEqual(-0.26726124, vn[0])
        self.assertAlmostEqual(0.53452248, vn[1])
        self.assertAlmostEqual(0.80178373, vn[2])

    def test_operators(self):
        a = Vector3D(1, 2, 3)
        b = Vector3D(5, 6, 7)
        c = Vector3D(-0.7, 4.5, -0.232)
        res = -a + b - c * np.abs(a)
        self.assertAlmostEqual(4.7, res.x)
        self.assertAlmostEqual(-5.0, res.y)
        self.assertAlmostEqual(4.696, res.z)


if __name__ == "__main__":
    unittest.main()
