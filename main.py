import streamlit as st
from sklearn import tree

#Training Data
X = [
    [160, 71, 10.3], [163, 48, 6.6], [154, 81, 11.7], [156, 90, 8.3], [198, 100, 9.1],
    [182, 47, 9.5], [150, 99, 9.9], [162, 57, 10.3], [198, 77, 6.2], [169, 86, 10.1],
    [164, 74, 9.0], [183, 52, 8.5], [155, 52, 10.3], [161, 60, 7.2], [180, 78, 8.9],
    [170, 100, 11.7], [158, 94, 10.2], [155, 75, 12.4], [157, 71, 12.1], [186, 91, 6.2],
    [193, 80, 11.5], [199, 83, 12.0], [180, 76, 11.0], [188, 73, 10.3], [183, 49, 8.9],
    [154, 61, 7.0], [196, 72, 11.2], [188, 55, 12.8], [164, 83, 9.1], [154, 47, 9.3],
    [195, 48, 6.9], [173, 57, 12.7], [188, 92, 10.1], [159, 68, 10.5], [157, 74, 6.0],
    [150, 72, 8.6], [171, 48, 12.8], [189, 68, 7.0], [172, 52, 11.2], [155, 97, 9.8],
    [186, 56, 8.5], [152, 82, 12.8], [193, 74, 8.6], [192, 46, 6.3], [200, 71, 7.6],
    [174, 98, 7.5], [164, 82, 6.1], [151, 88, 7.8], [168, 100, 6.3], [162, 46, 6.7]
]

Y = [
    "Male", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Female",
    "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female",
    "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Female", "Female", "Male",
    "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Female", "Female",
    "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Female", "Male"
]

#Train the decision tree model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)


# Streamlit UI
st.title("Gender Classifier")

st.write("Enter your details below to predict your gender.")

# User Inputs
height = st.number_input("Height (cm)", min_value=120, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
shoe_size = st.number_input("Shoe Size (US)", min_value=4.0, max_value=15.0, value=9.0)

if st.button("Predict Gender"):
    user_data = [[height, weight, shoe_size]]
    prediction = clf.predict(user_data)
    st.success(f"Predicted Gender: **{prediction[0]}**")
