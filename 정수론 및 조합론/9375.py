#패션왕 신해빈
'''
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 
예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 

'''
T=int(input())
for _ in range(T):
    n=int(input())
    clothes=[]
    for _ in range(n):
        clothes.append(input().split()[-1])
    n=len(clothes)
    m=len(set(clothes))
    print(n+)