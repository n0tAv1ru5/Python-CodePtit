t = int(input())
for k in range(t) :
	n, s = 2 * int(input()), 0
	for i in range(2, int(n ** 0.5) + 1) :
		if n % i == 0 :
			a, b = n / i, i
			k = a - b + 1
			if k % 2 == 0 :
				l = (a - b + 1) / 2
				r = a - l 
				if r >= 1 and r > l : s += 1
	print(s)

