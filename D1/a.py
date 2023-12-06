ans = 0
while True:
    try:
        s = input()
        dig =  ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        d = []
        for i in range(len(s)):
            if s[i].isdigit():
                d.append(int(s[i]))
        ans += d[0] * 10 + d[-1]
    except:
        print(ans)
        exit()