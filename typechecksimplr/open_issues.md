1. It requires all the arguments of a function to have type-hints .
    HINT : use inspect.getargspec(func)
2. since only built-in type-hints are supported , there is no message for if user specifies a custom made type-hint.
    e.g below will fail :-
    ```python
    from typing import NewType
    salary = NewType('Salary',float)
    
    @strict
    def f(a:salary):...
    
    @strict
    def f(v:(int,float)):...
    ```
3. performance optimization is possible !. zip() function in source code can be replaced
