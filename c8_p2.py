import sys

n=int(sys.stdin.readline())

array=list(map(int,sys.stdin.readline().split()))

d=[0]*100

d[0]=array[0]                   #초기값 설정
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])        #점화식작성

print(d[n-1])