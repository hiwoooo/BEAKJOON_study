#배수와 약수
'''
두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
'''

arr=[]
while 1:
    arr.append(list(map(int,input().split())))
    if arr[-1]==[0,0]:
        arr.pop(-1)
        break

for i in range(len(arr)):
    if arr[i][1]%arr[i][0]==0:
        print('factor')
    elif arr[i][0]%arr[i][1]==0:
        print('multiple')
#    elif arr[i][0]%arr[i][1]!=0 and arr[i][1]%arr[i][0]!=0:
    else :
        print('neither')