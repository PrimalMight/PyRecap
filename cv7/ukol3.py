def word_freq(text):
    my_dict = {}

    all_words = []

    for word in text.split(" "):
        new_word = [char for char in word if char.isalpha()]
        all_words.append("".join(new_word))
    for word in all_words:
        if not my_dict.get(word):
            my_dict[word] = 1
        else:
            my_dict[word] = 1 + my_dict.get(word)


    return my_dict

txt = "Alone, alone, all, all alone, alone on a wide wide sea!"
print(word_freq(txt.lower()))