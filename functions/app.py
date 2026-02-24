import streamlit as st
from plotly import plot_ts

st.title('Stocks History')
st.write('Lool the stocks values')

ticker = st.sidebar.text_input('Choose the ticket: ', value= 'AAPL')

fig = plot_ts(ticker)

st.plotly_chart(fig)