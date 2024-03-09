import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the dataset
data = pd.read_csv('C:\\Users\\khuy1\\Downloads\\opa_properties_public.csv')

# Data Cleaning and Preparation
# Dropping columns with high percentage of missing values
columns_to_drop = ['mailing_address_2', 'mailing_care_of', 'house_extension', 'owner_2']  
data_cleaned = data.drop(columns=columns_to_drop)

# Fill missing values
for col in data_cleaned.select_dtypes(include=['float64', 'int64']):
    data_cleaned[col].fillna(data_cleaned[col].median(), inplace=True)

for col in data_cleaned.select_dtypes(include=['object']):
    data_cleaned[col].fillna(data_cleaned[col].mode()[0], inplace=True)

# Feature Engineering: Interaction Term
data_cleaned['depth_frontage_interaction'] = data_cleaned['depth'] * data_cleaned['frontage']

# Selecting Features for Modeling
selected_features = ['market_value', 'depth', 'frontage', 'census_tract', 
                     'building_code_description', 'category_code_description', 'zip_code', 
                     'depth_frontage_interaction']
data_selected = data_cleaned[selected_features]

# One-hot Encoding for Categorical Variables
data_encoded = pd.get_dummies(data_selected, columns=['building_code_description', 
                                                      'category_code_description', 
                                                      'zip_code'], drop_first=True)

# Sampling the Data
sampled_data = data_encoded.sample(frac=0.1, random_state=42)

# Splitting the Data
X = sampled_data.drop('market_value', axis=1)
y = sampled_data['market_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Initialization and Training
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42)
}

# Model Training and Evaluation
model_performance = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    model_performance[name] = {'MAE': mae, 'RMSE': rmse}

# Printing Model Performance
for model, performance in model_performance.items():
    print(f"{model}: MAE = {performance['MAE']}, RMSE = {performance['RMSE']}")

