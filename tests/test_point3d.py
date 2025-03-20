# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import pytest

import numpy as np

from raymann.math_tools.point3d import Point3D


class TestPoint3D:
    
    def setup_method(self):
        self.eps = 1E-8

    def test_init_with_invalid_data(self):
        with pytest.raises(TypeError):
            p = Point3D("[1, 2, 3]")

        with pytest.raises(TypeError):
            p = Point3D(np.array([0, 1, 2]))

    def test_operators(self):
        a = Point3D(1, 2, 3)
        b = Point3D(5, 6, 7)
        c = Point3D(-0.7, 4.5, -0.232)
        res = -a + b - c * np.abs(a)
        assert abs(4.7 - res.x) < self.eps
        assert abs(-5.0 - res.y) < self.eps
        assert abs(4.696 - res.z) < self.eps

    def test_coordinate_modifiers(self):
        v = Point3D()
        with pytest.raises(TypeError):
            v.coordinates = ["2", "3"]
        with pytest.raises(TypeError):
            v.x = "1"
        with pytest.raises(TypeError):
            v.y = "2"
        with pytest.raises(TypeError):
            v.z = "3"
