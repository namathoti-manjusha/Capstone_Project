"""def demo():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'E'
x=demo()
print(next(x))"""

'''num=[x*x for x in range(10)]
print(num)'''

'''n=[i for i in range(100)]
print(n)'''

num=(x*x for x in range(10))
print(num)
print(next(num))