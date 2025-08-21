def my_split(sentence, separator):
    words_lst = []
    word = ""
    for c in sentence:
        if c == separator:
            words_lst.append(word)
            word = ""
        else:
            word += c
    words_lst.append(word)
    return words_lst

def my_join(words_lst, separator):
    result = ""
    for i in range(len(words_lst)):
        result += words_lst[i]
        if i < len(words_lst) - 1:
            result += separator
    return result

sentence = input("Please enter sentence:")
words = my_split(sentence, " ")
print(my_join(words, ","))
for w in words:
    print(w)
