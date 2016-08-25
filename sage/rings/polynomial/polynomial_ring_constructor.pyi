u"""
Python interface for the `sage.rings.polynomial.polynomial_ring_constructor` module.

http://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_ring_constructor.html
"""

from typing import Any, List, Union, Optional


import sage.structure.factory
import sage.rings.finite_rings.finite_field_base


def BooleanPolynomialRing_constructor(n=None, names=None, order='lex'): ...

def PolynomialRing(base_ring,
                   arg1=None,
                   arg2=None,
                   sparse=False,
                   order='degrevlex',
                   names=None,
                   name=None,
                   var_array=None,
                   implementation=None): ...

def polynomial_default_category(base_ring_category, multivariate): ...
