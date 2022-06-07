#다리놓기
'''
서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다.(이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.) 
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.
'''

#nCm(조합)
T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    N_facto, M_facto, N_M_facto=1,1,1
    for i in range(1,N+1):
        N_facto=N_facto*i
    for i in range(1,M+1):
        M_facto=M_facto*i
    for i in range(1,M-N+1):
        N_M_facto=N_M_facto*i

    print(M_facto//(N_facto*N_M_facto))
