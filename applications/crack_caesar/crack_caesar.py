# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from collections import defaultdict

# common letters
freq_list = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]

# open file
with open("ciphertext.txt") as file:
    ciphertext = file.read()

counts = defaultdict(int)

for c in ciphertext:
    if c.isupper():
        counts[c] += 1

cipher_freq = [item[0] for item in sorted(counts.items(), key=lambda x: x[1], reverse=True)]

lookup = {cipher: plain for cipher, plain in zip(cipher_freq, freq_list)}

print(ciphertext.translate(str.maketrans(lookup)))
