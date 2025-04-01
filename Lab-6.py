#LAB-6: Implementing Linear Congruential Method of Random Number Generation
def lcg_random_numbers(seed: int, multiplier: int, increment: int, modulus: int, count: int):
    """Generates pseudo-random numbers using the Linear Congruential Method."""
    random_numbers = []
    current_value = seed

    for i in range(count):
        current_value = (multiplier * current_value + increment) % modulus
        random_numbers.append(current_value)
        # print(f"x{i} = {current_value}")

    return random_numbers

# User input
seed_value = int(input("Enter the seed value: "))
multiplier = int(input("Enter the multiplier: "))
increment = int(input("Enter the increment: "))
modulus = int(input("Enter the modulus: "))
num_count = int(input("How many random numbers to generate? "))

# Generate numbers
random_sequence = lcg_random_numbers(seed_value, multiplier, increment, modulus, num_count)

# Display results
print("\nGenerated Random Numbers [Nabin Joshi]:")
print(", ".join(f"x{i}={num}" for i, num in enumerate(random_sequence)))