import joblib
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
penguins = sns.load_dataset('penguins')

# Drop rows with missing values
penguins.dropna(inplace=True)

# Encode the target variable (species)
penguins['species'] = penguins['species'].map(
    {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
    )

# Select features and target
X = penguins[
    ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    ]
y = penguins['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Make predictions and evaluate the model
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(model, 'logistic_regression_model.joblib')
