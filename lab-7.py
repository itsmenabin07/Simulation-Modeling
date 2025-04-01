def multiplicative_congruential_method(seed: int, multiplier: int, modulus: int, count: int):
    """Generates pseudo-random numbers using the Multiplicative Congruential Method."""
    random_numbers = []
    current_value = seed

    for i in range(count):
        current_value = (multiplier * current_value) % modulus
        random_numbers.append(current_value)
        print(f"x{i} = {current_value}")
    
    return random_numbers


def get_positive_int(prompt):
    """Helper function to get a positive integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Please enter a positive integer.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


# User input with validation
seed_value = get_positive_int("Enter the seed value: ")
multiplier = get_positive_int("Enter the multiplier: ")
modulus = get_positive_int("Enter the modulus: ")
num_count = get_positive_int("How many random numbers to generate? ")

# Generate random numbers
print("\nGenerated Random Numbers:")
multiplicative_congruential_method(seed_value, multiplier, modulus, num_count)
