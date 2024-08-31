import matplotlib.pyplot as plt

# Sample-per-class accuracy data for pneumonia_mvf
pneumonia_mvf = {'0': 0.817, '1': 0.827, '5': 0.825, '10': 0.825, '20': 0.824, '50': 0.816, '100': 0.809, '200': 0.8, '300': 0.793, '500': 0.776 , '700':0.787, '900':0.787}

# Sample-per-class accuracy data for pneumonia_random
pneumonia_random = {'0':0.817, '1': 0.821, '5': 0.822, '10': 0.821, '20': 0.822, '50': 0.822, '100': 0.824, '200': 0.817, '300': 0.822, '500': 0.822, '700': 0.819, '900': 0.83}

# Convert the keys (samples per class) to integers and sort them
samples_mvf = [str(k) for k in sorted([int(k) for k in pneumonia_mvf.keys()])]
accuracy_mvf = [pneumonia_mvf[k] * 100 for k in samples_mvf]  # Convert to percentage

samples_random = [str(k) for k in sorted([int(k) for k in pneumonia_random.keys()])]
accuracy_random = [pneumonia_random[k] * 100 for k in samples_random]  # Convert to percentage

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(samples_mvf, accuracy_mvf, marker='o', label='MVF', color='blue')
plt.plot(samples_random, accuracy_random, marker='o', label='Random', color='red')

# Adding title and labels
plt.title('Pneumonia Accuracy Comparison')
plt.xlabel('Removed features per Class')
plt.ylabel('Accuracy (%)')
plt.ylim(76, 90)  # Set y-axis limits to 75-100 for percentage
plt.xticks(samples_mvf)  # Ensure X-ticks are evenly spaced with categorical labels
plt.grid(True)

# Adding a legend
plt.legend()

# Show the plot
plt.show()