from typing import List

from syntax.generics.ie_enumerable import IEnumerable


class Binder:

    def __init__(self, syntax):
        self.__syntax = syntax
        self.__diagnostics: List[str] = []

    @property
    def diagnostics(self):
        return IEnumerable(self.__diagnostics)

    def bind_unary_expression(self, syntax): ...

    def bind_binary_expression(self, syntax): ...

    def bind_literal_expression(self, syntax): ...
