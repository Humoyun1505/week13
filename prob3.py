import random
import statistics
results = []
for _ in range(1000):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_sum = die1 + die2
    results.append(dice_sum)
mean_value = statistics.mean(results)
median_value = statistics.median(results)
mode_value = statistics.mode(results)
print("--- Simulation Results (1000 rolls) ---")
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Mode: {mode_value}")
