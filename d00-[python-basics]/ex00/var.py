def my_var():
    i = 42
    s = "42"
    ss = 'quarante-deux'
    f = 42.0
    b = True
    l = [42]
    d = {42:42}
    t = (42,)
    sss = set()
    print(i, "has a type", type(i))
    print(s, "has a type", type(s))
    print(ss, "has a type", type(ss))
    print(f, "has a type", type(f))
    print(b, "has a type", type(b))
    print(l, "has a type", type(l))
    print(d, "has a type", type(d))
    print(t, "has a type", type(t))
    print(sss, "has a type", type(sss))

if __name__ == '__main__':
    my_var()