#대칭차집합

N,M=map(int,input().split())
Nset={x for x in map(int,input().split())}
Mset={x for x in map(int,input().split())}

print(len(Mset^Nset))