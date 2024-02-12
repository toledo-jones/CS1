from math import ceil


def simulate_infection(
        population: int,
        initial_infected: int,
        r_number: float) -> None:
    infected = initial_infected
    day = 1
    display_population(day, population)
    while population > 0:
        deceased = infected
        population -= deceased
        infected = ceil(infected * r_number)
        day += 1
        display_population(day, population)


def display_population(day, population):
    if population < 0:
        population = 0
    print(f"{day} {population}")


simulate_infection(1000000, 1000, 1.1)
# print("Expected value at 14 is 0")
