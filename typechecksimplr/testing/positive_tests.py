from typechecksimplr.testing.additional_utils import Fn
from typechecksimplr.testing.testing_utils import AssertionUtil
from typechecksimplr.testing import scope

def test_positive_o_numeric_types():
    
    print(f"Running {Fn().name} ...")
    assert AssertionUtil.not_raises(Exception, scope.integer_function, 2), "Integer Expected"
    assert AssertionUtil.not_raises(Exception, scope.float_function, 2.2), "Float Expected"
    assert AssertionUtil.not_raises(Exception, scope.complex_function, complex(5,10)), "Complex Expected"
def test_positive_o_sequence_types():

    print(f"Running {Fn().name} ...")
    message :str = "FAIL : Test {0} : {1}"
    assert AssertionUtil.not_raises(Exception, scope.list_function, [2,"yes",False]), message.format(1,"list Expected")
    assert AssertionUtil.not_raises(Exception, scope.tuple_function, (2.2,"yes")), message.format(2,"float Expected")
    assert AssertionUtil.not_raises(Exception, scope.range_function, range(500,1000)), message.format(3,"range Expected")

def test_positive_o_text_sequence_types():

    print(f"Running {Fn().name} ...")
    message :str = "FAIL : Test {0} : {1}"
    assert AssertionUtil.not_raises(Exception, scope.str_function, "1"), message.format(1,"str Expected")

def test_positive_o_binary_sequence_types():

    print(f"Running {Fn().name} ...")
    message :str = "FAIL : Test {0} : {1}"
    f = lambda *args: message.format(*args)
    assert AssertionUtil.not_raises(Exception, scope.bytes_function, bytes("yes", 'utf-8')), f(1,"byte expected")
    assert AssertionUtil.not_raises(Exception, scope.bytes_function, bytes("no", 'ascii')), f(2,"byte expected")
    assert AssertionUtil.not_raises(Exception, scope.bytearray_function, bytearray("no", 'ascii')), f(3,"bytearray expected")
    assert AssertionUtil.not_raises(Exception, scope.memoryview_function, memoryview(bytearray('ABCDE', 'utf-8'))), f(3,"memoryview expected")

def test_positive_o_set_types():

    print(f"Running {Fn().name} ...")
    message :str = "FAIL : Test {0} : {1}"
    f = lambda *args: message.format(*args)
    assert AssertionUtil.not_raises(Exception, scope.set_function, {1,2,3,3,8}), f(1,"set Expected")
    assert AssertionUtil.not_raises(Exception, scope.frozenset_function, frozenset({1,2,3,3,8})), f(2,"frozenset Expected")

def test_positive_o_mapping_types():

    print(f"Running {Fn().name} ...")
    f = AssertionUtil.AssertCounter().formatter(type=2).f
    assert AssertionUtil.not_raises(Exception, scope.dict_function, {}), f("dict Expected")
    assert AssertionUtil.not_raises(Exception, scope.dict_function, {1:2}), f("dict Expected")
    assert AssertionUtil.not_raises(Exception, scope.dict_function, {1:{}}), f("dict Expected")
