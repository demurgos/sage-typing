u"""
Python interface for the `sage.rings.polynomial.polynomial_singular_interface` module.

http://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_singular_interface.html
"""

from typing import Any, List, Union, Optional


import sage.structure.factory
import sage.rings.finite_rings.finite_field_base


class PolynomialRing_singular_repr(object):
    pass


class Polynomial_singular_repr(object):
    pass

def can_convert_to_singular(R) -> bool: ...
