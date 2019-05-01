from type import Type
from utils import *


def pop_list(stack):
    l = []
    while len(stack) > 0:
        if isinstance(stack[-1], list):
            l.append(stack.pop(-1))
        elif stack[-1].type != Type.bracketLeft:
            l.append(stack.pop(-1))
        else:
            break
    stack.pop(-1)
    l.reverse()
    return l


def parsed_ast_by_stack(tokens):
    """
    用栈解析 ast
    """
    l = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        i += 1
        if token.type == Type.bracketRight:
            list_token = pop_list(l)
            l.append(list_token)
        else:
            l.append(token)
    return l
