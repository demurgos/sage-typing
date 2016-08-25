u"""
Python interface for the `sage.rings.finite_rings.finite_field_constructor` module.

http://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_constructor.html
"""

from typing import Any, List, Union, Optional


import sage.structure.factory
import sage.rings.finite_rings.finite_field_base


class FiniteFieldFactory(sage.structure.factory.UniqueFactory):
    def __call__(self,
                 order,
                 name: Optional[basestring] = None,  # Name of symbol used for polynomial representation of elements
                 modulus=None,
                 names=None,
                 impl=None,
                 proof=None,
                 check_irreducible=True,
                 **kwds
                 ) -> sage.rings.finite_rings.finite_field_base.FiniteField: ...


GF = FiniteField = FiniteFieldFactory()

def is_PrimeFiniteField(x) -> bool: ...

zech_log_bound = ... # type: int
