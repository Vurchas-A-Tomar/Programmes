s = set()

a, b, c, d, e = input('Enter different 5 names : ').split(' ')
s.update(a)
s.update(b)
s.update(c)
s.update(d)
s.update(e)

s.pop()

s.discard(a)
s.discard(b)
print(s)