import numpy as np
import matplotlib.pyplot as plt
 
class MarkovChain:
    def __init__(self, transition_matrix, states):
        self.transition_matrix = np.array(transition_matrix)
        self.states = states
        self.n_states = len(states)

    def next_state(self, current_state):
        return np.random.choice(
            self.states,
            p=self.transition_matrix[self.states.index(current_state)]
        )

    def generate_states(self, current_state, n_steps):
        states = [current_state]
        for _ in range(n_steps):
            next_state = self.next_state(current_state)
            states.append(next_state)
            current_state = next_state
        return states

# Modified transition matrix with increased Sunny -> Cloudy probability
weather_transition_matrix = [
    [0.5, 0.3, 0.2],  # Sunny
    [0.2, 0.6, 0.2],  # Rainy
    [0.4, 0.2, 0.4]   # Cloudy
]
weather_states = ["Sunny", "Stormy", "Rainy"]

# Create a Markov Chain instance
weather_chain = MarkovChain(weather_transition_matrix, weather_states)

# Take user input for starting state and number of predictions
start_state = input("Enter the starting state (Sunny/Stormy/Rainy): ")
num_days = int(input("Enter the number of days to predict: "))
num_days = max(num_days, 20)  # Ensure at least 100 days for steady-state analysis

# Generate weather sequence
weather_sequence = weather_chain.generate_states(start_state, num_days)

# Count occurrences of each state
state_counts = {state: weather_sequence.count(state) for state in weather_states}

# Display results
print("\n Predicted Weather Sequence:")
print(" --> ".join(weather_sequence))
print("\nState Occurrences in Simulation:")
for state, count in state_counts.items():
    print(f"{state}: {count} times")

# Compute steady-state distribution
steady_state = {state: count / num_days for state, count in state_counts.items()}
print("\nSteady-State Distribution:")
for state, probability in steady_state.items():
    print(f"{state}: {probability:.4f}")

# Visualization
plt.figure(figsize=(12, 5))

# Bar Chart: State Occurrences
plt.subplot(1, 2, 1)
plt.bar(state_counts.keys(), state_counts.values(), color=['Red', 'Green', 'Purple'])
plt.xlabel("Weather State")
plt.ylabel("Occurrences")
plt.title("Weather State Frequency in Simulation [Nabin Joshi]")

# Line Graph: Weather Transitions Over Time
plt.subplot(1, 2, 2)
time_steps = list(range(len(weather_sequence)))
state_indices = [weather_states.index(state) for state in weather_sequence]
plt.plot(time_steps, state_indices, marker='o', linestyle='-', color='black')
plt.yticks(range(len(weather_states)), weather_states)
plt.xlabel("Time Steps (Days)")
plt.ylabel("Weather State")
plt.title("Weather Transitions Over Time [Nabin Joshi]")

plt.tight_layout()
plt.show()