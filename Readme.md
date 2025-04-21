# Regression

A comprehensive implementation of various regression techniques using Python, including Simple Linear Regression, Multiple Linear Regression, Polynomial Regression, and advanced techniques like Ridge and Lasso Regression, as well as Logistic Regression for classification tasks. The project also includes a web application for deploying the models.

## Overview

This project demonstrates different regression and classification analysis techniques:
- Linear Regression Techniques:
  - Simple Linear Regression (Height-Weight Analysis)
  - Multiple Linear Regression (Economic Index Analysis)
  - Polynomial Regression (Non-linear Data Modeling)
  - Ridge and Lasso Regression (Regularization Techniques with Forest Fires Analysis)
  - Model Training and Optimization (Forest Fire Prediction)
- Logistic Regression Classification:
  - Binary Classification
  - Multiclass Classification
  - Handling Imbalanced Datasets
  - ROC-AUC Evaluation
- Web Application for Model Deployment


## Installation

1. Clone the repository:
```bash
git clone https://github.com/Abhinavexists/Regression.git
cd Regression
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Dependencies

- numpy (>= 1.21.0)
- pandas (>= 1.3.0)
- matplotlib (>= 3.4.0)
- seaborn (>= 0.11.0)
- scikit-learn (>= 1.0.0)
- jupyter (>= 1.0.0)
- ipykernel (>= 6.0.0)
- statsmodels (>= 0.13.0)
- flask (for web application)
- pickle (for model serialization)

## Usage

### Simple Linear Regression
- Analyzes the relationship between height and weight
- Features standardization and model evaluation
- Includes R-squared and adjusted R-squared calculations

### Multiple Linear Regression
- Analyzes economic indices including interest rates and unemployment rates
- Implements feature scaling and cross-validation
- Includes comprehensive model evaluation metrics

### Polynomial Regression
- Demonstrates handling of non-linear relationships
- Implements polynomial feature transformation
- Includes model comparison with different polynomial degrees

### Ridge and Lasso Regression
- Implements L1 and L2 regularization techniques
- Handles multicollinearity in features
- Demonstrates parameter tuning using cross-validation
- Compares performance between Ridge and Lasso models
- Uses Algerian Forest Fires dataset for real-world application

### Model Training
- Advanced model training techniques
- Hyperparameter optimization
- Model validation and testing
- Performance comparison across different regression techniques
- Forest fire prediction using weather and environmental factors
- Data preprocessing and feature engineering for real-world data

### Logistic Regression
- Binary classification implementation
- Multiclass classification techniques
- Strategies for handling imbalanced datasets
- ROC curve analysis and AUC score evaluation
- Threshold optimization
- Probability calibration

### Web Application
- Flask-based web interface for model predictions
- User-friendly input form for forest fire prediction
- Deployment-ready configuration for AWS Elastic Beanstalk
- Saved models for quick inference

## Running the Web Application

1. Make sure all dependencies are installed:
```bash
pip install flask
```

2. Run the application locally:
```bash
python application.py
```

3. Access the application in your browser at `http://localhost:8080`

## Deployment

The project includes configuration for deployment to AWS Elastic Beanstalk:

1. Install the EB CLI:
```bash
pip install awsebcli
```

2. Initialize your EB application:
```bash
eb init -p python-3.8 regression-app
```

3. Create an environment and deploy:
```bash
eb create regression-env
```

4. Open the deployed application:
```bash
eb open
```

## Model Evaluation Metrics

All implementations include various evaluation metrics:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared Score
- Adjusted R-squared Score
- Cross-validation Scores

## Results Visualization

Each notebook includes detailed visualizations:
- Scatter plots
- Correlation matrices
- Regression lines and decision boundaries
- Residual plots
- Pair plots
- Regularization path plots
- Learning curves
- ROC curves and confusion matrices

## Datasets

The project uses several datasets:
- Height_Weight.csv: Basic dataset for simple linear regression
- Economic_Index.csv: Economic indicators for multiple linear regression
- Algerian_forest_fires_dataset_UPDATE.csv: Original forest fires dataset
- Algerian_forest_fires_cleaned_dataset.csv: Preprocessed forest fires dataset for advanced regression techniques

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.