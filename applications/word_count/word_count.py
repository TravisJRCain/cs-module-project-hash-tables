def word_count(s):
    # Your code here
    # lowercase
    s = s.lower()
    # ignore these characters
    ignore = ['"',
        ":",
        ";",
        ",",
        ".",
        "-",
        "+",
        "=",
        "/",
        "\\",
        "|",
        "[",
        "]",
        "{",
        "}",
        "(",
        ")",
        "*",
        "^",
        "&",]

    for char in ignore:
        # replace characters with nothing
        s = s.replace(char, "")
        # dictionary
        counts = {}
        split = s.split()
        for word in split:
            if word in counts.keys():
                counts[word] += 1
            else:
                counts[word] = 1
        return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))