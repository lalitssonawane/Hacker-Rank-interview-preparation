#We define the following:

#A subarray of array  of length  is a contiguous segment from  through  where .

from bisect import bisect,insort

T = int(input())
for _ in range(T):
    N,M = [int(i) for i in input().split()]
    ar = [int(i) for i in input().split()]
    
    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0
    
    for i in range(N):
        sum_so_far = (sum_so_far + ar[i]) % M        
        pos = bisect(cumulative_sums, sum_so_far)
        d = 0 if pos == i else cumulative_sums[pos]
        max_sum = max(max_sum, (sum_so_far + M - d) % M)
        insort(cumulative_sums, sum_so_far)
    
    print(max_sum)