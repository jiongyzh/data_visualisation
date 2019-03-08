import json
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
# from pygal.style import LightColorizedStyle

from country_codes import get_country_code


file_name = 'population_data.json'
with open(file_name) as f:
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for pop_dict in json.load(f):
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                if population < 10000000:
                    cc_pops_1[code] = population
                elif population < 1000000000:
                    cc_pops_2[code] = population
                else:
                    cc_pops_3[code] = population
            else:
                print('Error - ' + country_name)

    wm_style = RS('#336699', base_style=LCS)
    wm = pygal.maps.world.World(style=wm_style, value_formatter=lambda x: '{:,}'.format(x))
    wm.title = 'World Population in 2010, by Country'
    wm.add('0-10m', cc_pops_1)
    wm.add('10m-1bn', cc_pops_2)
    wm.add('>1bn', cc_pops_3)
    wm.render_to_file('world_population.svg')


def place_value(number):
    return "{:,}".format(number)
