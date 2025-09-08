
money = [500,100,50,10,5,1]
price = int(input())
count = 0
change = 1000 - price
for m in money:
    count += change // m
    change%=m
print(count)
