import numpy as np


class Matrix2D:
    def __init__(self, mat=None):
        if isinstance(mat, Matrix2D):
            self._data = mat._data
        elif mat is None:
            self._data = np.matrix(np.identity(2))
        else:
            raise TypeError()

    @property
    def identity(self):
        return np.matrix(np.identity(2))

    @property
    def determinant(self):
        return np.linalg.det(self._data)
