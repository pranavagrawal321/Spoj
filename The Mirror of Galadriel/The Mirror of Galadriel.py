def check(s):
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if s[i:j + 1][::-1] not in s:
                return False
    return True


for _ in range(int(input())):
    s = input()
    print(["NO", "YES"][check(s)])
