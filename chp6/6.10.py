favourite_num_friends={'chuyang':['1','6','7'],
                       'danny':['2','7','9'],
                       'yibing':['3','4','8'],
                       'deehan':['4','6','8'],
                       'jeff':['5','8','9']
                       }
for keys,values in favourite_num_friends.items():
    print(f"\n{keys.title()}'s favourite numbers are:")
    for value in values:
        print(f"\t{value.title()}")
#print("chuyang 喜欢的数字是：" + str(favourite_num_friends["chuyang"]) + ".")