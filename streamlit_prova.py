'''
Run on terminal: streamlit run code.py, then a webpage will appear
where you can re-run from there each time you update the Py code.
Check streamlit website > Streamlit library > API reference
to get a bunch of functionalities such as those here below
Note: if you need to install anything, it might be necessary to put such
package in this very folder.
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
