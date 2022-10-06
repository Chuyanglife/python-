rivers_country={'nile':'egypt',
        '长江':'china',
        'amazon river':'brazil'
        }
for key,value in rivers_country.items():
    print("The "+key.title()+" runs through "+value.title()+" .")
for key_river in rivers_country.keys():
    print(key_river.title())
for value_river in rivers_country.values():
    print(value_river.title())