def count_lower_upper(sentence):
    d = {
        'Lower' : 0,
        'Upper' : 0
    }

    for word in sentence.split():
        for letter in word:
            if letter.islower():
                d['Lower'] += 1
            elif letter.isupper():
                d['Upper'] += 1
            else:
                pass

    return d

print(count_lower_upper('My'))