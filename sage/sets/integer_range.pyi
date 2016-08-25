u"""
Python interface for the `sage.sets.integer_range` module

http://doc.sagemath.org/html/en/reference/structure/sage/sets/integer_range.html
"""

from typing import Any

from sage.rings.integer import Integer
import sage.structure.parent
import sage.structure.unique_representation


class IntegerRange(sage.structure.unique_representation.UniqueRepresentation,
                   sage.structure.parent.Parent):

    def __init__(self, begin, end, step: int = 1, middle_point: int = None) -> None: ...
    element_class = ... # type: Integer

class IntegerRangeFinite(IntegerRange):
    def cardinality(self) -> Integer: ...
    def rank(self, x: int) -> Any: ...
    def unrank(self, i: int) -> Integer: ...
