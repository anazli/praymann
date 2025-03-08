# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.

from abc import ABC, abstractmethod

import numpy as np

from raymann.acceleration.bounding_box import BoundingBox
from raymann.common.intersection import Intersection
from raymann.math_tools.vector3d import Vector3D
from raymann.transformation.transformer import Transformer
from raymann.math_tools.ray import Ray


def get_min_hit_param(tmin: float, tmax: float, *args) -> float:
    thit = np.inf
    for t in args:
        if tmin <= t < tmax and t < thit:
            thit = t

    return thit


class Primitive(ABC):
    def __init__(self, transformation: Transformer):
        if isinstance(transformation, Transformer):
            self._transformation = transformation
        else:
            raise TypeError("expects a Transformer object")
        self._bbox = BoundingBox()

    @abstractmethod
    def intersect(self, ray: Ray, record: Intersection) -> bool:
        """Tests if there's an intersection between ray and primitive"""
        if not isinstance(ray, Ray) or not isinstance(record, Intersection):
            raise TypeError("invalid parameters, should be (Ray, Intersection)")
        return False

    @abstractmethod
    def pdf(self, record: Intersection, wi: Vector3D) -> float:
        """probability density of sampling a point on the primitive"""
        if not isinstance(record, Intersection) or not isinstance(wi, Vector3D):
            raise TypeError("invalid parameters, should be (Intersection, Vector3D)")
        return False

    @abstractmethod
    def surface_area(self) -> float:
        """the area of the geometric primitive"""

    def bounding_box(self) -> BoundingBox:
        """Bounding box of the privimite in object space"""
        return self._bbox
