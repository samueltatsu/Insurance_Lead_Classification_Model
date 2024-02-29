# Import Essential Library
import streamlit as st
import pandas as pd

# Library for Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Function to run EDA
def run():
    # Set Title
    st.title('Insurance Lead Prediction Model')

    # Sub Title
    st.subheader('Exploratory Data Analysis Section')
    st.markdown('---')

    # Insert Image
    st.image('https://www.startinsland.de/site/assets/files/4129/tk-logo_koop_official_health_partner_pos.800x0.png')

    # Markdown
    st.markdown('# Dataframe Insurance Lead')

    # Load Data
    data = pd.read_csv('data_eda.csv')

    # Display dataframe in StreamLit
    st.dataframe(data.head(20))
    st.markdown('---')

    # EDA
    st.markdown('## EDA')

    # Convert Rate Balance Visualization
    st.markdown('### Convert Rate Balance')
    canvas = plt.figure(figsize=(10,5))
    sns.barplot(x=data['Response'].value_counts().index, y=data['Response'].value_counts(), hue=data['Response'].value_counts().index)
    st.pyplot(canvas)
    st.markdown('Data is still slightly imbalanced (biased towards clients who will not likely convert)')

    # Holding Policy Duration Distribution Visualization 
    st.markdown('### Holding Policy Duration Distribution')
    canvas = plt.figure(figsize=(10,5))
    sns.histplot(data['Holding_Policy_Duration'], kde=True, bins=15)
    st.pyplot(canvas)

    # Holding Policy Type Distribution Visualization 
    st.markdown('### Holding Policy Type Distribution')
    canvas = plt.figure(figsize=(10,5))
    sns.barplot(x=data['Holding_Policy_Type'].value_counts().index, y=data['Holding_Policy_Type'].value_counts(), hue=data['Holding_Policy_Type'].value_counts().index)
    st.pyplot(canvas)

    # Recommended Policy Category Distribution Visualization 
    st.markdown('### Recommended Policy Category Distribution')
    canvas = plt.figure(figsize=(15,5))
    sns.barplot(x=data['Reco_Policy_Cat'].value_counts().index, y=data['Reco_Policy_Cat'].value_counts(), hue=data['Reco_Policy_Cat'].value_counts().index)
    st.pyplot(canvas)


if __name__=='__main__':
    run()