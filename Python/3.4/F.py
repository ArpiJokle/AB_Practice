import itertools

First = ["2", "3", "4", "5", "6", "7", "8", '9', "10", "валет", "дама", "король", "туз"]
Second = ["пик", "треф", "бубен", "червей"]
Second.remove(input())

for i, j in itertools.product(First, Second):
    print(i + ' ' + j)