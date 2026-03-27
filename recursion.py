def num(n):
    if n == 0:
        return 0
    
    return n + num(n-1)
print(num(4))


def power(x,n):
    if n == 0:
        return 1
    half = power(x,n // 2)
    if half % 2== 0:
        return half * half
    else:
        return x * half * half
print(power(2,2))

#to check ifthe array is sorted 
def issorted(arr,n):
    if n == 1:
        return True
    if arr[n-1] <= arr[n-2]:
        return False
    return issorted(arr,n-1) 
print(issorted([1,1,1,1],4))

#Print ALL subsequences of a string
def subseq(s,k):
    if k == 0:
        return ""
    print()
    return subseq(s,k-1)
print(subseq("abc",3))
