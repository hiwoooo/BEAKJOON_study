#N과 M 3
'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''


N,M=map(int, input().split())
arr=[]

def backtracking():
    if len(arr)==M:
        print(*arr)
        return

    for i in range(1,N+1):
        arr.append(i)
        backtracking()
        arr.pop()

backtracking()