#하노이탑

def Hanoi(n,pos1,pos3,pos2):
    if n==1:
        print(pos1, pos3)
    else : 
        Hanoi(n-1,pos1,pos2,pos3)

        print(pos1, pos3)

        Hanoi(n-1,pos2,pos3,pos1)

n=int(input())
print(2**n-1)
Hanoi(n,1,3,2)