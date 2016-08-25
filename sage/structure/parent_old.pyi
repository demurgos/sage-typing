# -*- coding: utf8 -*-
u"""
Python interface for the `sage.structure.parent_old` module.

Documentation:
http://doc.sagemath.org/html/en/reference/structure/sage/structure/parent_old.html

Source:
https://github.com/sagemath/sage/blob/master/src/sage/structure/parent_old.pxd
https://github.com/sagemath/sage/blob/master/src/sage/structure/parent_old.pyx
"""


from typing import Any

import sage.structure.parent

class Parent(sage.structure.parent.Parent):
    def coerce_map_from_c(self, S) -> Any: ...
    def get_action_c(self, S, op, self_on_left) -> Any: ...
    def get_action_impl(self, S, op, self_on_left) -> Any: ...
    def has_coerce_map_from_c(self, S) -> Any: ...
    def list(self) -> Any: ...
