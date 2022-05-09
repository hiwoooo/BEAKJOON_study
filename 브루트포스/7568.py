#덩치
'''
A(x,y) B(p,q) 
x>p, y>q이면 A가 B보다 덩치가 크다
'''

N=int(input())
physicalTable=[list(map(int,input().split()))for _ in range(N)]
rank=[]

for x in physicalTable:
    cnt=1
    for y in physicalTable:
        if x[0]<y[0] and x[1]<y[1]:
            cnt+=1
    rank.append(cnt)

print(*rank)