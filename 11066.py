'''
11066번
'''
INF = 987654321
iteration = int(input())
cost = []
dp = []
psum = []

def f_dp(start , end):
    if start == end:
        return cost[start]

    if dp[start][end] != -1:
        return dp[start][end]

    m = INF
    for i in range(start,end):
        m = min(m, f_dp(start,i)+f_dp(i+1,end))
    dp[start][end] = m
    return m

for _ in range(iteration):
    cnt = int(input())

    dp = [[-1] * cnt for i in range(cnt)]
    

    psum = [0] * cnt
    cost = list(map(int,input().split()))
    minsum = INF

    for i in range(cnt): 
        dp[i][i] = cost[i]
        if i == 0:
            psum[i] = cost[i]
        else:
            psum[i] = psum[i-1] + cost[i]

    for i in range(cnt-1):
        minsum = min(minsum , f_dp(0,i) + f_dp(i + 1 ,cnt - 1))
        s = minsum + psum[-1]
        print(dp, s)
    print(s)
    
        
    