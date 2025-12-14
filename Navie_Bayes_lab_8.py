import math

# Example dataset
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
]

# Separate dataset by class
def separate_by_class(dataset):
    separated = {}
    for row in dataset:
        class_value = row[-1]
        if class_value not in separated:
            separated[class_value] = []
        separated[class_value].append(row[:-1])
    return separated

# Calculate mean and variance
def mean(numbers):
    return sum(numbers)/float(len(numbers))

def variance(numbers):
    m = mean(numbers)
    return sum([(x-m)**2 for x in numbers])/float(len(numbers))

# Gaussian probability
def calculate_probability(x, mean, var):
    if var == 0:
        return 1
    exponent = math.exp(-(x-mean)**2 / (2*var))
    return (1 / math.sqrt(2*math.pi*var)) * exponent

# Naive Bayes classifier (simplified for categorical as numeric encoding)
def predict(dataset, input_data):
    separated = separate_by_class(dataset)
    probabilities = {}
    
    for class_value, rows in separated.items():
        probabilities[class_value] = 1
        for i in range(len(input_data)):
            # categorical encoding: 1 if match else 0.5 (Laplace smoothing)
            probabilities[class_value] *= 1 if input_data[i]==rows[0][i] else 0.5
    
    best_class = max(probabilities, key=probabilities.get)
    return best_class

# Example prediction
test_instance = ['Sunny', 'Cool', 'High', 'Strong']
result = predict(data, test_instance)
print("Predicted class:", result)

