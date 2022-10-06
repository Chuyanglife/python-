
file="C:\\Users\\Admin\\OneDrive\\Desktop\\python_basic\\chp10\\guest_book.txt"

with open(file,'a') as file_1:
    while True:
        name=input("Enter your name: ")
        if name=='quit':
            break
        elif name=='cls':
            file_1.truncate()
            break
        else:
            file_1.write("The person is : "+ name +"\n")
        