import types

def is_method(object):
    return isinstance(object, types.MethodType)

def is_function(object):
    return isinstance(object, types.FunctionType)

def is_code(object):
    return isinstance(object, types.CodeType)

def get_argspec(func):
    if is_method(func):
        func = func.__func__
    if not is_function(func):
        raise TypeError(f'arg is not a Python function // {func}')
    args, varargs, varkw = getargs(func.__code__)
    return args, varargs, varkw, func.__defaults__

