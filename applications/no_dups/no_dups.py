def no_dups(s):
    # Your code here
    # strip and split the words
    words = s.strip().split()
    new = ""
    # dict
    lex = {}
    # if word is not in dict, add it, if it is in dict, do not add, return stripped word
    for word in words:
        if word not in lex.keys():
            lex[word] = 1
            new += word + " "
    return new.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))