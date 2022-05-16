#좌표 정렬하기

N=int(input())
coordicate=[list(map(int,input().split())) for _ in range(N)]
coordicate.sort()
for i in range(N):
    print(*coordicate[i])

#또 시간초과.. pypy3로 해야 통과
#퀵/병합정렬로 해야 시간복잡도를 줄일 수 있다.

