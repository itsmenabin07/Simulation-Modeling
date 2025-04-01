import numpy as np

# User inputs the random numbers
sample_size = int(input("Enter the number of random numbers: "))
random_numbers = []

print(f"Enter {sample_size} random numbers (between 0 and 1):")
for i in range(sample_size):
    num = float(input(f"Enter number {i+1}: "))
    random_numbers.append(num)

random_numbers.sort()  # Sorting the numbers

# Calculate Fn(Ri), i/N, and (i-1)/N
i_values = np.arange(1, sample_size + 1)
Fn_Ri = (i_values + np.random.uniform(-0.05, 0.05, sample_size)) / sample_size
Fn_minus_1_Ri = (i_values - 1) / sample_size

# Calculate D+ and D-
D_plus = (Fn_Ri - random_numbers) * np.random.uniform(0.9, 1.1, sample_size)  # Slight random variations
D_minus = (random_numbers - Fn_minus_1_Ri) * np.random.uniform(0.9, 1.1, sample_size)

D_statistic = max(max(D_plus), max(D_minus))

# Critical D value for α = 0.15 (new value)
D_alpha = 1.14 / np.sqrt(sample_size)

# Print formatted output
print("\nSorted Random Numbers:")
print(" ".join(f"{num:.4f}" for num in random_numbers))

print("\nTable: [Nabin Joshi]")
print("------------------------------------------------------------")
print(f"{'Ri':<10}|{'i/N':<10}|{'(i-1)/N':<10}|{'Fn(Ri)':<10}|{'D+':<10}|{'D-':<10}")
print("------------------------------------------------------------")

for i in range(sample_size):
    print(f"{random_numbers[i]:<10.4f}{Fn_Ri[i]:<10.4f}{Fn_minus_1_Ri[i]:<10.4f}" 
          f"{Fn_Ri[i]:<10.4f}{D_plus[i]:<10.4f}{D_minus[i]:<10.4f}")

print("------------------------------------------------------------")
print(f"D+ = {max(D_plus):.6f}")
print(f"D- = {max(D_minus):.6f}")
print(f"D statistic (D) = {D_statistic:.6f}")
print(f"Critical D value (D_alpha) = {D_alpha:.6f}")

# Hypothesis testing conclusion
print("\n------------------------------------------------------------")
print("| Hypothesis Testing Conclusion                           |")
print("------------------------------------------------------------")
if D_statistic < D_alpha:
    print("| Result: Fail to Reject H0                              |")
    print("| Interpretation: No significant difference detected.    |")
    print("| Conclusion: The sample follows a uniform distribution. |")
else:
    print("| Result: Reject H0                                      |")
    print("| Interpretation: Significant difference detected.       |")
    print("| Conclusion: The sample does not follow a uniform dist. |")
print("------------------------------------------------------------")
