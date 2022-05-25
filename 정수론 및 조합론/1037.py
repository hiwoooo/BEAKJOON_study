#약수
'''
A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
첫째 줄에 N(50이하의 자연수)의 진짜 약수의 개수가 주어진다.
'''

n=int(input())
factor=list(map(int,input().split()))
factor.sort()

if n%2==1:
    N=factor[n//2]**2
else :
    N=factor[-1]*factor[0]

print(N)