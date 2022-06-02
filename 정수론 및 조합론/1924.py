#최소공배수
'''
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
'''
T=int(input())

def gcd(a,b):
    while b>0:
        a,b=b, a%b
    return a

for _ in range(T):
    a,b=map(int,input().split())

    print(a*b//gcd(a,b))