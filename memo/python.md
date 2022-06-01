# Python

## ipython

!ls
%run
%hist

```
i ** j
i // j
a, b = b, a
(1, 2, 3) > (1, 1, 3)

with open('./txt', 'wt') as f:
    print("...", sep=',', end='', file=f)

v1 if condition else v2

from collections import *
defaultdict(list)
defaultdict(set)
OrderdDict()

集合: & -

{k: d[k] + 1 for k in d.keys()}

(n for n in items if n > 0)
[n if n > 0 else 0 for n in items]

```

## 字符串处理

'ab' in 'abc'
2 * 'John'

## 解压可迭代对象赋值给多个变量

```
a,b,c,d,e = 'hello'
name, _, price, (year, mon, day), *time = [ 'ACME', 50, 91.1, (2012, 12, 21), '10:00', '11:00' ]
field1, field2 = line.split(',')

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
```

## pdb
n
p
s
