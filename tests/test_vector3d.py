# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import pytest

import numpy as np

from raymann.math_tools.vector3d import Vector3D


class TestVector3D:
    
    def setup_method(self):
        self.eps = 1E-8

    def test_init_with_invalid_data(self):
        with pytest.raises(TypeError):
            v = Vector3D("[1, 2, 3]")

        with pytest.raises(TypeError):
            v = Vector3D(np.array([0, 1, 2]))

    def test_length(self):
        v = Vector3D(1, 2, -3)
        assert 3.7416573867739413 == v.length()

    def test_normalized(self):
        v = Vector3D(-1, 2, 3)
        vn = v.normalized()
        assert abs(-0.26726124 - vn.x) < self.eps
        assert abs(0.53452248 - vn.y) < self.eps
        assert abs(0.80178373 - vn.z) < self.eps

    def test_operators(self):
        a = Vector3D(1, 2, 3)
        b = Vector3D(5, 6, 7)
        c = Vector3D(-0.7, 4.5, -0.232)
        res = -a + b - c * np.abs(a)
        assert abs(4.7 - res.x) < self.eps
        assert abs(-5.0 - res.y) < self.eps
        assert abs(4.696 - res.z) < self.eps

    def test_coordinate_modifiers(self):
        v = Vector3D()
        with pytest.raises(TypeError):
            v.coordinates = ["2", "3"]
        with pytest.raises(TypeError):
            v.x = "1"
        with pytest.raises(TypeError):
            v.y = "2"
        with pytest.raises(TypeError):
            v.z = "3"
