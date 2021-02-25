n , k = map(int, input().split())

coinval = []
for i in range(n):
    coinval.append(int(input()))

sumcoin = 0
for i in reversed(range(n)):
    sumcoin += int(k / coinval[i])
    k = k % coinval[i]

print(sumcoin)