"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
"""


def generate_hashtag(s):
    if len(s) == 0 or len(s) >= 140:
        return False

    words = s.lower().split()
    f = ''
    for i in words:
        f += i[0].upper() + i[1:]
    return '#' + ''.join(f)


generate_hashtag(" Hello there thanks for trying my Kata")


"""
Метод capitalize() вернет копию строки str с первым символом в верхнем
регистре, а остальные символы будут в нижнем регистре.
def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output
"""

"""
Метод title() возвращает строку с заглавной первой буквой каждого слова
в верхний регистр.
def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False
"""
