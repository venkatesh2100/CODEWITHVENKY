
MOD = 10**9 + 7
MAX = 10**6

fact = [1] * (MAX + 1)
inv_fact=[1]*(MAX + 1)

for i in range(1,MAX+1):
    fact[i] = fact[i-1] * i %MOD

inv_fact[MAX] = pow(fact[max],MOD-2,MOD)


for i in range(MAX-1,0,-1):
    inv_fact[i] = fact[i+1] * (i+1)%MOD


def nCr(n,r):
    if r < 0 or r > n:
        return 0
    return  fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

T = int(input())

for _ in range(T):
    n = int(input())
    r = int(input())
    print(nCr(n,r))

