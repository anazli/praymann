# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np

from raymann.math_tools.vector3d import Vector3D


class Spectrum:
    def __init__(self, val: Vector3D = None):
        if val is None:
            self._color = Vector3D()
        elif isinstance(val, Vector3D):
            self._color = val
        else:
            raise TypeError("Spectrum takes only Vector3D as init parameter")

    @property
    def samples(self) -> Vector3D:
        return self._color

    @samples.setter
    def samples(self, val: Vector3D):
        if isinstance(val, Vector3D):
            self._color = val
        else:
            raise TypeError("must be Vector3D")

    def isblack(self) -> bool:
        return self._color == Vector3D()

    def hasnans(self) -> bool:
        return np.isnan(self._color.coordinates)

    def clip(self, a: int | float, b: int | float):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            np.clip(self._color, a, b)
        else:
            raise TypeError("a and b must be int or float")

    def __eq__(self, other: "Spectrum") -> bool:
        if isinstance(other, Spectrum):
            return self._color == other._color
        else:
            raise TypeError("cannot compare Spectrum with other type")

    def __ne__(self, other: "Spectrum") -> bool:
        if isinstance(other, Spectrum):
            return self._color != other._color
        else:
            raise TypeError("cannot compare Spectrum with other type")

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other: "Spectrum") -> "Spectrum":
        if isinstance(other, Spectrum):
            return Spectrum(self._color + other._color)
        elif isinstance(other, (int, float)):
            return Spectrum(self._color + other)
        else:
            raise TypeError("cannot do addition between Spectrum and another type")

    def __sub__(self, other):
        return self._add(other)

    def __rsub__(self, other):
        return self._add(other)

    def _sub(self, other: "Spectrum") -> "Spectrum":
        if isinstance(other, Spectrum):
            return Spectrum(self._color - other._color)
        elif isinstance(other, (int, float)):
            return Spectrum(self._color - other)
        else:
            raise TypeError("cannot do subtraction between Spectrum and another type")

    def __mul__(self, other):
        return self._add(other)

    def __rmul__(self, other):
        return self._add(other)

    def _mul(self, other: "Spectrum") -> "Spectrum":
        if isinstance(other, Spectrum):
            return Spectrum(self._color * other._color)
        elif isinstance(other, (int, float)):
            return Spectrum(self._color * other)
        else:
            raise TypeError(
                "cannot do multiplication between Spectrum and another type"
            )

    def __neg__(self) -> "Spectrum":
        return Spectrum(-self._color)

    def __str__(self) -> str:
        return f"Spectrum: {self._color}"
