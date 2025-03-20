# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import pytest

import numpy as np

from raymann.math_tools.vector2d import Vector2D


class TestVector2D:

    def setup_method(self):
        self.eps = 1E-8

    def test_init_with_invalid_data(self):
        with pytest.raises(TypeError):
            v = Vector2D("[1, 2]")

        with pytest.raises(TypeError):
            v = Vector2D(np.array([0, 1]))

    def test_length(self):
        v = Vector2D(2, -3)
        assert 3.605551275463989 == v.length()

    def test_normalized(self):
        v = Vector2D(-1, 2)
        vn = v.normalized()
        assert abs(-0.4472136 - vn.x) <= self.eps
        assert abs(0.89442719 - vn.y) <= self.eps

    def test_operators(self):
        a = Vector2D(-1.55, 6.243)
        b = Vector2D(5, -6)
        c = Vector2D(-0.7, -0.232)
        res = -a + b - c * np.abs(a)
        assert abs(7.635 - res.x) < self.eps
        assert abs(-10.794624 - res.y) < self.eps

    def test_coordinate_modifiers(self):
        v = Vector2D()
        with pytest.raises(TypeError):
            v.coordinates = ["2", "3", "4"]
        with pytest.raises(TypeError):
            v.x = "1"
        with pytest.raises(TypeError):
            v.y = "2"
