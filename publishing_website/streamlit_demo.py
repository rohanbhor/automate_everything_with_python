import pandas
import streamlit as st

data = {
    'series_1': [1, 3, 4, 5, 7],
    'series_2': [10, 30, 40, 100, 250]
}
df = pandas.DataFrame(data)
st.title('Our first Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('This is our first Web App')
st.write(df)
st.line_chart(df)

my_slider = st.slider("Celcius")
st.write(my_slider, 'In Fahrenheit is ', my_slider*9/5 + 32)