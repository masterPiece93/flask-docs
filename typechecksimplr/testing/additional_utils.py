import sys
from typing import NewType

none = NewType('none',type(None))
fn_name = lambda : sys._getframe(1).f_code.co_name
class Fn:
    name = property(fget=lambda self: sys._getframe(1).f_code.co_name)
