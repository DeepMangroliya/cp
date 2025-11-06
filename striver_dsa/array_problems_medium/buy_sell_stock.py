prices = list(map(int, input().split()))
profit, mini, cost = 0, prices[0], 0
for i in range(1, len(prices)):
    
    cost = prices[i] - mini
    profit = max(profit, cost)
    mini = min(prices[i], mini)

print(profit)