n = int(input())

for i in range(0, n):
    for j in range(3 + i, 0, -1):
        print("До старта " + str(j) + " секунд(ы)")
    print("Старт " + str(i + 1) + "!!!")