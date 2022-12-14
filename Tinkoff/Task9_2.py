# costs = [35, 40, 101, 59, 63]

n = int(input())
costs = list(map(int, input().split()))

general_cost = 0
while costs:
    lunch = costs.pop(0)
    general_cost += lunch
    if costs and lunch > 100:
        costs.remove(max(costs))

print(general_cost)
