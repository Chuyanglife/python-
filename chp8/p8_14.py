def make_car(brand,model,**user_info):
    user_info['brand'] = brand
    user_info['model'] = model
    return user_info

car=make_car('subaru','outback',
             color='blue',
             tow_package=True)
print(car)
