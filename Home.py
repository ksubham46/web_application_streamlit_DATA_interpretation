import streamlit as st
st.set_page_config(
    page_title="Checkout Data",
    page_icon="ποΈβπ¨οΈπ±",
    layout="wide"
)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# st.set_page_config(layout="wide")
# st.sidebar.success("Home")
# st.sidebar.text("π  OBC Survillance Data ")
p_color = "white"

title = 'π Checkout π₯οΈ Data π' 
st.markdown(f"<h1 style='text-align: center; color: green;'>{title}</h1>", unsafe_allow_html=True)

new = ("Page under Development ...... Please check other page    ")
st.markdown(f"<p style='text-align: left; color: {p_color};'>{new}</p>", unsafe_allow_html=True)


emo = "π’π£π΄π‘πΊπ»ποΈβπ¨οΈπ±ββ­π«ββπππππͺ©π©π―πππππππππβοΈπ₯οΈπΉοΈβπ§βοΈ"
st.write(f"{emo}")

def Failed():
    return(f"Failed π΄ ")

def Passed():
    return(f"Passed π’ ")

d =200
st.write(Passed())
st.write(Failed())


# import pages.us as us
# st.write(us.ll[0])


