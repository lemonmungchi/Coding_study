h=int(input())

count=0
for i in range(h):
    for j in range(60):
        for h in range(60):
            if '3' in str(i)+str(j)+str(h):
                count+=1

print(count)

#시간을 입력변수로 받고 나머지는 반복문 그리고 문자열로 합쳐서 in으로 확인