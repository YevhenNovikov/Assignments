class Country:

    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        two_countries_name = self.name + ' ' + other_country.name
        together_population = self.population + other_country.population
        return Country(two_countries_name, together_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
