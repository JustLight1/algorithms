"""
Complete the solution so that the function will break up camel casing, using a
space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    res = ''
    for i in s:
        if i.isupper():
            res += ' ' + i
        else:
            res += i
    return res
