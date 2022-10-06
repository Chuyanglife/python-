sandwich_orders=['tuna sandwich','pastrami','bacon sandwich','pastrami','egg sandwich','pastrami']
print("Pastrami is out of the deli.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("Only following sandwiches are available: ")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())
