y = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

total = 0

for key in y:
    # print(key)
    if type(y[key]) == int:
        total += y[key]
print(total)


# x = y['dog'] + y[19]
