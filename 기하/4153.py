#직각삼각형
'''
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
'''

triangle=[]
cnt=0
while 1:
    triangle.append(list(map(int, input().split())))
    if triangle[cnt]==[0,0,0]:
        triangle.remove(triangle[cnt])
        break
    cnt+=1

for i in range(len(triangle)):
    triangle[i].sort()
    if triangle[i][0]**2 + triangle[i][1]**2 == triangle[i][2]**2:
        print('right')
    else : print('wrong')