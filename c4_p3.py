import sys

loc=sys.stdin.readline()
row=int(loc[1])
col=int(ord(loc[0]))-int(ord('a'))+1    #ord=> 유니코드 변환 숫자연산하려고 a빼줌

go=[(2,1),(2,-1),(-2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)]

count=0
for go in go:
    next_r=row+go[0]
    next_c=col+go[1]
    if next_r>=1 and next_c<=8 and next_r<=8 and next_c>=1:
        count+=1

print(count)