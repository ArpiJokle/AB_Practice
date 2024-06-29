Str = input().replace(" ", "")
if Str.lower() == Str.lower()[::-1]:
    print("YES")
    exit()
print("NO")