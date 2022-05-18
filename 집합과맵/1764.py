#듣보잠
'''
첫째 줄에 듣도 못한 사람의 수 N(500,000 이하의 자연수), 보도 못한 사람의 수 M(500,000 이하의 자연수) 입력
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하.
각 명단에는 중복되는 이름이 없으며, 듣보잡의 수와 그 명단을 사전순으로 출력하라.
'''
from collections import Counter

N,M=map(int,input().split())
Nname=[input() for _ in range(N)]
Mname=[input()for _ in range(M)]

dbj=set(Nname)&set(Mname)
print(len(dbj))
print(*sorted(dbj),sep='\n')