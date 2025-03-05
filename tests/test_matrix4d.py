import numpy as np
import unittest

from montyray.math_tools.matrix4d import Matrix4D


class TestMatrix4D(unittest.TestCase):

    def test_matrix(self):
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

        self.assertTrue(np.allclose(test_mat, res.data))
        a[0, 2] = 3.14
        self.assertEqual(3.14, a[0, 2])
