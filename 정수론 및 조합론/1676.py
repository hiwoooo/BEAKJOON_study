#팩토리얼 0의 개수
'''
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
'''

N=int(input())
ans, cnt=1,0
for n in range(1,N+1):
    ans*=n

while ans%10==0:
    ans=ans//10
    cnt+=1
print(cnt)
