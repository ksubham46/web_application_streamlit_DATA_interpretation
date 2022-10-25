
import streamlit as st
import os 
ll = os.listdir("C://Users//Ksubh//Desktop//DESK//testing//web_APP")
st.write(ll)
li =[]
for x in os.listdir():
    if x.endswith(".png"):
        li.append(x)

st.write(li)

# option = st.selectbox(
#     'How would you like to be contacted?',
#     li)

# st.write(option)