import streamlit as st
# from pages.EMA import EMA

st.set_page_config(layout="centered",initial_sidebar_state="auto",
    page_title="EMA -Data",
    page_icon=":)"
    )
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# ----------------------------------------------------
title = '🚀 PDF Report Generator 📈' 
st.markdown(f"<h1 style='text-align: center; color: orange;'>{title}</h1>", unsafe_allow_html=True)
# --------- Import ---------------
from fpdf import FPDF

# ----------main-----------------------
st.markdown('#### click every page and then click below Download button')
if st.button('Download PDF'):
    name = "EMA"

    WIDTH = 210
    HEIGHT=297

    pdf = FPDF()
    # first page ------------------------
    pdf.add_page()

    pdf.set_font('Arial','B',20)
    pdf.cell(40,10,f"Checkout Report of {name}")

    pdf.image('act01.png',5,30, WIDTH-10)
    pdf.image('act02.png',5,155, WIDTH-10)

    pdf.set_font('Arial','B',8)
    pdf.cell(200,0,"page 1 of 2")
    st.warning('Page 1 of 2 completed')
    # --------------------------------------------
    #second page
    pdf.add_page()

    pdf.image('act03.png',5,30, WIDTH-10)
    pdf.image('act04.png',5,155, WIDTH-10)

    pdf.set_font('Arial','B',8)
    pdf.cell(200,0,"page 2 of 2")
    # --------------------------------------------
    # -----------output-----------------------------
    pdf.output(f'report_{name}.pdf','F')
    st.success('Page 2 of 2 compeleted')
    # -------------------------------------------------
    import os
    os.remove("act01.png")
    os.remove("act02.png")
    os.remove("act03.png")
    os.remove("act04.png")
    st.success("Report Generated")
    # ---------------------------------------------------