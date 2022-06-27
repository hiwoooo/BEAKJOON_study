# N과 M(4)
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다. 고른 수열은 비내림차순이어야 한다.
'''

N,M= map(int, input().split())
arr=[]
def DFS(x,cnt):
    if cnt-1==M:
        print(*arr)
        return 
    
    for i in range(x,N+1):

        arr.append(i)
        DFS(i,cnt+1)
        arr.pop()

DFS(1,1)