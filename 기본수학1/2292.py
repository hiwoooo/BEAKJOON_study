#벌집


N=int(input())
cnt=1
for i in range(0,N,6):
    N=N-i
    if N>1:
        cnt+=1
    else: break
print(cnt)
