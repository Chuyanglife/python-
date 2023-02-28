cities={
    'new york city':{
        'country':'USA',
        'population':'80,000,000',
        'fact':'delicious'
        },
    'london':{
        'country':'england',
        'population':'30,000,000',
        'fact':'old'
    },
    'tokyo':{
        'country':'japan',
        'population':'40,000,000',
        'fact':'crowd'
    }
}
for keys,values in cities.items():
    print(f"\ncity: {keys.title()}")
    country=values['country']
    population=values['population']
    fact=values['fact']
    print(f"\tcountry: {country.title()}")
    print(f"\tpopulation: {population.title()}")
    print(f"\tfact: {fact.title()}")
   # print(f"\t{values['fact'].title()}")