import json
from country_codes import get_country_code


file_name = 'population_data.json',
with open(file_name) as f:
    for pop_dict in json.load(f):
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                print(code + ': ' + str(population))
            else:
                print('Error - ' + country_name)
