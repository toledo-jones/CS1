from math import ceil


def simulate_infection_pp(
        population: int,
        initial_infected: int,
        r_number: float) -> None:
    infected = initial_infected
    day = 1
    population_values_to_display = {day: population}
    while population > 0:
        deceased = infected
        population -= deceased
        infected = ceil(infected * r_number)
        day += 1
        population_values_to_display[day] = population
    display_population(population_values_to_display)


def make_field(content: any, length: int) -> str:
    content = str(content)
    if len(content) > length - 2:
        content = content[:length - 2]
    return f"|{content.rjust(length)} |"


def make_line(length: int) -> str:
    end = "+"
    middle = "-" * length
    return end + middle + end


def pretty_print_int(number: int) -> str:
    return f"{number:,}"

def display_population(population):
    print("+-----++------------+")
    print("| Day || Population |")
    print("+-----++------------+")
    for key in population.keys():
        if population[key] < 0:
            population[key] = 0
        print(f"{make_field(key, 4)}{make_field(pretty_print_int(population[key]), 11)}")
    print("+-----++------------+")


simulate_infection_pp(1000000, 1000, 1.1)
# print("Expected value at 14 is 0")

"""
Expected output: 


+-----++------------+
| Day || Population |
+-----++------------+
|   1 ||  1,000,000 |
|   2 ||    999,000 | 
|   3 ||    997,900 |
  ...
|  48 ||    123,944 |
|  49 ||     35,312 |
|  50 ||          0 |
+-----++------------+
"""
