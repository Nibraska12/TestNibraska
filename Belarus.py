import datetime


class Country:
    def __init__(
        self,
        name,
        capital,
        location,
        population,
    ):
        self.name = name
        self.location = location
        self.population = population
        self.capital = capital

    def info(self):
        return (
            "Name: "
            + self.name
            + "\nCapital: "
            + self.capital
            + "\nLocation: "
            + self.location
            + "\nPopulation: "
            + str(self.population)
        )


class Area(Country):
    def __init__(self, name, location, area):
        super().__init__(name, location)
        self.area = area

    @staticmethod
    def get_total_area(areas):
        total_area = 0
        for area in areas:
            total_area += area.area
        return total_area


class City(Country):
    def __init__(self, name, capital, location, population, established_date):
        super().__init__(name, capital, location, population)
        self.established_date = established_date

    @property
    def population_of_rb(self):
        return self.population

    @population_of_rb.setter
    def population_of_rb(self, value):
        if value < 0:
            raise ValueError("Population can't be negative")
        self.population = value

    @population_of_rb.deleter
    def population_of_rb(self):
        del self.population

    def __lt__(self, other):
        return self.population < other.population

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.established_date.year
        return age


belarus = Country("Belarus", "Minsk", ("50°00 28°00"), (9300000))
poland = Country('Poland', 'Warsaw', ("34°00 56°00"), (37700000))

gomel_area = Area('Gomelskay', ('78°23′14'), (40400))
# vitebsk_area = Area('Vitebskay', ('23°14′56'), (42200))
# brestskay_area = Area('Brestskay', ('42°66′88'), (38200))
# mogilevskay_area = Area('Mogilevskay', ('53°55′00'), (28599))
# grodnenskay_area = Area('Grodnenskay', ('453.54567°'), (25300))
# minskay_area = Area('Minskay', ('27.5667°'), (40300))

# print(gomel_area.area)

mogilev = City("Mogilev", "n", ("53°55′00"), (405000), datetime.date(1922, 6, 22))
minsk = City("Minsk", "y", ("27.5667°"), (1950000), datetime.date(1067, 2, 14))
grodno = City("Grodno", "n", ("453.54567°"), (368710), datetime.date(1128, 5, 16))
gomel = City("Gomel", "n", ("78°23′14"), (508839), datetime.date(1142, 3, 17))
vitebsk = City("Vitebsk", "n", ("23°14′56"), (362466), datetime.date(1233, 5, 21))
brest = City("Brest", "n", ("42°66′88"), (343985), datetime.date(1415, 6, 12))

print(belarus.info())

# areas = [mogilevskay_area, grodnenskay_area, minskay_area, brestskay_area, vitebsk_area, gomel_area]
# total_area = Area.get_total_area(areas)
# print(f"total area of Belarus: {total_area}")

mogilev.population += 788
print("Population of Mogilev is: ", mogilev.population)



# del mogilev.population # удаление всей популяции

print(f"Age of city: {grodno.get_age()} ")  # узнать возраст города

print("1 has a larger population than city2" if grodno > minsk else "2 has a larger population than 1")# Сравнить два города по популяции
