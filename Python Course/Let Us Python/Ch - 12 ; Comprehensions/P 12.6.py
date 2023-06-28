words = {
    'Avik' : 1,
    'Vurchas' : 2
}

dictionary = {''.join(vowel for vowel in k if vowel not in 'aeiou') : v for (k,v) in words.items()}
print(dictionary)