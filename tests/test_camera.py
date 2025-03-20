# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import pytest
import numpy as np
from raymann.camera.camera import Camera
from raymann.math_tools.math_utils import y_rot_matrix, translation_matrix
from raymann.math_tools.matrix4d import Matrix4D
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.vector3d import Vector3D


class TestCamera:

    def setup_method(self):
        self.eps = 1E-5

    def test_pixel_size(self):
        c = Camera(200, 125, np.pi / 2, Matrix4D())
        assert abs(0.01 - c.pixel_size) < self.eps

        c = Camera(125, 200, np.pi / 2, Matrix4D())
        assert abs(0.01 - c.pixel_size) < self.eps

    def test_ray_through_the_screen_center(self):
        c = Camera(201, 101, np.pi / 2, Matrix4D())
        ray = c.get_ray(100, 50)
        assert Point3D() == ray.origin
        assert abs(0 - ray.direction.x) < self.eps
        assert abs(0 - ray.direction.y) < self.eps
        assert abs(-1 - ray.direction.z) < self.eps

    def test_ray_through_the_screen_corners(self):
        c = Camera(201, 101, np.pi / 2, Matrix4D())
        ray = c.get_ray(0, 0)
        assert Point3D() == ray.origin
        assert abs(0.66519 - ray.direction.x) < self.eps
        assert abs(0.33259 - ray.direction.y) < self.eps
        assert abs(-0.66851 - ray.direction.z) < self.eps

    def test_camera_transform(self):
        c = Camera(
            201,
            101,
            np.pi / 2,
            Matrix4D(y_rot_matrix(np.pi / 4) * translation_matrix(0, -2, 5)),
        )
        ray = c.get_ray(100, 50)
        assert abs(0 - ray.origin.x) < self.eps
        assert abs(2 - ray.origin.y) < self.eps
        assert abs(-5 - ray.origin.z) < self.eps
        assert abs(np.sqrt(2) / 2 - ray.direction.x) < self.eps
        assert abs(0 - ray.direction.y) < self.eps
        assert abs(-np.sqrt(2) / 2 - ray.direction.z) < self.eps
