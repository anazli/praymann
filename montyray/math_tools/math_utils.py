import numpy as np

from montyray.math_tools.matrix4d import Matrix4D
from montyray.math_tools.vector3d import Vector3D
from montyray.math_tools.vector2d import Vector2D
from montyray.math_tools.vector4d import Vector4D
from montyray.math_tools.point3d import Point3D


def dot(elem1, elem2):
    """dot product of two math entities"""
    if (
        (isinstance(elem1, Vector2D) and isinstance(elem2, Vector2D))
        or (isinstance(elem1, Vector3D) and isinstance(elem2, Vector3D))
        or (isinstance(elem1, Vector4D) and isinstance(elem2, Vector4D))
    ):
        return np.dot(elem1.coordinates, elem2.coordinates)
    else:
        raise TypeError("Cannot calculate the dot product of the given elements!")


def cross(elem1, elem2):
    """cross product of two math entities"""
    if isinstance(elem1, Vector2D) and isinstance(elem2, Vector2D):
        new_data = np.cross(elem1.coordinates, elem2.coordinates)
        ret = Vector2D()
        ret.coordinates = new_data
        return ret
    elif isinstance(elem1, Vector3D) and isinstance(elem2, Vector3D):
        new_data = np.cross(elem1.coordinates, elem2.coordinates)
        ret = Vector3D()
        ret.coordinates = new_data
        return ret
    elif isinstance(elem1, Vector4D) and isinstance(elem2, Vector4D):
        new_data = np.cross(elem1.coordinates, elem2.coordinates)
        ret = Vector4D()
        ret.coordinates = new_data
        return ret
    else:
        raise TypeError("Cannot calculate the cross product of the given elements!")


def identity_matrix():
    return Matrix4D(np.identity(4))


def zero_matrix():
    return Matrix4D(np.zeros((4, 4)))


def translation_matrix(x, y, z):
    if (
        isinstance(x, (int, float))
        and isinstance(y, (int, float))
        and isinstance(z, (int, float))
    ):
        m = np.identity(4)
        m[0, 3] = x
        m[1, 3] = y
        m[2, 3] = z
        return Matrix4D(m)
    else:
        raise TypeError()


def scale_matrix(x, y, z):
    if (
        isinstance(x, (int, float))
        and isinstance(y, (int, float))
        and isinstance(z, (int, float))
    ):
        m = np.identity(4)
        m[0, 0] = x
        m[1, 1] = y
        m[2, 2] = z
        return Matrix4D(m)
    else:
        raise TypeError()


def x_rot_matrix(rad):
    if isinstance(rad, (int, float)):
        m = np.identity(4)
        m[1, 1] = np.cos(rad)
        m[1, 2] = -np.sin(rad)
        m[2, 1] = np.sin(rad)
        m[2, 2] = np.cos(rad)
        return Matrix4D(m)
    else:
        raise TypeError()


def y_rot_matrix(rad):
    if isinstance(rad, (int, float)):
        m = np.identity(4)
        m[0, 0] = np.cos(rad)
        m[0, 2] = np.sin(rad)
        m[2, 0] = -np.sin(rad)
        m[2, 2] = np.cos(rad)
        return Matrix4D(m)
    else:
        raise TypeError()


def z_rot_matrix(rad):
    if isinstance(rad, (int, float)):
        m = np.identity(4)
        m[0, 0] = np.cos(rad)
        m[0, 1] = -np.sin(rad)
        m[1, 0] = np.sin(rad)
        m[1, 1] = np.cos(rad)
        return Matrix4D(m)
    else:
        raise TypeError()
