# -*- coding: utf8 -*-
u"""
Python interface for the `sage.rings.infinity` module.

Documentation:
http://doc.sagemath.org/html/en/reference/rings/sage/rings/infinity.html

Source:
https://github.com/sagemath/sage/blob/master/src/sage/rings/infinity.py
"""


from typing import Any

import sage.structure.element
import sage.rings.ring


class AnInfinity(object):
    def lcm(self, x) -> Any: ...


class FiniteNumber(sage.structure.element.RingElement):
    def __init__(self, parent, x) -> None: ...
    def sqrt(self) -> Any: ...


# Real parent classes: sage.rings.infinity._uniq, sage.rings.ring.Ring
class InfinityRing_class(sage.rings.ring.Ring):
    def fraction_field(self) -> Any: ...
    def gen(self, n=0) -> Any: ...
    def gens(self) -> Any: ...
    def is_commutative(self) -> Any: ...
    def is_zero(self) -> Any: ...
    def ngens(self) -> Any: ...


# Real parent classes: sage.rings.infinity._uniq, sage.structure.element.RingElement
class LessThanInfinity(sage.structure.element.RingElement):
    def __init__(self, parent=...) -> None: ...


# Real parent classes: sage.rings.infinity._uniq,
#                      sage.rings.infinity.AnInfinity,
#                      sage.structure.element.InfinityElement
class MinusInfinity(AnInfinity, sage.structure.element.InfinityElement):
    def sqrt(self) -> Any: ...


# Real parent classes: sage.rings.infinity._uniq,
#                      sage.rings.infinity.AnInfinity,
#                      sage.structure.element.InfinityElement
class PlusInfinity(AnInfinity, sage.structure.element.InfinityElement):
    def sqrt(self) -> Any: ...


class SignError(ArithmeticError):
    pass



# Real parent classes: sage.rings.infinity._uniq,
#                      sage.rings.infinity.AnInfinity,
#                      sage.structure.element.InfinityElement
class UnsignedInfinity(AnInfinity, sage.structure.element.InfinityElement):
    pass



# Real parent classes: sage.rings.infinity._uniq, sage.rings.ring.Ring
class UnsignedInfinityRing_class(sage.rings.ring.Ring):
    def fraction_field(self) -> Any: ...
    def gen(self, n=0) -> Any: ...
    def gens(self) -> Any: ...
    def less_than_infinity(self) -> Any: ...
    def ngens(self) -> Any: ...


def is_Infinite(x) -> bool: ...
def test_comparison(ring) -> Any: ...
def test_signed_infinity(pos_inf) -> Any: ...
