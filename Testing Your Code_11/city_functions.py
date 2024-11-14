"""A collection of functions for working with cities."""

# def city_country(city, country):
#     """Return a string like 'Santiago, Chile'."""
#     full_name = city.title() + ", " + country.title()
#     return full_name


"""A collection of functions for working with cities."""


def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""

    output_string = city.title() + ", " + country.title()
    if population:
        output_string += " - population " + str(population)
    return output_string
