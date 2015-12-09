__author__ = 'uv2sun'


def test(a, *args, **dic):
    print a, args, dic.get('x', '3232')


test(1, 2, 3, x=2)
test(1, 2)
