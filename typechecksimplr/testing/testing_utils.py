from collections import namedtuple
import dataclasses
from typing import NewType

from typechecksimplr.schema import TypeCheck


none = NewType('none',type(None))
class AssertionUtil:

    @staticmethod
    def raises(exception_cls,fn,*args,**kwargs):
        exception = False
        try:
            fn(*args,**kwargs)
        except exception_cls:
            exception = True
        except Exception: pass
        return exception
    @staticmethod
    def not_raises(exception_cls,fn,*args,**kwargs):
        exception = True
        try:
            fn(*args,**kwargs)
        except exception_cls:
            exception = False
        except Exception: pass
        return exception

    class AssertCounter:

        def __init__(self) -> None:
            # TODO : add support for user to add custom format string .
            self._count :int = 0
            self._available_format_templates :dict = {
                1: "FAIL : Test {0} : {1}",
                2: "\n#{0} .\nFAILED.\nReason : {1}\n",
            }
        def formatter(self,type :int = 1) -> str:
            """Message Formatter Type 1"""
            message :str = self._available_format_templates[type]
            result = namedtuple('result','f')
            def format(*args):
                self._count += 1
                return message.format(*(self._count,*args))
            return result(f=format)

