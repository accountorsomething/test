def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in string_:
        if i in vowels:
            string_ = string_.replace(i,'')
    return string_

print(disemvowel("This website is for losers LOL!"))