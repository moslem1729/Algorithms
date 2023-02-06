array=[7,10,12,7,9,14]

def max_subset_sum(array):
    dp=[0 for _ in array]
    dp[0],dp[1]=array[0],array[1]
    for i in  range(2,len(array)):
        dp[i]=max(array[i]+dp[i-2],dp[i-1])

    return dp[-1]

print(max_subset_sum(array))