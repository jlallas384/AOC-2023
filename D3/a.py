g = []
while True:
    try:
        g.append('.' + input().rstrip() + '.')
    except EOFError:
        break
ans = 0
def check(i, j):
    if i == -1 or i == len(g):
        return False
    return g[i][j] != '.'

for i in range(len(g)):
    s = ""
    for ind, v in enumerate(g[i]):
        if v.isdigit():
            s = s + v
        elif s != "":
            val = int(s)
            has = check(i, ind - len(s) - 1) or check(i, ind)
            for j in range(ind - len(s), ind):
                has |= check(i + 1, j) or check(i - 1, j)
            has |= check(i - 1, ind - len(s) - 1) 
                    or check(i + 1, ind - len(s) - 1) 
                    or check(i - 1, ind) 
                    or check(i + 1, ind)
            s = ""
            if has:
                ans += val
print(ans)
