# Streamlit plotting demo

# Steps
#1. Make a Python file where we will house all our Streamlit code.
#2. Use the plotting code given in the demo.
#3. Make small edits for practice.
#4. Run our file locally .

import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt 

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(50, 1).cumsum(axis=0)
    status_text.text("%i%% Complete"% i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)
progress_bar.empty()

# Streamlit widgets automatically run the scrip
# this button is not connected to any other log
# rerun.
st.button("Re-run") 

 

with st.form('first form'):
	perc_heads = st.number_input(label='Chance of Coins Landing on Heads', min_value=0.0, 	max_value=1.0, value=.5)  
	graph_title = st.text_input(label='Graph Title') 
	my_submit_button = st.form_submit_button()

binom_dist = np.random.binomial(1, perc_heads, 1000)  
list_of_means = []  
for i in range(0, 1000):
	list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())  

fig, ax = plt.subplots()  
plt.hist(list_of_means, range=[0,1]) 
plt.title(graph_title) 
st.pyplot(fig) 