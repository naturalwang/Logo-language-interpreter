# Logo-language-interpreter

An interpreter of custom logo language base on python.

### Basic Usage

#### Types Example
```
int: 123
boolean: true, false
null: null
string: "hello"
operators:
- +
- -
- *
- \
- %
- = equal
- ! not equal
- > greater than
- < less than
- ; comment
```

#### keywords:
- set
- function
- log
- if

#### Syntax Example
variable assignment
```
[set a 1]
[set b 2]
[+ a b]
```

calculate expression with comment
```
[+ 1 2]       ; value is 3

[+ 1 [- 2 3]] ; value is 0

[* 2 3 4]     ; value is 24
```

condition expression
```
[if true
    [log "success"]
    [log "failed"]
]
```

function define and call
```
[function [addOrSub a b]
    [if [> a b]
        [- a b]
        [+ a b]
    ]
]
[addOrSub 1 3]    ; value is 4
```

#### Usage
``` python
from parser import apply as apply_code


def main():
    code = """
        [function [addOrSub a b]
            [if [> a b]
                [- a b]
                [+ a b]
            ]
        ]
        [addOrSub 1 3]
    """
    value = apply_code(code)
    print('result is', value)

if __name__ == '__main__':
    main()


```
