def hanoi(n, k, a=1, b=2, c=3):
	if (k == pow(2, n-1)):
		print("{} -> {}".format(a, c))
	elif (k < pow(2, n-1)):
		hanoi(n-1, k, a, c, b)
	else:
		hanoi(n-1, k-pow(2, n-1), b, a, c)


if __name__ == "__main__":
	n = 64
	k = 18446744073709551615
	hanoi(n, k)


# EOF

