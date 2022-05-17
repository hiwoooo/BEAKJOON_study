#숫자카드
'''
상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. -10,000,000<=card_num<=10,000,000
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며
각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
'''
N=int(input())
card_num=list(map(int, input().split()))
M=int(input())
card_check=list(map(int, input().split()))
card=set(card_check)&set(card_num) #차집합

ans={}
for i in range(M):
    ans[card_check[i]]=0
for x in card:
    ans[x]=1
    
for x in ans:
    print(ans[x], end=' ')