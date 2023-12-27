# Streamlit plotting demo

# Steps
#1. Make a Python file where we will house all our Streamlit code.
#2. Use the plotting code given in the demo.
#3. Make small edits for practice.
#4. Run our file locally .

import streamlit as st
import time
import numpy as np

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.rand(5)
    status_text.text("%i%% Complete"% i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)
progress_bar.empty()

# Streamlit widgets automatically run the scrip
# this button is not connected to any other log
# rerun.
st.button("Re-run") # El salvajeee !!!! Este es el tipooooo!!!
