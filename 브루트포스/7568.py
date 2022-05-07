#덩치
'''
A(x,y) B(p,q) 
x>p, y>q이면 A가 B보다 덩치가 크다
'''

N=int(input())
physicalTable=[list(map(int,input().split()))for _ in range(N)]
rank=[0]*N

for i in range(N):
    for j in range(2):