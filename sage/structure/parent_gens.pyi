# -*- coding: utf8 -*-
u"""
Python interface for the `sage.structure.parent_gens` module.

Documentation:
http://doc.sagemath.org/html/en/reference/structure/sage/structure/parent_gens.html

Source:
https://github.com/sagemath/sage/blob/master/src/sage/structure/parent_gens.pxd
https://github.com/sagemath/sage/blob/master/src/sage/structure/parent_gens.pyx
"""


from typing import Any, Tuple

import sage.structure.parent_base

class ParentWithGens(sage.structure.parent_base.ParentWithBase):
     def gen(self, i=0) -> Any: ...
     def gens(self) -> Tuple: ...
     def hom(self, im_gens, codomain=None, check=True) -> Any: ...
     def ngens(self) -> Any: ...


class ParentWithAdditiveAbelianGens(ParentWithGens):
    def generator_orders(self) -> Any: ...


class ParentWithMultiplicativeAbelianGens(ParentWithGens):
    def generator_orders(self) -> Any: ...


def is_ParentWithAdditiveAbelianGens(x) -> bool: ...
def is_ParentWithGens(x) -> bool: ...
def is_ParentWithMultiplicativeAbelianGens(x) -> bool: ...


class localvars(object):
    def __init__(self, X, names, latex_names: Any = ..., normalize=False) -> None: ...
