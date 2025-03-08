# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
from raymann.math_tools.matrix4d import Matrix4D
from raymann.math_tools.ray import Ray


class Transformer:
    def __init__(self, mat: Matrix4D = Matrix4D()):
        if isinstance(mat, Matrix4D):
            self._matrix = mat
            self._inverse = self._matrix.inverse
            self._inverse_transpose = self._inverse.transpose
        else:
            raise TypeError()

    @property
    def matrix(self) -> Matrix4D:
        return self._matrix

    @property
    def inverse_matrix(self) -> Matrix4D:
        return self._inverse

    @property
    def inverse_transpose_matrix(self) -> Matrix4D:
        return self._inverse_transpose

    def world_to_obj_space(self, entity: Ray) -> Ray:  # to be edited
        if isinstance(entity, Ray):
            obj_space_origin = self._inverse * entity.origin
            obj_space_direction = self._inverse * entity.direction
            return Ray(origin=obj_space_origin, direction=obj_space_direction)
        else:
            raise TypeError("unknown type for world to object space transformation")

    def obj_to_world_space(self, entity: Ray) -> Ray:
        if isinstance(entity, Ray):
            wrld_space_origin = self._matrix * entity.origin
            wrld_space_direction = self._matrix * entity.direction
            return Ray(origin=wrld_space_origin, direction=wrld_space_direction)
        else:
            raise TypeError("unknown type for object to world space transformation")
