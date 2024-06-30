import itertools

words = input().split()

for i in itertools.accumulate(map(lambda x: ' ' + x, words)):
    print(i[1:])