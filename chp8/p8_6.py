def city_country(name,country):
    country_name=f"{name.title()}, {country.title()}"
   # print(country_name)
    return country_name

name1=city_country('tokyo','japan')
name2=city_country('kuala lumpur','malaysia')
name3=city_country(name='santiago',country='chile')
print(name1)
print(name2)
print(name3)