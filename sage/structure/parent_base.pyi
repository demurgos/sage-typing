u"""
Python interface for the `sage.structure.parent_base` module.

http://doc.sagemath.org/html/en/reference/structure/sage/structure/parent_base.html
"""

from typing import Any

import sage.structure.parent_old

class ParentWithBase(sage.structure.parent_old.Parent):
    def base_extend(self, X) -> Any: ...

def is_ParentWithBase(x) -> Any: ...
