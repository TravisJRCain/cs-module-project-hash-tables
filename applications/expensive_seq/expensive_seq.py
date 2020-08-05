# Your code here
cache = {}

def expensive_seq(x, y, z):
    # Your code here
    # start with if x is less than or equal to zero
    if x <= 0:
        # if the element is in our cache already, return
        if (x, y, z) in cache:
            return cache[(x, y, z)]
        # set current slot
        cache[(x, y, z)] = y + z
        # return current slot
        return cache[(x, y, z)]
    # if x is greater than zero
    if x > 0:
        # element in cache already
        if (x, y, z) in cache:
            return cache[(x, y, z)]
        # set current slot
        cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        # return current slot
        return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
