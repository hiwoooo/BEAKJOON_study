#이항계수1
'''
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.

이항계수 : 이항식을 이항 정리로 전개했을 때 각 항의 계수이며, 주어진 크기의 (순서 없는) 조합의 가짓수
n!/k!(n-k)!
'''

N,K=map(int,input().split())

n_facto,k_facto,n_k_facto=1,1,1
for i in range(1,N+1):
    n_facto=n_facto*i
for i in range(1,K+1):
    k_facto=k_facto*i
for i in range(1,N-K+1):
    n_k_facto=n_k_facto*i

print(n_facto//(k_facto*n_k_facto))