#앵그리창영
'''
박스의 크기와 성냥의 길이가 주어졌을 때, 성냥이 박스에 들어갈 수 있는지 없는지를 구하는 프로그램을 작성하시오. 
첫째 줄에 던진 성냥의 개수 N과 박스의 가로 크기 W와 세로 크기 H가 주어진다. (1 ≤ N ≤ 50, 1 ≤ W, H ≤ 100)
성냥의 길이는 1보다 크거나 같고 1000보다 작거나 같은 자연수이다.
박스안에 들어갈 수 있으면 "DA" 없으면 "NE"를 출력한다. 
'''

from math import sqrt


N,W,H=map(int, input().split())
Matchs=list(int(input())for _ in range(N))

for x in Matchs:
    if x<=sqrt(W**2+H**2):
        print('DA')
    else : 
        print('NE')
