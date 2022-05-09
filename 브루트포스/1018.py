#체스판 다시 칠하기
'''
MxN(8<=N,M<=50) 체스판에서 8X8로 잘라서 검은색, 흰색 칠하기
'''

N,M=map(int,input().split())
chess=[list(input()) for _ in range(N)]

def color_cnt(case):
    cnt=0
    for i in range(7):
        if case[0][i]=='B':
            if case[0][i+1]=='W':
                cnt=cnt
            else : 
                case[0][i+1]='W'
                cnt+=1
        else:
            if case[0][i+1]=='B':
                cnt=cnt
            else : 
                case[0][i+1]='B'
                cnt+=1
    case=list(map(list, zip(*case)))
    for i in range(8):
        for j in range(7):
            if case[i][j]=='B':
                if case[i][j+1]=='W':
                    cnt=cnt
                else : 
                    case[i][j+1]='W'
                    cnt+=1
            else:
                if case[i][j+1]=='B':
                    cnt=cnt
                else : 
                    case[i][j+1]='B'
                    cnt+=1
    return cnt

def change_first(case):
    if case[0][0]=='B':
        case[0][0]='W'
    else : case[0][0]='B'
    return case

cnt_list=[]
for i in range(N-8+1):
    for j in range(M-8+1):
        case=[row[j:j+8] for row in chess[i:i+8]]
        cnt_list.append(color_cnt(case))
        case2=change_first(case)
        #cnt_list.append(color_cnt(case2)+1)
print(min(cnt_list))
print(cnt_list)