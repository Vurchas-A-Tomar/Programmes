def ispangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s.lower())

print(ispangram('the quick brown fox jumps over the lazy dog'))
