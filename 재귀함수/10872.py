#팩토리얼
#  N(0 ≤ N ≤ 12)! 

def factorial(N):
    if N>0 and N<=12:
        return N*factorial(N-1)

    elif N==0 : return 1

N=int(input())
print(factorial(N))