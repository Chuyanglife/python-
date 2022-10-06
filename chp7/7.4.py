prompt="\nWhat kind of toppings do you want?"
prompt+="\nEnter 'quit' to end the program."

active=True
while active:
    message=input(prompt)
    if message=='quit':
        break
    else:
        print("We will add: "+message+'.')