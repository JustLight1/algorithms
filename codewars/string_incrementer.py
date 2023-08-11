def increment_string(strng):
    res = ''
    for i in strng[-3:]:
        if (i.isdigit()):
            res += i
            b = int(res) + 1
    print(strng + str(b))


increment_string('foobar1')
