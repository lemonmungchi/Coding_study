n,k=map(int,input().split())
coin_data=[]
for i in range(n):
    coin_data.append(int(input()))
coin_data.sort(reverse=True)
count=0
for i in coin_data:
    if k!=0:
        count+=k//i
        k%=i
print(count)

