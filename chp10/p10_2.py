
f_name = 'C:\\Users\\Admin\\OneDrive\\Desktop\\python_basic\\chp10\\learning_python.txt'

with open(f_name) as f_name1:
    print("____'3'_____")
    lines=f_name1.readlines()
    for i in lines:
        c=i.replace('Python', 'c语言')
        print(c.rstrip()) 
with open(f_name) as f_name1:       
    print("_____'1'____")
    i=f_name1.read()
    c=i.replace('Python', 'C')
    print(c.rstrip())
with open(f_name) as f_name1:    
    print("_____'2'____")
    for i in f_name1:
        c=i.replace('Python', 'C')
        print(c.rstrip())