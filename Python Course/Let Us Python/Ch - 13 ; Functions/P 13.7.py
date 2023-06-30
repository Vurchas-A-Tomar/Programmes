def count_alphabets_digits(sentence):
    d = {
        'Alphabet' : 0,
        'Numbers' : 0
    }
    for x in sentence:
        if x.isalpha():
            d['Alphabet'] += 1
        elif x.isdigit():
            d['Numbers'] += 1
        else:
            pass

    return d

print(count_alphabets_digits('asdkf3'))