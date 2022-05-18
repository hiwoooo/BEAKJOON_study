#숫자카드2
'''
상근이는 숫자 카드 N(1 ≤ N ≤ 500,000)개를 가지고 있다. 
정수 M(1 ≤ M ≤ 500,000)개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
'''

'''
list에서 카운팅하면 시간초과.
시간복잡도를 줄이는 알고리즘 공부를 하자..
'''
#이진탐색

N=int(input())
Ncard=sorted(map(int,input().split()))
M=int(input())
Mcard=list(map(int,input().split()))

def binary(n,Ncard,start,end):
    if start>end:
        return 0
    m=(start+end)//2
    if n==Ncard[m]: #가운데 원소일때 
        return N[start:end+1].count(n) #리스트에서 원소 카운팅
    elif n<N[m]: #반 나눴을 때 왼쪽의 원소일 경우
        return binary(n,Ncard,start,m-1) #왼쪽의 리스트로 재귀함수
    else : #반으로 나눴을 때 오른쪽의 원소일 경우
        return binary(n,Ncard,m+1,end) #오른쪽 리스트로 재귀함수

ans={}
for n in Ncard:
    start=0
    end=N-1
    if n not in ans: #Ncard리스트 내 n원소 카운팅, 중복된 원소가 나올 경우 skip
        ans[n]=binary(n,Ncard,start,end)

'''
근데 이걸 한줄로 요약하면(Conter함수) 
ans=Counter(Ncard)

'''
print(' '.join(str(ans[x]) if x in ans else '0' for x in Mcard))
#Mcard의 원소의 key를 갖는 ans의 value값 출력. key없으면 0