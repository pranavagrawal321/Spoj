while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        print("AP", c + b - a) if b - a == c - b else print("GP", c * (c//b))
