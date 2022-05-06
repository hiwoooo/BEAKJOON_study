#블랙잭
'''
카드의 갯수 N, 카드숫자 합 최대M
N개의 카드 숫자 차례로 입력
'''

N,M=map(int,input().split())
card_list=list(map(int, input().split()))

card_sum=[]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            card_sum.append(card_list[i]+card_list[j]+card_list[k])

card_sum.sort()
if max(card_sum)<=M:
    print(max(card_sum))
else :
    for x in card_sum:
        if x<=M:
            ans=x
        else :
            print(ans)
            break