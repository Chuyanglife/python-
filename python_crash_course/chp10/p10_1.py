
f_name = 'C:\\Users\\Admin\\OneDrive\\Desktop\\python_basic\\chp10\\learning_python.txt'

with open(f_name) as f_name1:
    print("_____'1'____")
    print(f_name1.read())
with open(f_name) as f_name1:
    print("_____'2'____")
    for i in f_name1:
        print(i.rstrip())
with open(f_name) as f_name1:
    print("_____'3'____")
    lines=f_name1.readlines()
    for i in lines:
        print(i.rstrip())