import sys

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)


def main():
	x = sys.argv[1]
	print x, fact(int(x))


if __name__ == "__main__":
    main()
