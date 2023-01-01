def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)

    # vowels = "aeiouAEIOU"
    # vowel_indexes = []
    # for x, letter in enumerate(s):
    #     if letter in vowels:
    #         vowel_indexes.append(x)
    # s[vowel_indexes[0]] = s[vowel_indexes[-1]]
    # s[vowel_indexes[-1]] = s[vowel_indexes[0]]

    # return s
