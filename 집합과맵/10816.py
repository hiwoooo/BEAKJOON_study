#숫자카드2
'''
상근이는 숫자 카드 N(1 ≤ N ≤ 500,000)개를 가지고 있다. 
정수 M(1 ≤ M ≤ 500,000)개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
'''
from collections import Counter

N=int(input())
Ncard=list(map(int,input().split()))
M=int(input())
#cnt = {x: 0 for x in map(int, input().split())}
Mcard=list(map(int,input().split()))

cnt=Counter(Ncard)
'''for card in Ncard:
    if card in cnt.keys():
        cnt[card]+=1

print(*cnt.values())
'''
#M을 바로 conuter함수쓰면 M이 중복되는 경우에 오답.
#N을 카운팅해서 M과 같은 경우에만 value를 넣어주고 아니면 0을 넣는다.

print(' '.join(f'{cnt[m]}' if m in cnt else '0' for m in Mcard))