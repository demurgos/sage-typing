u"""
Python interface for the `sage.rings.finite_rings.finite_field_base` module.

http://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_base.html
"""

from typing import Any

import sage.rings.ring


class FiniteField(sage.rings.ring.Field):
    def algebraic_closure(self, name='z', **kwds) -> Any: ...
    def cardinality(self) -> Any: ...
    def construction(self) -> Any: ...
    def dual_basis(self, basis=None, check=True) -> Any: ...
    def extension(self, modulus, name=None, names=None, map=False, embedding=None, **kwds) -> Any: ...
    def factored_order(self) -> Any: ...
    def factored_unit_order(self) -> Any: ...
    def frobenius_endomorphism(self, n=1) -> Any: ...
    def gen(self) -> Any: ...
    def is_conway(self) -> Any: ...
    def is_field(self, proof=True) -> Any: ...
    def is_finite(self) -> Any: ...
    def is_perfect(self) -> Any: ...
    def is_prime_field(self) -> Any: ...
    def modulus(self) -> Any: ...
    def multiplicative_generator(self) -> Any: ...
    def ngens(self) -> Any: ...
    def order(self) -> Any: ...
    def polynomial(self, name=None) -> Any: ...
    def polynomial_ring(self, variable_name=None) -> Any: ...
    def primitive_element(self) -> Any: ...
    def random_element(self, *args, **kwds) -> Any: ...
    def some_elements(self) -> Any: ...
    def subfields(self, degree=0, name=None) -> Any: ...
    def unit_group_exponent(self) -> Any: ...
    def vector_space(self) -> Any: ...
    def zeta(self, n=None) -> Any: ...
    def zeta_order(self) -> Any: ...

class FiniteFieldIterator(object):
    def next(self) -> Any: ...

def is_FiniteField(x) -> bool: ...
