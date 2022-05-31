def rotate_word(word, amount):
    
    rotated_word = ""

    for char in word:
        asc = ord(char) + amount
        if asc > 122:
            asc = 97 + asc - 123

        rotated_word += chr(asc)
    
    return rotated_word

print(rotate_word("jelly", 13))