import matplotlib.pyplot as plt

# Sample-per-class accuracy data for STL-10
stl10_accuracy = {'1': 1, '2': 0.995, '3': 0.995, '4': 0.994, '5': 0.995, '6': 0.995, '7': 0.995, '8': 0.995, '9': 0.995, '10': 0.994}



# Sample-per-class accuracy data for CIFAR-10 (replace with actual data)
cifar10_accuracy = {'1': 1.0, '2': 0.9993, '3': 0.995, '4': 0.9911, '5': 0.9877, '6': 0.9815, '7': 0.9808, '8': 0.981, '9': 0.9796, '10': 0.9786}

# Convert the keys (samples per class) to integers and sort them
samples_stl10 = sorted([int(k) for k in stl10_accuracy.keys()])
accuracy_stl10 = [stl10_accuracy[str(k)] * 100 for k in samples_stl10]  # Convert to percentage

samples_cifar10 = sorted([int(k) for k in cifar10_accuracy.keys()])
accuracy_cifar10 = [cifar10_accuracy[str(k)] * 100 for k in samples_cifar10]  # Convert to percentage

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(samples_stl10, accuracy_stl10, marker='o', label='STL-10', color='blue')
plt.plot(samples_cifar10, accuracy_cifar10, marker='o', label='CIFAR-10', color='red')

# Adding title and labels
plt.title('Sample-per-Class Accuracy Comparison')
plt.xlabel('Number of Samples per Class')
plt.ylabel('Accuracy (%)')
plt.xscale('log')  # Use a logarithmic scale for the x-axis
plt.ylim(97.5, 100)  # Set y-axis limits to 0-100 for percentage
plt.xticks(samples_stl10, samples_stl10)  # Ensure X-ticks are the sample numbers
plt.grid(True)

# Adding a legend
plt.legend()

# Show the plot
plt.show()