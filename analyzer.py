import operator
from functools import reduce

from token import Token
from type import Type
from utils import *


def apply_keyword_if(other, variables):
    # log('debug other', other)
    result = None
    condition, valid, invalid = other
    #
    check_pass = None
    if isinstance(condition, list):
        check_pass = parse_expression(condition, variables)
    else:
        check_pass = interpret_variable(condition, variables)
    #
    if check_pass:
        result = interpret_variable(valid, variables)
    else:
        result = interpret_variable(invalid, variables)
    return result


def apply_keyword_func(other, variables, funcs):
    func_name, *params = other[0]
    name = func_name.valueByType()
    content = other[1:]
    func_info = {
        "name": name,
        "params": [t.valueByType() for t in params],
        "content": content,
        "variables": {},
    }
    funcs[name] = func_info


def apply_keyword(keyword, other, variables, funcs):
    value = keyword.value
    result = None
    # log('debug other', other)
    if value == 'set':
        k = other[0].valueByType()
        v = other[1].valueByType()
        variables[k] = v
    elif keyword.value == 'log':
        log(*other)
    elif keyword.value == 'if':
        result = apply_keyword_if(other, variables)
    elif keyword.value == 'function':
        apply_keyword_func(other, variables, funcs)
    else:
        # error
        pass
    return result


def apply_boolean(value):
    bool_map = {
        'true': True,
        'false': False,
    }
    return bool_map[value]


def interpret_variable(oprand, variables={}, funcs={}):
    if isinstance(oprand, list):
        return parse_expression(oprand, variables, funcs)
    elif oprand.type == Type.number:
        return oprand.valueByType()
    elif oprand.type == Type.boolean:
        return oprand.valueByType()
    else:
        try:
            value = variables[oprand.value]
        except KeyError:
            raise NameError(f'variable {oprand.value} is not defined')
        return value


def apply_operator(op, other, variables):
    op_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '>': operator.gt,
        '<': operator.lt,
        '=': operator.eq,
        '!': operator.ne,
    }
    oprands = [interpret_variable(i, variables) for i in other]
    return reduce(op_map[op.value], oprands)


def apply_function(op, other, variables, funcs):
    name = op.value
    params = [interpret_variable(t) for t in other]
    func_info = funcs[name]
    func_info['variable'] = {k: v for k, v in zip(func_info['params'], params)}
    # TODO: 暂时先用 func_info['variable'], 只支持局部变量, 不支持外部变量
    # 后续需在 parse_expression 里添加变量处理, 先从局部作用域查询, 再取查询上层作用域
    value = analyze(func_info['content'], func_info['variable'], funcs)
    return value


def parse_expression(item, variables, funcs={}):
    op = item[0]
    oprands = item[1:]
    value = None
    if op.type == Type.keyword:
        value = apply_keyword(op, oprands, variables, funcs)
    elif op.type == Type.operator:
        value = apply_operator(op, oprands, variables)
    elif op.type == Type.variable:
        # FIXME: 其实是 func
        value = apply_function(op, oprands, variables, funcs)
    else:
        pass
    return value


def analyze(ast, variables={}, funcs={}):
    # log('debug ast', ast)
    result = None
    for item in ast:
        result = parse_expression(item, variables, funcs)
        # log('debug variables', variables)
    return result
