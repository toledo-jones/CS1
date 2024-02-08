from math import ceil

def simulate_infection(
        population: int,
        initial_infected: int,
        r_number: float) -> None:
    infected = initial_infected
    day = 0
    deceased = 0
    while population > 0:
        print("Increasing Day")
        day += 1
        
        print(f"Decreasing {population} by {deceased}")
        population -= deceased
        print(f"Population is now: {population}")
        
        print(f"Setting deceased to {infected}")
        deceased = infected
        
        print(f"Multiply infected by {r_number}")
        infected *= r_number
        
        print(f"Now there are {infected} infected")
        infected = ceil(infected)

        print(f"Adjust infected value to closest integer {infected}")
        print(f"{day} {population}")


simulate_infection(125672, 20, 2.054376744899002)

# Expected value at 14 is 0. 
