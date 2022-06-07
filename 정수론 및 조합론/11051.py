#이항계수2
'''
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
(1 ≤ \(N\) ≤ 1,000, 0 ≤ \(K\) ≤ \(N\))
'''
N,K=map(int, input().split())

n_facto,k_facto,n_k_facto=1,1,1
for i in range(1,N+1):
    n_facto=n_facto*i
for i in range(1,K+1):
    k_facto=k_facto*i
for i in range(1,N-K+1):
    n_k_facto=n_k_facto*i

print((n_facto//(k_facto*n_k_facto))%10007)

#10007은 대체 무슨 의미길래...?