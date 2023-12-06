ans = 0
mx = {'red': 12, 'green': 13, 'blue': 14}

for i in range(999999999999999):
    try:
        alls = [l.rstrip() for x in input().split(": ")[1].split("; ") for l in x.split(", ")]
    except EOFError:
        break
    prod = 1
    for col in ["red", "blue", "green"]:
        prod *= max(int(count) for count, color in [x.split(" ") for x in alls] if color == col)
    ans += prod
print(ans)
