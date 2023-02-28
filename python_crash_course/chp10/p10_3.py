
f_name = 'C:\\Users\\Admin\\OneDrive\\Desktop\\python_basic\\chp10\\guest.txt'

with open(f_name,'r+') as f_name1:
    while True:
        name=input("Enter your name: ")
        if name=='quit':
            break
        elif name=='cls':
            f_name1.truncate()
            break
        else:
            f_name1.write("My name is: "+ name+"\n")