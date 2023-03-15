from collections import namedtuple
import dataclasses
from typechecksimplr.schema import TypeCheck
from typechecksimplr.strict import strict
from typechecksimplr.testing.additional_utils import none

@dataclasses.dataclass
class TestConfigSchema(TypeCheck):
    title: str

def setup(**config)->none:
    TestConfigSchema(**config)
    print(f"SETUP : {config['title']} ")
    @strict
    def f1(a:int):...
    @strict
    def f2(a:float):...
    @strict
    def f3(a:complex):...
    @strict
    def f4(a:list):...
    @strict
    def f5(a:tuple):...
    @strict
    def f6(a:range):...
    @strict
    def f7(a:str):...
    @strict
    def f8(a:bytes):...
    @strict
    def f9(a:bytearray):...
    @strict
    def f10(a:memoryview):...
    @strict
    def f11(a:set):...
    @strict
    def f12(a:frozenset):...
    @strict
    def f13(a:dict):...
    
    keys :tuple = (
        'integer_function','float_function','complex_function',
        'list_function','tuple_function','range_function',
        "str_function",
        "bytes_function", "bytearray_function", "memoryview_function",
        "set_function", "frozenset_function",
        "dict_function"
    )
    setup = namedtuple('setup',keys)
    return setup(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13)
