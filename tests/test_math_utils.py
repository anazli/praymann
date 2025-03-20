# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import pytest
import numpy as np

from raymann.math_tools.math_utils import *
from raymann.math_tools.vector4d import Vector4D
from raymann.math_tools.vector3d import Vector3D
from raymann.math_tools.vector2d import Vector2D
from raymann.math_tools.point3d import Point3D


class TestMathUtils:
    
    def setup_method(self):
        self.eps = 1E-8

    def test_dot_product(self):
        with pytest.raises(TypeError):
            d = dot(Vector3D(1, 2, 3), Vector2D(3, 4))
        a = dot(Vector3D(1, 2, 3), Vector3D(3, 4, 5))
        assert 26 == a

    def test_cross_product(self):
        with pytest.raises(TypeError):
            c = cross(Vector3D(), Point3D())

        c = cross(Vector3D(4.5, -0.68, 7.3), Vector3D(0.0, -13.4, -0.44))
        assert abs(98.1192 - c.coordinates[0]) < self.eps
        assert abs(1.98 - c.coordinates[1]) < self.eps
        assert abs(-60.3 - c.coordinates[2]) < self.eps

    def test_translation_matrix(self):
        p = Point3D(-3, 4, 5)
        m = translation_matrix(5, -3, 2)
        res = m * p
        assert Point3D(2, 1, 7) == res

        m = m.inverse
        res = m * p
        assert Point3D(-8, 7, 3) == res

    def test_scale_matrix(self):
        p = Point3D(-4, 6, 8)
        m = scale_matrix(2, 3, 4)
        res = m * p
        assert Point3D(-8, 18, 32) == res

        m = m.inverse
        res = m * p
        assert Point3D(-2, 2, 2) == res

    def test_x_rot_matrix(self):
        p = Point3D(0, 1, 0)
        m = x_rot_matrix(np.pi / 4.0)
        res = m * p
        assert abs(0 - res.x) < self.eps
        assert abs(np.sqrt(2) / 2.0 - res.y) < self.eps
        assert abs(np.sqrt(2) / 2.0 - res.z) < self.eps

        m = m.inverse
        res = m * p
        assert abs(0 - res.x) < self.eps
        assert abs(np.sqrt(2) / 2.0 - res.y) < self.eps
        assert abs(-np.sqrt(2) / 2.0 - res.z) < self.eps

    def test_y_rot_matrix(self):
        p = Point3D(0, 0, 1)
        m = y_rot_matrix(np.pi / 4.0)
        res = m * p
        assert abs(np.sqrt(2) / 2.0 - res.x) < self.eps
        assert abs(0 - res.y) < self.eps
        assert abs(np.sqrt(2) / 2.0 - res.z) < self.eps

    def test_z_rot_matrix(self):
        p = Point3D(0, 1, 0)
        m = z_rot_matrix(np.pi / 4.0)
        res = m * p
        assert abs(-np.sqrt(2) / 2.0 - res.x) < self.eps
        assert abs(np.sqrt(2) / 2.0 - res.y) < self.eps
        assert abs(0 - res.z) < self.eps

    def test_transformation_chaining(self):
        p = Point3D(1, 0, 1)
        a = x_rot_matrix(np.pi / 2.0)
        b = scale_matrix(5, 5, 5)
        c = translation_matrix(10, 5, 7)

        m = c * b * a
        res = m * p
        assert Point3D(15, 0, 7) == res
