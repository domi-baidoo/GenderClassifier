# GenderClassifier
This project implements gender classification based on height, weight, and shoe size using various machine learning models from scikit-learn. The goal is to predict whether a person is Male or Female given their physical attributes.

## Features
- Accepts user input for height (cm), weight (kg), and shoe size (US)
- Uses a decision tree classifier to predict gender
- Displays the predicted gender in a simple web interface

## Technologies Used
- Python
- Streamlit
- Scikit-learn

## Installation
To run this project locally, follow these steps:

### Prerequisites
Ensure you have Python installed (Python 3.7 or later is recommended). You also need to install the required dependencies.

### Install Dependencies
```sh
pip install streamlit scikit-learn
```

### Run the Application
```sh
streamlit run main.py
```

## How It Works
1. The decision tree classifier is trained on a dataset containing height, weight, and shoe size as input features, and gender as the target variable.
2. The trained model takes user inputs and predicts gender.
3. The Streamlit interface allows users to input values and displays the predicted gender.

## Example Usage
1. Open the application.
2. Enter your height, weight, and shoe size.
3. Click the "Predict Gender" button.
4. View the predicted gender.

## Author
Dominion Baidoo



