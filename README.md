# CMPSC445-PROJECT1
Project1: Individual project

This is the data set I'm using: https://www.phila.gov/property/data/
This data set contains 500k+ entries and I tried to edit/remove it to 10k+ entries.

Cleaning process:
Dropping Columns with High Percentage of Missing Values: columns_to_drop: This is a list of column names that are identified as having a high percentage of missing values or being less relevant to the analysis.
The data.drop() function is used to remove these columns from the dataset. Removing columns with too many missing values helps simplify the dataset and focus on more reliable data.
Handling Missing Values: For numerical columns, missing values are filled with the median of each column. The median is often used because it is less sensitive to outliers compared to the mean. For categorical columns, missing values are filled with the mode (the most frequent value) of each column. This is a common practice for categorical data as it's a robust measure of central tendency. The fillna() function is used for this imputation, with inplace=True to modify the DataFrame in place.
The goal of this data cleaning process is to create a dataset that is free from missing values and irrelevant features

Insights from Data Analysis:
The creation of interaction terms, such as multiplying 'depth' and 'frontage', can unveil hidden relationships in the data that single features may not reveal. This suggests that the dimensions and shape of a property might jointly influence its market value. The dataset demonstrated a complex mix of numerical and categorical data, underlining the multifaceted nature of real estate valuation.
Data Quality and Completeness: The initial steps highlighted the importance of handling missing data. The strategies used for imputation had a significant impact on the subsequent model's performance.

Challenges in Model Development:
Handling a large dataset with many entries and columns was difficult for me, especially after one-hot encoding, and was computationally challenging, leading to memory issues. For feature engineering complexity, I've decided which features to create or modify, which involves a balance between adding informative complexity and maintaining computational efficiency and I Found out that Interaction Term is a pretty solid one.

Recommendations for Improvement:
I think in the future, I should exploring more sophisticated methods of feature engineering like polynomial features or feature interactions based on domain knowledge so it could make better results.

Reflection on Approach Strengths and Limitations:
Strengths:
The first strength of my approach is flexibility in data handling, the approach was adaptable to different types of data, demonstrating flexibility in handling numerical and categorical variables.
Diverse Model Evaluation: The use of various models provided a broad perspective on how different algorithms perform on the same dataset.
Limitations:
I think my biggest weakness is potential overfitting. With high-dimensional data, especially with many one-hot encoded features, raises the risk of overfitting.

Future Research Directions:
Deep Learning Models: Experiment with deep learning architectures, which might capture complex patterns in large datasets more effectively.
Geographical Data Analysis: Integrating geospatial data could offer a richer context, as location is a critical factor in real estate.
Econometric Modeling: Incorporating economic models might reveal broader market trends influencing property values.

RESULTS OF THE MODEL:
Linear Regression: MAE = 87211.5560385793, RMSE = 167712.13509649795
Decision Tree: MAE = 102373.54085603113, RMSE = 273917.82429418754
Random Forest: MAE = 70934.39180717683, RMSE = 143597.98503693144
Gradient Boosting: MAE = 87030.4989279761, RMSE = 153491.34113737344

So based on metrics (MAE and RMSE), the Random Forest model is the best performer among the ones evaluated. Here's why:
Lowest Mean Absolute Error (MAE): The Random Forest model has the lowest MAE of 70,934.39. This means, on average, its predictions are closer to the actual values compared to the other models. A lower MAE is desirable as it indicates better predictive accuracy.
Lowest Root Mean Squared Error (RMSE): With an RMSE of 143,597.98, the Random Forest model also has the lowest RMSE, which suggests it is better at dealing with larger errors in the predictions. Lower RMSE values are preferred as they indicate the model is making fewer large errors in prediction.
