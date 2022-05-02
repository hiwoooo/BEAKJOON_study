#피보나치수열
#n은 20보다 작거나 같은 자연수 또는 0이다

def fibo(n):
    global fibo_list
    if n>=2 and n<=20:
        return fibo(n-2)+fibo(n-1)
    elif n==0 or n==1: return n
    else : return 0

print(fibo(int(input())))