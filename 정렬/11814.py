#나이순 정렬
'''
사람들의 나이와 이름을 순서대로 입력
나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬
'''
N=int(input())
member=[list(map(str, input().split()))for _ in range(N)]
member.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(*member[i])

# 시간이 오래 걸렸다.
#다른 사람 코드
N=int(input())
member={}
for i in range(1,201):
    member[i]=[] #공백의 2차원
for i in range(N):
    age, name=map(str, input().split())
    member[int(age)].append(name) # 나이번째 리스트에 이름들 추가, #정렬필요없다
for i in range(1,201):
    for name in member[i]: #리스트에 값이 있는것들만 차례로 출력
        print(str(i)+' '+ name)


