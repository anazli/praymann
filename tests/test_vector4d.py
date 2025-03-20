# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import pytest

import numpy as np

from raymann.math_tools.vector4d import Vector4D


class TestVector4D:
    
    def setup_method(self):
        self.eps = 1E-8

    def test_init_with_invalid_data(self):
        with pytest.raises(TypeError):
            v = Vector4D("[1, 2, 3, 4]")

        with pytest.raises(TypeError):
            v = Vector4D(np.array([0, 1, 2, 3]))

    def test_length(self):
        v = Vector4D(1, 2, -3, -0.92785)
        assert 3.8549845165058705 == v.length()

    def test_normalized(self):
        v = Vector4D(-1, 2, 3, -45.32)
        vn = v.normalized()
        assert abs(-0.02199049 - vn.x) < self.eps
        assert abs(0.04398099 - vn.y) < self.eps
        assert abs(0.06597148 - vn.z) < self.eps
        assert abs(-0.99660918 - vn.w) < self.eps

    def test_operators(self):
        a = Vector4D(1, 2, 3, 4)
        b = Vector4D(5, 6, 7, 8)
        c = Vector4D(-0.7, 4.5, -0.232, 0.0)
        res = -a + b - c * np.abs(a)
        assert abs(4.7 - res.x) < self.eps
        assert abs(-5.0 - res.y) < self.eps
        assert abs(4.696 - res.z) < self.eps
        assert abs(4.0 - res.w) < self.eps

    def test_coordinate_modifiers(self):
        v = Vector4D()
        with pytest.raises(TypeError):
            v.coordinates = ["2", "3", "4", "5", "6"]
        with pytest.raises(TypeError):
            v.x = "1"
        with pytest.raises(TypeError):
            v.y = "2"
        with pytest.raises(TypeError):
            v.z = "3"
        with pytest.raises(TypeError):
            v.z = ","
