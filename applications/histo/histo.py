# Your code here

def word_count(s):

    # Your code here
    s = s.lower()
    ignore = [
        '"',
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
        "&",
    ]

    for char in ignore:
        s = s.replace(char, "")
    counts ={}
    split = s.split()
    for word in split:
        if word in counts.keys():
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# open file
with open("robin.txt") as file:
    s = file.read()

counts = word_count(s)
width = max([len(word) for word in counts.keys()]) + 2

counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

print(counts)

for count in counts:
    # aligns the words on the left side
    print(f"{count[0].ljust(width)}" + "#" * count[1])