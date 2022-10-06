while True:
    prompt="\nPlease enter your age,and then we will tell you huw much you shall pay."
    prompt+="\nEnter 'quit' to end the program."
    age=input(prompt)

    if age== 'quit':
        break
    if int(age)<3:
        print("Your cost is $0.")
    elif int(age)<=12:
        print("Your cost is $10.")
    else:
        print("Your cost is $15.")