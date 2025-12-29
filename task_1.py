import heapq

def find_min_connection_cost(cables):
    if not cables:
        return 0
    if len(cables) == 1:
        return 0

    heapq.heapify(cables)

    total_cost = 0
    merge_order = []

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        current_cost = first + second
        total_cost += current_cost

        merge_order.append(f"{first} + {second} = {current_cost}")

        heapq.heappush(cables, current_cost)

    return total_cost, merge_order

# Приклад використання:
cable_lengths = [12, 4, 8, 21, 2]
min_cost, steps = find_min_connection_cost(cable_lengths)

print("Порядок об'єднання кабелів:")
for i, step in enumerate(steps, 1):
    print(f"({i}) -> {step}")

print(f"\nМінімальні загальні витрати: {min_cost}")
