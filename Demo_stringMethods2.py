a = "1abc2abc3abc4abc"
print(a)
print(a.replace('abc', 'ABC'))
print(a.replace('abc', 'ABC', 1))
print(a.replace('abc', 'ABC', 2))

"""
There has to be a simpler way to replace the nth instance
"""
n = 3
b = a.replace('abc', 'ABC', n)
print(b.replace('ABC', 'abc', n-1))
"""

"""

print('**************************************')
"""
Substrings
"""
print(b[0:6])
print(b[0:6:2])
"""
Really simple encryption
"""
c = b[0:len(b):2]
d = b[1:len(b):2]
print(c)
print(d)
print(d + c)
"""
Reverse the string
"""
print(b[len(b):0:-1])