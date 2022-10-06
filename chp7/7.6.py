#1
'''
prompt="\nWhat kind of toppings do you want?"
prompt+="\nEnter 'quit to end the program."

message=""
while message!='quit':
    message=input(prompt)

    if message!='quit':
        print("we will add "+message+'.')
'''
#2
'''
prompt="\nWhat kind of toppings do you want?"
prompt+="\nEnter 'quit to end the program."
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print("we will add "+message+'.')
'''
#3
prompt="\nWhat kind of toppings do you want?"
prompt+="\nEnter 'quit to end the program."

while True:
    message=input(prompt)
    if message=='quit':
        break
    else:
        print("we will add "+message+'.')