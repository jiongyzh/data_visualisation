import pygal


def get_country_code(counttry_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in pygal.maps.world.COUNTRIES.items():
        print(code + ': ' + name)
        if name == counttry_name:
            return code
    return None