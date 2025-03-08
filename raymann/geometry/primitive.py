# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.

from abc import ABC, abstractmethod

from raymann.acceleration.bounding_box import BoundingBox
from raymann.common.intersection import Intersection
from raymann.math_tools.vector3d import Vector3D
from raymann.transformation.transformer import Transformer
from raymann.math_tools.ray import Ray


class Primitive(ABC):
    def __init__(self, transformation: Transformer):
        if isinstance(transformation, Transformer):
            self._transformation = transformation
        else:
            raise TypeError("expects a Transformer object")

    @abstractmethod
    def intersect(self, ray: Ray, record: Intersection) -> bool:
        """Tests if there's an intersection between ray and primitive"""
        if not isinstance(ray, Ray) or not isinstance(record, Intersection):
            raise TypeError("invalid parameters, should be (Ray, Intersection)")

    @abstractmethod
    def pdf(self, record:Intersection, wi: Vector3D) -> float:
        """pdf"""
        if not isinstance(record, Intersection) or not isinstance(wi, Vector3D):
            raise TypeError("invalid parameters, should be (Intersection, Vector3D)")

    @abstractmethod
    def bounding_box(self) -> BoundingBox:
        """Bounding box of the privimite in object space"""

    @abstractmethod
    def surface_area(self):
        """the area of the geometric primitive"""