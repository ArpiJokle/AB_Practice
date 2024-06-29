NUM = int(input())
sum = 0
while NUM != 0:
	sum += NUM % 10
	NUM //= 10
print(sum)