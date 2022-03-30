import time


def return_abc():
    alphabets = []
    for ch in "ABC":
        time.sleep(1)
        alphabets.append(ch)
    return alphabets


def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch


def yield_infinite_abc():
    while True:
        yield "A"
        yield "B"
        yield "C"

# def yield_abc():
#   yield from ["A", "B", "C"]


for ch in return_abc():
    print(ch)

for ch in yield_abc():
    print(ch)

for ch in yield_infinite_abc():
    print(ch)