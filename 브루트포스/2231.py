#분해합
'''
256=(245+2+4+5)
245는 256의 생성자
'''
n=int(input())
ans=0
if n>=1 and n<=1000000:
    for i in range(n,0,-1):
        if i+sum(map(int,str(i)))==n: #각 자리수의 합: sum(map(int,str(x)))
            ans=i
    print(ans)
else : 
    print(ans)
