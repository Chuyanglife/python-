favourite_places={'chuyang':['kuala lumpur','shanghai','taipei city'],
                  'lixiang':['california','pulau penang','new york city'],
                  'yeehenrg':['melborne','taichung','tainan']
                  }
for key,values in favourite_places.items():
    print(f"\n{key.title()}'s favourite places are:")
    for value in values:
        print(f"\t{value.title()}")