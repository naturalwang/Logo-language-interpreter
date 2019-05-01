from token import Token
from type import Type
from tokenizer import tokenize
from analyzer import analyze
from ast import parsed_ast_by_stack
from utils import *


def apply(code):
    tokens = tokenize(code)
    # log('debug tokens', tokens)
    ast = parsed_ast_by_stack(tokens)
    value = analyze(ast, {})
    return value
