#N과 M 2

'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

N,M=map(int,input().split())

arr=[]
def backtracking(x):
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(x,N+1): #i다음의 숫자가 나와야 중복X
        if i in arr:
            continue
        arr.append(i)
        backtracking(i+1)
        arr.pop()

backtracking(1)