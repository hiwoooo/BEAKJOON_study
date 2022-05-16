#좌표압축
'''
수직선 위에 N개의 X좌표들을 입력,
Xi>Xj를 만족하는 좌표의 갯수
input : 2 4 -10 4 -9
output : 2 3 0 3 1
'''

N=int(input())
X_axis=list(map(int,input().split()))

def compact(arr,i):
    cnt=0
    a=arr[i]
    arr.pop(i)
    for x in arr:
        if a>x:
            cnt+=1
    return cnt

for i in range(N):
    print(compact(X_axis, i))
