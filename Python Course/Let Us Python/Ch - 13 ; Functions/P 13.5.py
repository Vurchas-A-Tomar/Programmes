def is_parlindrom(sentence):
    split = [s.lower() for s in sentence.split(' ')]
    sent_ = ''.join(split)

    if sent_[:] == sent_[::-1]:
        s = True
    else:
        s = False
    
    return s

print(is_parlindrom('Malayalam'))