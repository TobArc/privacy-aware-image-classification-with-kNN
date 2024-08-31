import matplotlib.pyplot as plt

# Sample-per-class accuracy data for melanoma_mvf
melanoma_mvf = {'1': 0.693, '5': 0.692, '10': 0.689, '20': 0.686, '30': 0.682, '40': 0.675, '50': 0.671, '60': 0.669, '70': 0.667, '80': 0.667, '90': 0.669, '100': 0.663}

# Sample-per-class accuracy data for melanoma_random
melanoma_random = {'1': 0.701, '5': 0.701, '10': 0.702, '20': 0.701, '30': 0.702, '40': 0.702, '50': 0.702, '60': 0.702, '70': 0.695, '80': 0.7, '90': 0.703, '100': 0.702}

# Convert the keys (samples per class) to integers and sort them
samples_mvf = [str(k) for k in sorted([int(k) for k in melanoma_mvf.keys()])]
accuracy_mvf = [melanoma_mvf[k] * 100 for k in samples_mvf]  # Convert to percentage

samples_random = [str(k) for k in sorted([int(k) for k in melanoma_random.keys()])]
accuracy_random = [melanoma_random[k] * 100 for k in samples_random]  # Convert to percentage

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(samples_mvf, accuracy_mvf, marker='o', label='MVF', color='blue')
plt.plot(samples_random, accuracy_random, marker='o', label='Random', color='red')

# Adding title and labels
plt.title('melanoma Accuracy Comparison')
plt.xlabel('Removed features per Class')
plt.ylabel('Accuracy (%)')
plt.ylim(66, 71)  # Set y-axis limits to 75-100 for percentage
plt.xticks(samples_mvf)  # Ensure X-ticks are evenly spaced with categorical labels
plt.grid(True)

# Adding a legend
plt.legend()

# Show the plot
plt.show()