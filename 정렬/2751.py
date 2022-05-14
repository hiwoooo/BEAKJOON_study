#수 정렬하기
'''
N(1 ≤ N ≤ 1,000,000)개의 숫자 오름차순 정렬
시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다. 예를 들면 병합 정렬, 힙 정렬 등.
병합정렬로 풀어보겠다.!
'''
N=int(input())

def merge_sort(arr):
    if len(arr)<2:
        return arr
    
    mid=len(arr)//2
    ahead_arr=merge_sort(arr[:mid])
    back_arr=merge_sort(arr[mid:])

    merged_arr=[]
    l=h=0
    while l<len(ahead_arr) and h<len(back_arr):
        if ahead_arr[l]<back_arr[h]:
            merged_arr.append(ahead_arr[l])
            l+=1
        else :
            merged_arr.append(back_arr[h])
            h+=1
    merged_arr+=ahead_arr[l:]
    merged_arr+=back_arr[h:]

    return merged_arr

arr=[]
for _ in range(N):
    arr.append(int(input()))

print(*merge_sort(arr), sep='\n')