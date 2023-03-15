def strict(func):
    def wrapper(*args,**kwargs):
        _args :dict = dict(zip(func.__annotations__.keys(),args))
        for (name, field_type) in func.__annotations__.items():
            if name == 'return': continue
            if not isinstance(_args[name], field_type):
                current_type = type(_args[name])
                raise TypeError(f"The argument `{name}` was assigned with `{current_type}` instead of `{field_type}`")
        func_return_value = func(*args,**kwargs)
        if func.__annotations__.get('return') and not isinstance(func_return_value, func.__annotations__['return']):
            current_type = type(func_return_value)
            raise TypeError(f"The return should be `{field_type}` instead of `{current_type}`")
        return func_return_value
    return wrapper