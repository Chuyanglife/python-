
file="C:\\Users\\Admin\\OneDrive\\Desktop\\python_basic\\chp10\\programming_reason.txt"

with open(file,'a') as f:
    while True:
        reason=input("What is your programming_reason? ")
        if reason=='quit':
            break
        elif reason=='cls':
            f.truncate()
            break
        else:
            f.write("Your programming_reason is "+reason+'\n')
        