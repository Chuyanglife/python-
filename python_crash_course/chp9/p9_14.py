from random import choice

output=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']
lottery=[]
for i in range(4):
    outputs=choice(output)
    lottery.append(outputs)
print(f"The winner number is {lottery}")