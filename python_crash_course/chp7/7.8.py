sandwich_orders=['tuna sandwich','bacon sandwich','egg sandwich']
finished_sandwiches=[]
for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order.title()}.")

while sandwich_orders:
    making_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(making_sandwich)

print("\nI have made following sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
