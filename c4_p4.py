import sys                  #왼쪽돌면서 미로 찾기랑 같음

a,b = map(int,sys.stdin.readline().split())

map=[[0]*a for _ in range(b)]

x,y,d = map(int,sys.stdin.readline().split())

map[x][y]=1

array=[]

for i in range(a):
    array.append(list(map(int,sys.stdin.readline().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global d
    d-=1
    if d==-1:
        d=3

count=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[d]
    ny=y+dy[d]

    if map[nx][ny]==0 and array[nx][ny]==0:
        map[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:
        nx=x-dx[d]
        ny=y+dy[d]

        if array[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0

print(count)


