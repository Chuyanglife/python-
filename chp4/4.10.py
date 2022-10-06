numbers = list(range(1,20,2))
print(f"The first three items in the list are:")
for num in numbers[:3]:
    print(num)
print(f"Three items from the middle of the list are:")
for num in numbers[4:7]:
    print(num)
print(f"The last three items int he list are:")
for num in numbers[-3:]:
    print(num)