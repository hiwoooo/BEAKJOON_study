#네 번째 점
'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
'''
from collections import Counter

square_x=[None]*3; square_y=[None]*3
for i in range(3):
    square_x[i],square_y[i]=map(int,input().split())

X=Counter(square_x)
Y=Counter(square_y)

print(*list(x for x in X.keys() if X[x]==1),end=' ')
print(*list(y for y in Y.keys() if Y[y]==1))