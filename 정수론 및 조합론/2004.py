#조합 0의 갯수
'''
이항계수의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
'''

N,M=map(int,input().split())

#시간초과
'''
numerator,denominator=1,1
for i in range(N-M,N+1):
    numerator=numerator*i

for i in range(1,M+1):
    denominator=denominator*i

ans=numerator//denominator
cnt=0
while ans%10==0:
    ans=ans//10
    cnt+=1
print(cnt)
'''


