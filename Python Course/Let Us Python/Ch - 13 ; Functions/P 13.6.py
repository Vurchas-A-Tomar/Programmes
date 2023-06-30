def convert(sentence):
    split = [s for s in sentence.split(' ')]
    return ' '.join(sorted(set(split)))

print(convert('Hi HI Hi'))