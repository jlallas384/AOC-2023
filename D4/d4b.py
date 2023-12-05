alls  = []
counts = []
ans = 0
while True:
	try:
		s = input().split(": ")[1]
		s = s.split(" | ")
		a,b = [int(x) for x in s[0].split(" ") if x],[int(x) for x in s[1].split(" ") if x]
		count = sum(x in a for x in b)
		alls.append(count)
		counts.append(1)
	except EOFError:
		break

for i in range(len(alls)):
	for j in range(i + 1, i + 1 + alls[i]):
		counts[j] += counts[i]

print(sum(counts))