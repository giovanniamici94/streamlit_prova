'''
Streamlit tutorial
Check streamlit website > Streamlit library > API reference
to get a bunch of functionalities such as those here below
If you have any Py dependencies, include them in requirements.txt (on github repo)

RUN FROM LOCAL CODE
Run on terminal: streamlit run code.py, then a webpage will appear.

RUN FROM GITHUB CODE
Go to: Streamlit website > my apps > create app (put this github repository)

Once the app is opened in the website, interactively play with the options provided.
'''

import streamlit as st
import pandas as pd
import numpy as np

st.write('# Main')

st.write('Hello again')
answer = st.text_input('Favourite movie?')
st.write(f'Ok, you just replied: {answer}')
is_clicked = st.button('Click me')

#st.link_button('Profile', url='/profile?id1234') #not working

data = pd.read_csv('data.csv')
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)
st.bar_chart(chart_data)
st.line_chart(chart_data)
