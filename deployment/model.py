# Import Essential Library
import streamlit as st
import pandas as pd
import pickle

# Load Model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

list_cat_cols = ['education_level', 'pay_sep05', 'pay_aug05', 'pay_jul05', 'pay_jun05', 'pay_may05', 'pay_apr05']
list_num_cols = ['limit_balance', 'pay_amt_sep05', 'pay_amt_aug05', 'pay_amt_jul05', 'pay_amt_jun05', 'pay_amt_may05', 'pay_amt_apr05']

# Function to run model predictor
def run():
    # Set Title
    st.title('Credit Card Default Prediction Model')

    # Sub Title
    st.subheader('Model Predict Section')
    st.markdown('---')

    # Insert Image
    st.image('https://www.startinsland.de/site/assets/files/4129/tk-logo_koop_official_health_partner_pos.800x0.png')

    # Creating Form for Data Inference
    st.markdown('## Input Data')
    with st.form('my_form'):
        Holding_Policy_Duration = st.slider('Holding Policy Duration', min_value=1, max_value=14, value=2, step=1)
        Holding_Policy_Type = st.selectbox('Holding Policy Type', (1, 2, 3, 4))
        Reco_Policy_Cat = st.slider('Recommended Policy Category', min_value=1, max_value=22, value=6, step=1)

        submitted = st.form_submit_button("Check")

    # Dataframe
    data = {
        'Holding_Policy_Duration': Holding_Policy_Duration,
        'Holding_Policy_Type': Holding_Policy_Type,
        'Reco_Policy_Cat': Reco_Policy_Cat,
    }
    df = pd.DataFrame([data])

    # display dataframe of inputted data
    st.dataframe(df)

    # show result
    if submitted:
        result = model.predict(df)
        if result == 1:
            st.write('Lead will likely become actual customer')
        else:
            st.write('Lead will not likely become actual customer')

if __name__=='__main__':
    run()