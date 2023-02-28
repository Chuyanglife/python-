from random import choice

m=1
my_ticket=['1','2','3','4','5','6']
lottery=[]

while True:
    outputs=choice(my_ticket)
    lottery.append(outputs)
    if outputs=='1':
        outputs=choice(my_ticket)
        if outputs=='3':
            outputs=choice(my_ticket)
            if outputs=='5':
                print("You are winner!")
                print(m)
                break
            else:
                m+=1
        else:
            m+=1
    else:
        m+=1

