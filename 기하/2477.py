#참외밭
'''
첫 번째 줄에 1m2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1 ≤ K ≤ 20)가 주어진다. 
참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이(1 이상 500 이하의 정수)가 
둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다. 
변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.
'''
N=int(input())
farm=[list(map(int, input().split()))for _ in range(6)]
width=[]; height=[]; way=[]
farm.append(farm[0])
farm.append(farm[1])
for i in range(len(farm)):
    way.append(farm[i][0])
    if farm[i][0]<=2 :
        width.append(farm[i][1])
    else : 
        height.append(farm[i][1])

for i in range(6):
    if way[i:i+3]==[3,1,3] or way[i:i+3]==[4,1,4] or way[i:i+3]==[3,2,3] or way[i:i+3]==[4,2,4]:
        area=farm[i+1][1]*farm[i+2][1]

print((max(width)*max(height)-area)*N)