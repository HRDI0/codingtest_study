n = int(input())
price_list = []
for _ in range(n):
    price_list.append(float(input()))
price_list.sort()
print(f'{price_list[1]:.2f}')