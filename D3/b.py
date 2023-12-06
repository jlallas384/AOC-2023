g = []
while True:
    try:
        g.append('.' + input().rstrip() + '.')
    except EOFError:
        break
ans = 0

muls = [[[] for i in range(len(x))] for x in g]

def check(i, j):
    if i == -1 or i == len(g):
        return False
    if g[i][j] == '*':
        muls[i][j].append(val)

for i in range(len(g)):
    s = ""
    for ind, v in enumerate(g[i]):
        if v.isdigit():
            s = s + v
        elif s != "":
            val = int(s)
            check(i, ind - len(s) - 1)
            check(i, ind)
            for j in range(ind - len(s), ind):
                check(i + 1, j)
                check(i - 1, j)
            check(i - 1, ind - len(s) - 1)
            check(i + 1, ind - len(s) - 1)
            check(i - 1, ind)
            check(i + 1, ind)
            s = ""

print(sum(x[0] * x[1] for ll in muls for x in ll if len(x) == 2))
