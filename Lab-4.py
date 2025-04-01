import numpy as np
import matplotlib.pyplot as plt

num_rolls = int(input("Enter the number of dice rolls: "))

fair_rolls = np.random.randint(1, 7, num_rolls)

# Updated biased probabilities
biased_probs = [0.05, 0.10, 0.30, 0.20, 0.25, 0.10]
biased_rolls = np.random.choice([1, 2, 3, 4, 5, 6], num_rolls, p=biased_probs)

fair_observed_probs = np.bincount(fair_rolls, minlength=7)[1:] / num_rolls
biased_observed_probs = np.bincount(biased_rolls, minlength=7)[1:] / num_rolls

faces = np.arange(1, 7)
fair_expected_prob = [1/6] * 6

print("\nFAIR DICE:")
for i, p in zip(faces, fair_observed_probs):
    print(f"{i}: Expected={1/6:.4f}, Observed={p:.4f}")

print("\nBIASED DICE:")
for i, p, e in zip(faces, biased_observed_probs, biased_probs):
    print(f"{i}: Expected={e:.4f}, Observed={p:.4f}")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(faces, fair_observed_probs, alpha=0.8, label='Observed')
plt.bar(faces, fair_expected_prob, alpha=0.4, label='Expected')
plt.title("Fair Dice Rolls - Nabin")
plt.xlabel("Dice-Face")
plt.ylabel("Probability")
plt.legend()

plt.subplot(1, 2, 2)
plt.bar(faces, biased_observed_probs, alpha=0.8, label='Observed')
plt.bar(faces, biased_probs, alpha=0.4, label='Expected')
plt.title("Biased Dice Rolls - Joshi")
plt.xlabel("Dice-Face")
plt.ylabel("Probability")
plt.legend()

plt.tight_layout()
plt.show()
