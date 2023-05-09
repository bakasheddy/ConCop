import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import pickle

df = pd.read_csv('Bank Customer Churn Prediction Dataset.csv')

nav = st.sidebar.radio("Navigations", ['Home', 'Predictions'])

if nav == "Home":
    st.write(
        """
    # ConCop
    """)

    st.image('./images/Payment-Fraud-Detection_Overgraph.JPG')

    st.write("""### About dataset

this dataset was gotten from kaggle, it contains 6,362,620 data points with 11 columns. it captures transactions that has occured both legit and fraud The below column reference:

- step: represents a unit of time where 1 step equals 1 hour
- type: type of online transaction
- amount: the amount of the transaction
- nameOrig: customer starting the transaction
- oldbalanceOrg: balance before the transaction
- newbalanceOrig: balance after the transaction
- nameDest: recipient of the transaction
- oldbalanceDest: initial balance of recipient before the transaction
- newbalanceDest: the new balance of recipient after the transaction
- isFraud: fraud transaction
    """
             )
    st.dataframe(df)

elif nav == 'Predictions':
    st.image('./images/Payment-Fraud-Detection_Overgraph.JPG')
    st.sidebar.subheader('set parameters for predictions')

    def user_input_features():

        credit_score = st.sidebar.number_input(
            'credit_score', min_value=df['credit_score'].min(), max_value=df['credit_score'].max())
        gender = st.sidebar.selectbox('Gender', ['male', 'female'], index=1)
        gender = 1 if gender.lower() == 'male' else 0

        age = st.sidebar.slider('set age', value=16)
        tenure = st.sidebar.slider('tenure', max_value=10, value=1)
        balance = st.sidebar.number_input(
            'balance', max_value=df['balance'].max())
        products_number = st.sidebar.number_input(
            'products_number', min_value=df['products_number'].min(), max_value=df['products_number'].max())

        credit_card = st.sidebar.selectbox(
            'has credit card?', ['yes', 'no'], index=1)
        credit_card = 1 if credit_card.lower() == 'yes' else 0  # encoding

        active_member = st.sidebar.selectbox(
            'Active member?', ['yes', 'no'], index=1)
        active_member = 1 if active_member.lower() == 'yes' else 0  # encoding

        estimated_salary = st.sidebar.number_input(
            'estimated_salary', min_value=df['estimated_salary'].min(), max_value=df['estimated_salary'].max())

        data = {
            'credit_score': credit_score,
            'gender': gender,
            'age': age,
            'tenure': tenure,
            'balance': balance,
            'products_number': products_number,
            'credit_card': credit_card,
            'active_member': active_member,
            'estimated_salary': estimated_salary
        }
        feautres = pd.DataFrame(data, index=[0])
        return feautres
    dff = user_input_features()
    st.header('Specified Parameters')
    st.write(dff)
    st.write('---')
    file_name = 'RetainMe_Model.pkl'
    loaded_model = pickle.load(open(file_name, 'rb'))
    predictions = loaded_model.predict(dff)

    st.write('Churn probability')
    prob = loaded_model.predict_proba(dff)
    st.write(prob)

    st.write('Will this person churn?')
    st.write(predictions)
    st.write('---')

    # plot graph of feature importances for better visualization
    feat_importances = pd.Series(
        loaded_model.feature_importances_, index=dff.columns)
    feat_importances.nlargest(10).plot(kind='barh')
    plt.title('Most important features for prediction')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.style.use('ggplot')
    plt.grid(visible=False)
    st.pyplot()
