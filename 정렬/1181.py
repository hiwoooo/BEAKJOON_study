#단어정렬
'''
1.길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
'''

N=int(input())
str_list=list(set([input() for _ in range(N) ]))
str_list.sort()
str_list.sort(key=lambda x:len(x))
print(*str_list, sep='\n')