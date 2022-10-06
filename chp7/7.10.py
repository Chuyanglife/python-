responses={}

poll=True
while poll:
    name=input("What's you name?: ")
    place=input("If you could visit one place in the world, where would you go?: ")
    responses[name]=place
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        poll=False
print("----Polling Result----")
for name,place in responses.items():
    print("If "+name.title()+" could visit one place in the world, he/she would go "+ place.title()+ ".")