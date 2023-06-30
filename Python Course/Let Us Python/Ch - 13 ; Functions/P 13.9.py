def create_sent1(s1, s2, s3):
    lst = []

    for w1 in s1:
        for w2 in s2:
            for w3 in s3:
                sent_ = f'{w1} {w2} {w3}'
                lst.append(sent_)

    return lst


def create_sent2(s1, s2, s3):
    lst = [f'{w1} {w2} {w3}' for w1 in s1 for w2 in s2 for w3 in s3]
    return lst

subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['TV Serials', 'Netflix']

for w in create_sent1(subjects, verbs, objects):
    print(w)

print()
for w2 in create_sent2(subjects, verbs, objects):
    print(w2)
