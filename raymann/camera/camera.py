from raymann.math_tools.ray import Ray
import numpy as np
from raymann.math_tools.matrix4d import Matrix4D
from raymann.math_tools.vector4d import Vector4D
from raymann.math_tools.point3d import Point3D


class Camera:
    def __init__(
        self, hsize: int | float, vsize: int | float, fov: float, trans_mat: Matrix4D
    ):
        if (
            not isinstance(hsize, int | float)
            or not isinstance(vsize, int | float)
            or not isinstance(fov, float)
            or not isinstance(trans_mat, Matrix4D)
        ):
            raise TypeError("invalid argument for camera was given")
        if hsize <= 0 or vsize <= 0 or fov <= 0:
            raise ValueError(
                "invalid value for horizontal, vertical or field of view given"
            )
        self._fov = fov
        half_view = np.tan(self._fov / 2.0)
        aspect = hsize / vsize
        self._trans_matrix = trans_mat
        self._inv_trans_matrix = self._trans_matrix.inverse
        if aspect >= 1.0:
            self._half_height = half_view / aspect
            self._half_width = half_view
        else:
            self._half_width = half_view * aspect
            self._half_height = half_view
        self._pixel_size = 2.0 * self._half_width / hsize

    @property
    def pixel_size(self) -> float:
        return self._pixel_size

    def get_ray(self, pixel_x: int | float, pixel_y: int | float) -> Ray:
        xoffset = (pixel_x + 0.5) * self._pixel_size
        yoffset = (pixel_y + 0.5) * self._pixel_size
        world_x = self._half_width - xoffset
        world_y = self._half_height - yoffset
        pixel = self._inv_trans_matrix * Point3D(world_x, world_y, -1)
        o = self._inv_trans_matrix * Point3D()
        d = (pixel - o).normalized()
        return Ray(origin=o, direction=d)
