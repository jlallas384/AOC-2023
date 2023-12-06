ans = 0
mx = {'red': 12, 'green': 13, 'blue': 14}

for i in range(999999999999999):
    try:
        alls = [[l.rstrip() for l in x.split(", ")] for x in input().split(": ")[1].split("; ")]
    except EOFError:
        break
    if all(all(mx[color] >= int(count) for count, color in [y.split(" ") for y in x]) for x in alls):
        ans += i + 1

print(ans)
