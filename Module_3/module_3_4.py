def single_root_words(root_word, *other_words):
    same_words = []
    root_low = root_word.lower()
    other_words = list(other_words)

    for i in other_words:
        other_low = i.lower()
        find_root_in_other = other_low.find(root_low)
        if find_root_in_other != -1:
            same_words.append(i)
            same_words.append(root_word)
    for j in other_words:
        other_low_2 = j.lower()
        find_other_in_root = root_low.find(other_low_2)
        if find_other_in_root != -1:
            same_words.append(j)
    same_words = set(same_words)
    same_words = list(same_words)
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))