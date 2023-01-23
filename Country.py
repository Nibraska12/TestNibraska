import datetime

# from abc import ABC, abstractmethod


def add_get_total_area(cls):
    class NewClass(cls):
        def get_total_area(self, areas):
            total_area = 0
            for area in areas:
                total_area += area.area
            return total_area

    return NewClass


class Country:
    def __init__(
        self,
        name,
        capital,
        location,
        population,
        established_date,
    ):
        self.name = name
        self.location = location
        self.population = population
        self.capital = capital
        self.established_date = established_date


class Belarus(Country):
    def info(self):
        return (
            "Name: "
            + self.name
            + "\nCapital: "
            + self.capital
            + "\nLocation: "
            + self.location
            + "\nEstablished_date: "
            + str(self.established_date)
            + "\nPopulation: "
            + str(self.population)
        )


class CityBelarus(Belarus):
    def __init__(self, name, capital, location, population, established_date):
        super().__init__(name, capital, location, population, established_date)

    @property
    def population_of_city(self):
        return self.population

    @population_of_city.setter
    def population_of_city(self, value):
        if value < 0:
            raise ValueError("Population can't be negative")
        self.population = value

    @population_of_city.deleter
    def population_of_city(self):
        del self.population

    def __lt__(self, other):
        return self.population < other.population

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.established_date.year
        return age


class AreaBelarus(Belarus):
    def __init__(self, coordinates, number_of_cities, area):
        self.coordinates = coordinates
        self.number_of_cities = number_of_cities
        self.area = area
        self.total_area_belarus = 0


@add_get_total_area
class Belarus:
    pass


class Poland(Country):
    def info(self):
        return (
            "Name: "
            + self.name
            + "\nCapital: "
            + self.capital
            + "\nLocation: "
            + self.location
            + "\nEstablished_date: "
            + str(self.established_date)
            + "\nPopulation: "
            + str(self.population)
        )


class CityPoland(Poland):
    def __init__(self, name, capital, location, population, established_date):
        super().__init__(name, capital, location, population, established_date)

    @property
    def population_of_city(self):
        return self.population

    @population_of_city.setter
    def population_of_city(self, value):
        if value < 0:
            raise ValueError("Population can't be negative")
        self.population = value

    @population_of_city.deleter
    def population_of_city(self):
        del self.population

    def __lt__(self, other):
        return self.population < other.population

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.established_date.year
        return age


class AreaPoland(Poland):
    def __init__(self, coordinates, number_of_cities, area):
        self.coordinates = coordinates
        self.number_of_cities = number_of_cities
        self.area = area

@add_get_total_area
class Poland:
    pass


belarus = Belarus("Belarus", "Minsk", ("50°00 28°00"), (9300000), (1991, 11, 12))
poland = Poland("Poland", "Warsaw", ("34°00 56°00"), (37700000), (1569, 4, 21))

# print(belarus.info())
print(poland.info())

gomel_area = AreaBelarus(
    "Gomelskay",
    ("78°23′14"),
    (40400),
)
vitebsk_area = AreaBelarus("Vitebskay", ("23°14′56"), (42200))
brestskay_area = AreaBelarus("Brestskay", ("42°66′88"), (38200))
mogilevskay_area = AreaBelarus("Mogilevskay", ("53°55′00"), (28599))
grodnenskay_area = AreaBelarus("Grodnenskay", ("453.54567°"), (25300))
minskay_area = AreaBelarus("Minskay", ("27.5667°"), (40300))

print(gomel_area.number_of_cities)

mogilev = CityBelarus(
    "Mogilev", "n", ("53°55′00"), (405000), datetime.date(1922, 6, 22)
)
minsk = CityBelarus("Minsk", "y", ("27.5667°"), (1950000), datetime.date(1067, 2, 14))
grodno = CityBelarus(
    "Grodno", "n", ("453.54567°"), (368710), datetime.date(1128, 5, 16)
)
gomel = CityBelarus("Gomel", "n", ("78°23′14"), (508839), datetime.date(1142, 3, 17))
vitebsk = CityBelarus(
    "Vitebsk", "n", ("23°14′56"), (362466), datetime.date(1233, 5, 21)
)
brest = CityBelarus("Brest", "n", ("42°66′88"), (343985), datetime.date(1415, 6, 12))

# print(poland.info())

areas_local = [
    mogilevskay_area,
    grodnenskay_area,
    minskay_area,
    brestskay_area,
    vitebsk_area,
    gomel_area,
]

total_area_belarus = Belarus.get_total_area(areas_belarus)
total_area_poland = Poland.get_total_area(areas_poland)
print("Total area of Belarus: ", total_area_belarus)
print("Total area of Poland: ", total_area_poland)


# mogilev.population += 788
# print("Population of Mogilev is: ", mogilev.population)


# del mogilev.population # удаление всей популяции

print(f"Age of city: {grodno.get_age()} ")  # узнать возраст города

print(
    "1 has a larger population than city2"
    if grodno > minsk
    else "2 has a larger population than 1"
)  # Сравнить два города по популяции
