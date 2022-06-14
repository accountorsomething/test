def duplicate_count(text):
    new_text = text.lower()

    num = 0
    dict = {}

    for i in range(0,len(new_text)):
        dict[new_text[i]] = 0

    for key in dict:
        for i in range(0,len(new_text)):
            if(key == new_text[i]):
                dict[key] = dict[key] + 1
    
    for key in dict:
        if dict[key] > 1:
            num = num + 1

    print(dict)
    return num

print(duplicate_count("aslkdjas"))