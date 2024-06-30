Set = set()
for i in range(int(input())):
    Set = Set.union(input().split())
print('\n'.join(Set))