#링
'''
N개의 링이 앞에 있는 링과 뒤에 있는 링과 접하도록 바닥에 내려놓았다. 
첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 도는지 궁금해졌다.
링의 반지름이 주어진다. 이때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.
'''
from math import gcd
#파이썬내의 최대공약수 구하는 함수 이용
N=int(input())
radius=list(map(int,input().split()))

for i in range(1,N):
    numerator=radius[0]//gcd(radius[0],radius[i])
    denominator=radius[i]//gcd(radius[0],radius[i])
    print(f'{numerator}/{denominator}')


#유클리드호제법 이용시
'''
def GCD(a,b):
    while b>0:
        a,b=b, a%b
    return a

for i in range(1,N):
    numerator=radius[0]//GCD(radius[0],radius[i])
    denominator=radius[i]//GCD(radius[0],radius[i])    
    print(f'{numerator}/{denominator}')
'''