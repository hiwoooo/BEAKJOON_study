#영화감독 숌
'''
666이 들어간 수 작은수부터 차례로 나열하기
666,1666,2666,3666,4666,5666,6660,6661,...,6669,7666,8666,9666,
10666,11666,...
'''
N=int(input())
'''
movie=[i for i in range(1,3000000)]
title=[]

for x in movie:
    if str(x).find('666')>=0:
        title.append(x)
    if len(title)==N:
        break

print(title[N-1])
'''
#코드리뷰 : 메모리너무 크고 시간 너무 오래걸림. 수정필요

title=666
while 1:
    if '666' in str(title):
        N-=1
        if N==0: break
    title+=1 #666이 나올때까지 계속 더해준다, 나오면 N차감
print(title)