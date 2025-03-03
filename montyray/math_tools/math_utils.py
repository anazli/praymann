import numpy as np

from montyray.math_tools.vector3d import Vector3D


def dot(elem1, elem2):
    """dot product of two math entities"""
    if isinstance((elem1, elem2), Vector3D):
        return np.dot(elem1, elem2)
    else:
        raise TypeError("Cannot calculate the dot product of the given elements!")


def cross(elem1, elem2):
    """cross product of two math entities"""
    if isinstance((elem1, elem2), Vector3D):
        return np.cross(elem1, elem2)
    else:
        raise TypeError("Cannot calculate the cross product of the given elements!")
