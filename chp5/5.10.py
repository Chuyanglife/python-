current_users=['chuyang','lixiang','yingcong','admin','jiayi']
t=[]
for names in current_users:
    t.append(names.lower())
new_users=['chuyang','yeehenrg','yingcong','junyu','jiayi']
for new_name in new_users:
    if new_name in t:
        print(f"You should change your name!")
    else:
        print(f"This name is available.")
