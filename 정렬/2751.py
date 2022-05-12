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
    while 1:
        if ahead_arr[]