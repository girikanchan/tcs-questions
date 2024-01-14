n = int(input())
prime = [0] * (n+1)

for i in range(2, n + 1):
    if prime[i] == 0:
        for j in range(i*i, n + 1, i):
            prime[j] += 1

for i in range(2,n+1):
    if prime[i]==0:
        print(i,end= " ")