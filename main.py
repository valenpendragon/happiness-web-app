import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/happy.csv')
# df = df.drop('country', axis='columns')
cols = ['happiness', 'gdp', 'social_support', 'life_expectancy',
        'freedom_to_make_life_choices', 'generosity', 'corruption']
items = ['Happiness', 'GDP', 'Social Support', 'Life Expectancy',
         'Freedom To Make Life Choices', 'Generosity', 'Corruption']


st.title("In Search of Happiness")
x_choice = st.selectbox("Select the data for the X-axis", options=items)
y_choice = st.selectbox("Select the data for the Y-axis", options=items)

st.subheader(f"{x_choice} and {y_choice}")

x_axis = cols[items.index(x_choice)]
y_axis = cols[items.index(y_choice)]
figure = px.scatter(data_frame=df, x=df[x_axis], y=df[y_axis], labels={"x": x_choice, "y": y_choice})
st.plotly_chart(figure)
