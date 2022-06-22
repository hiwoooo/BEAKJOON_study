# N과 M 1
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

'''
백트래킹
백트래킹은 DFS(Depth-First Search, 깊이 우선 탐색)의 방식을 기반으로, 불필요한 경우를 배제하며 원하는 해답에 도달할 때까지 탐색하는 전략
DFS를 기반으로 두고 있기 때문에 스택(Stack)을 이용해 퇴각을 하며 다음 탐색을 진행하기 때문에 백트래킹(또는 퇴각검색)이라 불린다.
'''

N,M=map(int,input().split())
arr=[]
def backtracking():
    if len(arr)==M: #탈출
        print(*arr)
        return

    for i in range(1,N+1):
        if i in arr:
            continue
        arr.append(i)
        backtracking()
        arr.pop()

backtracking()