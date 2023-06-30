def frequency(s):
    freq = {}
    for word in s.split():
        freq[word] = freq.get(word, 0) + 1

    return freq

for x,y in frequency('Hi meaw meaw how').items():
    print(f'{x} : {y}')