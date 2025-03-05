import unittest

import numpy as np

from montyray.math_tools.ray import Ray
from montyray.math_tools.vector3d import Vector3D
from montyray.math_tools.point3d import Point3D


class TestRay(unittest.TestCase):

    def test_ray(self):
        o = Point3D(2, 3, 4)
        d = Vector3D(1, 0, 0)
        ray = Ray(origin=o, direction=d)

        self.assertEqual(o, ray.origin)
        self.assertEqual(d, ray.direction)

        self.assertEqual(o, ray.position(0))
        self.assertEqual(Point3D(3, 3, 4), ray.position(1))
        self.assertEqual(Point3D(1, 3, 4), ray.position(-1))
        self.assertEqual(Point3D(4.5, 3, 4), ray.position(2.5))


if __name__ == "__main__":
    unittest.main()
