# Import Libraries
import streamlit as st

# Import finished streamlit pages
import eda
import model

# Navigation Button
navi = st.sidebar.selectbox('Choose page: ', ('Predictor', 'EDA'))

if navi == 'Predictor':
    model.run()
else:
    eda.run()