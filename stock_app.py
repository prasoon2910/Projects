#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install yfinance


# In[7]:


import yfinance as yf
import streamlit as st
import pandas as pd

# Example: Fetch historical stock data for Apple Inc. (AAPL)
data = yf.download('AAPL', start='2022-01-01', end='2022-12-31')

# Streamlit app
st.title("Stock Price Chart for AAPL")

# Display the fetched data
st.write("Historical Stock Data for AAPL:")
st.write(data)

# Create a line chart using Plotly
st.write("Interactive Stock Price Chart:")
st.line_chart(data['Close'])

# You can add more Streamlit elements and customizations here as needed.


# In[ ]:




