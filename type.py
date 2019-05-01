from enum import Enum


class Type(Enum):
    auto = 1            # auto 用来处理单字符符号, 方便使用
    semicolon = 2       # ;
    bracketLeft = 3     # [
    bracketRight = 4    # ]
    number = 5          # 88
    string = 6          # "name"
    boolean = 7         # true / true
    null = 8            # nil
    keyword = 9         # if set
    operator = 10       # + - * / % = ! > <
    variable = 11       # 变量
    function = 12       # 函数
