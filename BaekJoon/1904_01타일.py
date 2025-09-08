N = int(input())

a = [1,2]

for i in range(2,N):
    a.append((a[i-2]+a[i-1])%15746)

print(a[N-1])