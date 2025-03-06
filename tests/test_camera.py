import unittest
import numpy as np
from montyray.camera.camera import Camera
from montyray.math_tools.math_utils import y_rot_matrix, translation_matrix
from montyray.math_tools.matrix4d import Matrix4D
from montyray.math_tools.point3d import Point3D
from montyray.math_tools.vector3d import Vector3D


class TestCamera(unittest.TestCase):
    def test_pixel_size(self):
        c = Camera(200, 125, np.pi / 2, Matrix4D())
        self.assertAlmostEqual(0.01, c.pixel_size)

        c = Camera(125, 200, np.pi / 2, Matrix4D())
        self.assertAlmostEqual(0.01, c.pixel_size)

    def test_ray_through_the_screen_center(self):
        c = Camera(201, 101, np.pi / 2, Matrix4D())
        ray = c.get_ray(100, 50)
        self.assertEqual(Point3D(), ray.origin)
        self.assertAlmostEqual(0, ray.direction.x)
        self.assertAlmostEqual(0, ray.direction.y)
        self.assertAlmostEqual(-1, ray.direction.z)

    def test_ray_through_the_screen_corners(self):
        c = Camera(201, 101, np.pi / 2, Matrix4D())
        ray = c.get_ray(0, 0)
        self.assertEqual(Point3D(), ray.origin)
        self.assertAlmostEqual(0.66519, ray.direction.x, 5)
        self.assertAlmostEqual(0.33259, ray.direction.y, 5)
        self.assertAlmostEqual(-0.66851, ray.direction.z, 5)

    def test_camera_transform(self):
        c = Camera(
            201,
            101,
            np.pi / 2,
            Matrix4D(y_rot_matrix(np.pi / 4) * translation_matrix(0, -2, 5)),
        )
        ray = c.get_ray(100, 50)
        self.assertAlmostEqual(0, ray.origin.x)
        self.assertAlmostEqual(2, ray.origin.y)
        self.assertAlmostEqual(-5, ray.origin.z)
        self.assertAlmostEqual(np.sqrt(2) / 2, ray.direction.x)
        self.assertAlmostEqual(0, ray.direction.y)
        self.assertAlmostEqual(-np.sqrt(2) / 2, ray.direction.z)
