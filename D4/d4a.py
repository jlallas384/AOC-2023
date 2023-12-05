ans = 0

while True:
	try:
		s = input().split(": ")[1]
		s = s.split(" | ")
		a,b = [int(x) for x in s[0].split(" ") if x],[int(x) for x in s[1].split(" ") if x]
		count = sum(x in a for x in b)
		if count:
			ans += 2 ** (count - 1)
	except EOFError:
		break
print(ans)
