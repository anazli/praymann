# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np
import pytest

from raymann.math_tools.matrix4d import Matrix4D
from raymann.math_tools.vector4d import Vector4D


class TestMatrix4D:
    
    def test_matrix_operations(self):
        a = Matrix4D()
        b = Matrix4D(
            np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        )
        c = Matrix4D(
            np.array(
                [[0, 2, -1, 4], [5, 6, -0.3, 8], [9, 10, -8, 12], [13, 45.5, 15, 0.0]]
            )
        )
        res = a + b * c.inverse - b
        test_mat = np.array(
            [
                [0.2955174, -0.9560857, -3.46111533, -4.00534873],
                [-5.49029023, -2.4137669, -7.89405865, -7.99112597],
                [-10.27609786, -5.87144811, -11.32700198, -11.97690321],
                [-15.06190549, -8.32912931, -16.7599453, -14.96268044],
            ]
        )

        assert np.allclose(test_mat, res.data)
        a[0, 2] = 3.14
        assert 3.14 == a[0, 2]


    def test_matrix_vector_multiplication(self):
        m = Matrix4D()
        v = Vector4D(-0.8, 3.14, -5, 44.0)
        res = m * v
        assert v == res
