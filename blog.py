import streamlit as st
import pandas as pd

st.title('Multiply two numbers')
title = st.text_input('Enter Number 1', '')
title1 = st.text_input('Enter Number 2', '')

if title and title1:
    if st.button('Multiply'):
        ans = float(title)*float(title1)
        st.write("Multiplication of the two numbers is " + str(ans) )
