"""
Your task is to sort a given string. Each word in the string will contain a 
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input 
String will only contain valid consecutive numbers.
"""


def order(sentence):
    a = sentence.split()
    res = [None] * len(a)
    for i in a:
        for c in i:
            if c.isdigit():
                position = int(c) - 1
                res[position] = i
    return ' '.join(res)


result = order('is2 Thi1s T4est 3a')
print(result)

"""
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
"""
