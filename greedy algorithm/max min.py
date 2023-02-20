#You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

def maxMin(k, arr):
    k-=1
    arr.sort()
    return min(arr[i+k]-arr[i] for i in range(len(arr)-k))

n = int(input())
k = int(input())
arr = [int(input()) for _ in range(n)]
print(maxMin(k, arr))