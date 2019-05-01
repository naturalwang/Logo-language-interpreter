from utils import *
from parser import apply


def test_apply_1():
    code1 = "[+ 1 2]         ; 表达式的值是 3"
    # log('code1', tokenizer(code1))
    ensure(apply(code1) == 3, 'test apply 1')


def test_apply_2():
    code2 = "[* 2 3 4]       ; 表达式的值是 24"
    # log('code2', tokenizer(code2))
    ensure(apply(code2) == 24, 'test apply 2')


def test_apply_3():
    code3 = '[log "hello"]   ; 输出 hello, 表达式的值是 null(关键字 表示空)'
    # log('code3', tokenizer(code3))
    ensure(apply(code3) is None, 'test apply 3')


def test_apply_4():
    code4 = '[+ 1 [- 2 3]]   ; 表达式的值是 0, 相当于普通语法的 1 + (2 - 3)'
    # log('code4', tokenizer(code4))
    ensure(apply(code4) == 0, 'test apply 4')


def test_apply_5():
    code5 = '[if [> 2 1] 3 4]; 表达式的值是 3'
    # log('code5', tokenizer(code5))
    ensure(apply(code5) == 3, 'test apply 5')


def test_apply_6():
    code6 = """
        [if true
            [log "成功"]
            [log "没成功"]
        ]
    """
    # log('code6', tokenizer(code6))
    ensure(apply(code6) is None, 'test apply 6')


def test_apply_7():
    code7 = """
        [function [add a b]
            [if [> a b]
                [- a b]
                [+ a b]
            ]
        ]
        [add 1 3]
    """
    ensure(apply(code7) == 4, 'test apply 7')


def test_apply_8():
    code8 = '''
        [set a 1]
        [set b 2]
        [+ a b]
        '''
    ensure(apply(code8) == 3, 'test apply 8')


def test_apply_9():
    code = '''
        [set a 1]
        [set b 2]
        [+ a c]
        '''
    ensure(apply(code) == 3, 'test apply 8')


def test_apply():
    test_apply_1()
    test_apply_2()
    test_apply_3()
    test_apply_4()
    test_apply_5()
    test_apply_6()
    test_apply_7()
    test_apply_8()
    # test NameError
    # test_apply_9()


if __name__ == '__main__':
    test_apply()
