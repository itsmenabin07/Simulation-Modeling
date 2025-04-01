def mid_square_method(seed: int, count: int):
    """
    Implements the Mid-Square Method to generate pseudo-random numbers.
    
    Parameters:
    seed (int): The initial seed value (should be an n-digit number).
    count (int): Number of pseudo-random numbers to generate.
    
    Returns:
    list: A list of generated pseudo-random numbers.
    """
    n_digits = len(str(seed))  # Determine the number of digits in seed
    current_number = seed
    random_numbers = []

    for i in range(count):
        squared_number = current_number ** 2  # Square the number
        squared_str = str(squared_number).zfill(2 * n_digits)  # Ensure at least 2n digits with zero-padding
        mid_index = len(squared_str) // 2  # Find the middle index
        new_number = int(squared_str[mid_index - n_digits // 2 : mid_index + n_digits // 2])  # Extract middle n digits
        
        # Stop early if a zero is generated to avoid repetition
        if new_number == 0:
            print("Generated a zero! Stopping early to avoid repetition.")
            break
        
        random_numbers.append(new_number)
        current_number = new_number  # Update current number for next iteration

    return random_numbers


def main():
    """Main function to take user input and generate random numbers using the Mid-Square Method."""
    try:
        seed_value = int(input("Enter the seed value (n-digit number): "))
        count = int(input("Enter how many random numbers you want to generate: "))
        
        if count <= 0:
            print("Please enter a positive number for count.")
            return

        random_sequence = mid_square_method(seed_value, count)

        # Display results
        print("\nGenerated Random Numbers:")
        print(", ".join(f"x{i}={num}" for i, num in enumerate(random_sequence)))
    
    except ValueError:
        print("Invalid input! Please enter integer values only.")


if __name__ == "__main__":
    main()
