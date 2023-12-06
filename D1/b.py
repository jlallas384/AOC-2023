ans = 0
while True:
    try:
        s = input()
        dig =  ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        d = []
        for i in range(len(s)):
            if s[i].isdigit():
                d.append(int(s[i]))
            for j in range(0, 9):
                if i + len(dig[j]) <= len(s) and s[i: i + len(dig[j])] == dig[j]:
                    d.append(j + 1)
                    break
        ans += d[0] * 10 + d[-1]
    except:
        print(ans)
        exit()