import math
from collections import Counter

# Constants
DATA_SIZE = 20
K = 3

# Dataset
dataset = [
    {"age": 18, "income": 10000, "jeans_type": "Skinny"},
    {"age": 21, "income": 15000, "jeans_type": "Skinny"},
    {"age": 25, "income": 20000, "jeans_type": "Regular"},
    {"age": 28, "income": 22000, "jeans_type": "Regular"},
    {"age": 30, "income": 25000, "jeans_type": "Bootcut"},
    {"age": 35, "income": 27000, "jeans_type": "Bootcut"},
    {"age": 40, "income": 30000, "jeans_type": "Relaxed"},
    {"age": 45, "income": 35000, "jeans_type": "Relaxed"},
    {"age": 50, "income": 40000, "jeans_type": "Loose"},
    {"age": 55, "income": 45000, "jeans_type": "Loose"},
    {"age": 22, "income": 12000, "jeans_type": "Skinny"},
    {"age": 24, "income": 18000, "jeans_type": "Regular"},
    {"age": 32, "income": 24000, "jeans_type": "Bootcut"},
    {"age": 38, "income": 28000, "jeans_type": "Relaxed"},
    {"age": 42, "income": 33000, "jeans_type": "Relaxed"},
    {"age": 48, "income": 37000, "jeans_type": "Loose"},
    {"age": 27, "income": 21000, "jeans_type": "Regular"},
    {"age": 36, "income": 26000, "jeans_type": "Bootcut"},
    {"age": 44, "income": 34000, "jeans_type": "Relaxed"},
    {"age": 52, "income": 42000, "jeans_type": "Loose"}
]

# Compute Euclidean distance
def compute_distance(age1, income1, age2, income2):
    return math.sqrt((age1 - age2) ** 2 + (income1 - income2) ** 2)

# Predict jeans type using KNN
def predict_jeans_type(input_age, input_income):
    neighbors = []

    for person in dataset:
        distance = compute_distance(input_age, input_income, person["age"], person["income"])
        neighbors.append({"distance": distance, "jeans_type": person["jeans_type"]})

    # Sort by distance
    neighbors.sort(key=lambda x: x["distance"])

    # Take top K neighbors and count types
    top_k = neighbors[:K]
    types = [neighbor["jeans_type"] for neighbor in top_k]
    most_common = Counter(types).most_common(1)[0][0]

    return most_common

# Main program
def main():
    input_age = int(input("Enter age: "))
    input_income = int(input("Enter monthly income (NPR): "))

    predicted = predict_jeans_type(input_age, input_income)
    print(f"\nPredicted jeans type: {predicted}")

if __name__ == "__main__":
    main()
