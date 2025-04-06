def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    print(new)

    if new == objects:
        return True
    return False


def char(x):
    return x % 2 == 0


values = [0, 2, 10, 6]
print(same_by(char, values))