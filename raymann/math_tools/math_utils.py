# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np

from raymann.math_tools.matrix4d import Matrix4D
from raymann.math_tools.vector3d import Vector3D
from raymann.math_tools.vector2d import Vector2D
from raymann.math_tools.vector4d import Vector4D
from raymann.math_tools.point3d import Point3D


def dot(elem1: Vector2D | Vector3D | Vector4D, elem2: Vector2D | Vector3D | Vector4D):
    """dot product of two math entities"""
    if (
        (isinstance(elem1, Vector2D) and isinstance(elem2, Vector2D))
        or (isinstance(elem1, Vector3D) and isinstance(elem2, Vector3D))
        or (isinstance(elem1, Vector4D) and isinstance(elem2, Vector4D))
    ):
        return np.dot(elem1.coordinates, elem2.coordinates)
    else:
        raise TypeError("Cannot calculate the dot product of the given elements!")


def cross(elem1: Vector2D | Vector3D | Vector4D, elem2: Vector2D | Vector3D | Vector4D):
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


def identity_matrix() -> Matrix4D:
    return Matrix4D(np.identity(4))


def zero_matrix() -> Matrix4D:
    return Matrix4D(np.zeros((4, 4)))


def translation_matrix(x: int | float, y: int | float, z: int | float) -> Matrix4D:
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
        raise TypeError("unknown input type for translation matrix")


def scale_matrix(x: int | float, y: int | float, z: int | float) -> Matrix4D:
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
        raise TypeError("unknown input type for scale matrix")


def x_rot_matrix(rad: int | float) -> Matrix4D:
    if isinstance(rad, (int, float)):
        m = np.identity(4)
        m[1, 1] = np.cos(rad)
        m[1, 2] = -np.sin(rad)
        m[2, 1] = np.sin(rad)
        m[2, 2] = np.cos(rad)
        return Matrix4D(m)
    else:
        raise TypeError("unknown input type for rotation matrix")


def y_rot_matrix(rad: int | float) -> Matrix4D:
    if isinstance(rad, (int, float)):
        m = np.identity(4)
        m[0, 0] = np.cos(rad)
        m[0, 2] = np.sin(rad)
        m[2, 0] = -np.sin(rad)
        m[2, 2] = np.cos(rad)
        return Matrix4D(m)
    else:
        raise TypeError("unknown input type for rotation matrix")


def z_rot_matrix(rad: int | float) -> Matrix4D:
    if isinstance(rad, (int, float)):
        m = np.identity(4)
        m[0, 0] = np.cos(rad)
        m[0, 1] = -np.sin(rad)
        m[1, 0] = np.sin(rad)
        m[1, 1] = np.cos(rad)
        return Matrix4D(m)
    else:
        raise TypeError("unknown input type for rotation matrix")


def view_transform(self, from_v: Vector3D, to_v: Vector3D, up_v: Vector3D) -> Matrix4D:
    if (
        not isinstance(from_v, Vector3D)
        or not isinstance(to_v, Vector3D)
        or not isinstance(up_v, Vector3D)
    ):
        raise TypeError("invalid parameter for view transform matrix")
    forward = (to_v - from_v).normalized()
    up_norm = up_v.normalized()
    left = cross(forward, up_norm)
    up_res = cross(left, forward)

    m = np.array(
        [
            [left.x, left.y, left.z, 0.0],
            [up_res.x, up_res.y, up_res.z, 0.0],
            [-forward.x, -forward.y, -forward.z, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
    )

    return Matrix4D(m) * translation_matrix(-from_v.x, -from_v.y, -from_v.z)
