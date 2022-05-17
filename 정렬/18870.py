#좌표압축
'''
수직선 위에 N개의 X좌표들을 입력,
Xi>Xj를 만족하는 좌표의 갯수
input : 2 4 -10 4 -9
output : 2 3 0 3 1
1 ≤ N ≤ 1,000,000
-10^9 ≤ Xi ≤ 109
'''

N=int(input())
X_axis=list(map(int,input().split()))
'''
def compact(arr,i):
    cnt=0
    a=arr[i]
    for x in list(set(arr)):
        if a>x:
            cnt+=1
    return cnt

for i in range(N):
    print(compact(X_axis, i), end=' ')
'''
#시간초과. list, sort하면 시간이 많이걸린다.
#딕셔너리로 풀면 적게 걸린다구..

X_sort=list(set(X_axis))
X_sort.sort()  # x좌표 중복제거하여 정렬
arr={}
for i in range(len(X_sort)): 
    arr[X_sort[i]]=i #정렬된 원소에 번호 부여(key, val)

#X_axis=[2 4 -10 4 -9]
#arr={-10: 0, -9: 1, 2: 2, 4: 3}

for x in X_axis: #각 원소의 value가 곧 답.
    print(arr[x], end=' ')