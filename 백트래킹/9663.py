#N-Queen
'''
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제.
N(1≤ N<15)이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''
#퀸의 좌우상하 대각선에 다른 퀸이 없어야한다.

N=int(input())
chess=[0]*N
#Qcheck=[0]*N

cnt=0
def isPossible(depth):
    global chess
    for i in range(depth):
        if chess[depth]==chess[i] or abs(chess[i]-chess[depth])==abs(depth-i): 
        #직선방향, 대각선 방향 검사
            return False #존재하면 False로 반환
    return True #없을때 가지치기

def DFS(depth):
    global cnt
    if depth==N:
        cnt+=1
        return

    for i in range(N): 
        chess[depth]=i
        if isPossible(depth):
            DFS(depth+1)

DFS(0)
print(cnt)

#시간초과
#pypy3로제출했을 때 통과.
#이후에 다시 복습해볼것.