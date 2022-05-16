#소트인사이드
N=int(input())
n=[]
while N>=1:   
    n.append(N%10)
    N=N//10
n.sort(reverse=True)
print(''.join(str(x) for x in n))
