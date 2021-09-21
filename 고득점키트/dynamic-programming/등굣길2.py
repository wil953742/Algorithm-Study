def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i==1 and j==1:
                continue
            
            if [i,j] in puddles:
                dp[j][i] = 0
                continue
        
            dp[j][i] = dp[j-1][i] + dp[j][i-1]
    
    return dp[n][m]%1000000007