def ispangram(sentence):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    print(alphaset)
    return alphaset <= set(sentence.lower())

print(ispangram('abcdefghijklmnopqrstuvwxyzz'))