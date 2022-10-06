def describe_city(name,country='malaysia'):
    print(f"{name.title()} is in {country.title()}. ")

#name=input(f"Enter your city's name. ")
#country=input(f"Enter your country'name. ")
describe_city('pulau penang')
describe_city('shanghai','china')
describe_city(name='new york city',country='united state of america')