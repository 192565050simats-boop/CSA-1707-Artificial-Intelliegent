from sklearn.tree import DecisionTreeClassifier

# Input data
X = [[1, 1], [1, 0], [0, 1], [0, 0]]

# Output data
y = ["Yes", "Yes", "No", "No"]

# Create Decision Tree
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Give prediction input
result = model.predict([[1, 1]])

print("Prediction:", result[0])
