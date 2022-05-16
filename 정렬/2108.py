#통계학
'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
from collections import Counter

N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))

def arithmetic_mean(arr):
    return round(sum(arr)/len(arr))

def median_value(arr):
    arr.sort()
    return arr[len(arr)//2]

def Mode(arr):
    arr.sort()
    cnt=Counter(arr).most_common()
    if len(cnt)==1:
        return cnt[0][0]
    elif cnt[0][1]==cnt[1][1]:
        return cnt[1][1]
    else :
        return cnt[0][0]

def Range(arr):
    return max(arr)-min(arr)

print(arithmetic_mean(arr))
print(median_value(arr))
print(Mode(arr))
print(Range(arr))

#python3 실행 시 시간초과, PyPy가 속도가 빠르다고 하여 pypy3로 돌리니 통과.
