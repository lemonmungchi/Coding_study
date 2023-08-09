import sys

def binary_search(array,target,start,end):
    mid=(start+end)//2

    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    return None

n=int(sys.stdin.readline().rstrip())

array=list(map(int,sys.stdin.readline().split()))
array.sort()

a=int(sys.stdin.readline().rstrip())
x=list(map(int,sys.stdin.readline().split()))

for i in x:
    result=binary_search(array,i,0,len(array))
    if result!=None:
        print('yes',end=' ')
    else:
        print('no',end=' ')
