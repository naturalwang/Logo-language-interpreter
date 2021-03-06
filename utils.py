def log(*args, **kwargs):
    print(args, kwargs)


def ensure(condition, msg):
    if not condition:
        log('测试失败', msg)
    else:
        log('测试成功', msg)


def is_space(char):
    return char == ' '


def is_numeric(c):
    return c in '1234567890-+.'


def str_to_num(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)


def dict_equal(d1, d2):
    if len(d1.keys()) != len(d2.keys()):
        return False
    diffkeys = [k for k in d1 if d1[k] != d2[k]]
    return len(diffkeys) == 0


def is_empty(array):
    return len(array) == 0
