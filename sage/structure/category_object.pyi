u"""
Python interface for the `sage.structure.category_object` module.

http://doc.sagemath.org/html/en/reference/structure/sage/structure/category_object.html
"""

from typing import Any

import sage.structure.sage_object

class CategoryObject(sage.structure.sage_object.SageObject):
    def Hom(self, codomain, cat=None) -> Any: ...
    def base(self) -> Any: ...
    def base_ring(self) -> Any: ...
    def categories(self) -> Any: ...
    def category(self) -> Any: ...
    def gens_dict(self) -> Any: ...
    def gens_dict_recursive(self) -> Any: ...
    def has_base(self, category=None) -> Any: ...
    def inject_variables(self, scope=None, verbose=True) -> Any: ...
    def injvar(self, scope=None, verbose=True) -> Any: ...
    def latex_name(self) -> Any: ...
    def latex_variable_names(self) -> Any: ...
    def normalize_names(self, ngens, names) -> Any: ...
    def objgen(self) -> Any: ...
    def objgens(self) -> Any: ...
    def variable_name(self) -> Any: ...
    def variable_names(self) -> Any: ...

def certify_names(names) -> Any: ...
def check_default_category(default_category, category) -> Any: ...
def guess_category(obj) -> Any: ...
def localvars(obj, names, latex_names=None, normalize=True) -> Any: ...
def normalize_names(ngens, names) -> Any: ...