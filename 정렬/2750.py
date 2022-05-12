#수 정렬하기
'''
N(1<=N<=1,000)개의 숫자 입력 후 오름차순
'''

N=int(input())
num_list=[]
for n in range(N):
    num_list.append(int(input()))

num_list.sort()
print(*num_list,sep='\n')