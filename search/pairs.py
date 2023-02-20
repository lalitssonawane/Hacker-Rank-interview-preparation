#Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    a.sort()
    left = 0
    right = 1
    answer = 0
    while right < len(a):
        val = a[right]-a[left]
        if val == k:
            answer += 1
            left += 1
            right += 1
        elif val < k:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1

    return answer
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
