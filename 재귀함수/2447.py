#별찍기 10
'''
N=3일때
***
* *
***

'''

#실패/필사..

def append_star(n):
    if n==1:
        return ['*']
    
    stars=append_star(n//3)
    L=[]

    for s in stars: 
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(n//3)+s)
    for s in stars:
        L.append(s*3)
    return L

print('\n'.join(append_star(int(input()))))