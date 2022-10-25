import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="auto",
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
title = '🚀 EMA ⚙️ Data 📈' 
st.markdown(f"<h1 style='text-align: center; color: orange;'>{title}</h1>", unsafe_allow_html=True)
# -----------------------------------------------
import os 
li =[]
for x in os.listdir():
    if x.endswith(".bin"):
        li.append(x)

filename = st.selectbox('Select File',li)
st.write(filename)

# ---------------------------------------------------


def fig_upd(fig,a):
    fig.update_xaxes(minor=dict(showgrid=True),gridcolor='#333300')
    fig.update_yaxes(minor=dict(showgrid=True),gridcolor='#333300')
    fig.update_layout(plot_bgcolor='rgba(8,8,8,8)',title_text=f"Actuator {a}")
    fig.update_layout(
    xaxis_title="Time in seconds",
    xaxis_title_font_size=22,
    yaxis_title="Amplitude in Voltage",
    yaxis_title_font_size=22,
    legend_title="Legend Title",
    legend_title_font_size=12,
    title_font_size=29,
    title_y=0.9,
    title_x=0.5,
    # yaxis_range=[0,260],
    autosize=True,
    width=1000,
    height=600,
    )
    st.plotly_chart(fig,use_container_width=True)

# ------------------------------------------------
import plotly.graph_objects as go

if __name__ =='__main__':
    timec = [1,1,2,3,4]
    timed = timee = timec
    cseq = [1,1,1,1,1]
    dseq = [2,2,2,2,2]
    eseq = [3,3,3,3,3]

    #-----------------------------actuator  -1
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=timec, y=cseq,
                        mode='lines+markers',
                        name='Cmd'))
    fig1.add_trace(go.Scatter(x=timed, y=dseq,
                        mode='lines+markers',
                        name='ABS_Feedback'))
    fig1.add_trace(go.Scatter(x=timee, y=eseq,
                        mode='lines+markers',
                        name='Curr'))
    # ----------------------------------------------
    #-----------------------------actuator  -2
    fig2=go.Figure()
    fig2.add_trace(go.Scatter(x=timec, y=cseq,
                        mode='lines+markers',
                        name='Cmd'))
    fig2.add_trace(go.Scatter(x=timed, y=dseq,
                        mode='lines+markers',
                        name='ABS_Feedback'))
    fig2.add_trace(go.Scatter(x=timee, y=eseq,
                        mode='lines+markers',
                        name='Curr'))
    # ----------------------------------------------
    #-----------------------------actuator  -3
    fig3=go.Figure()
    fig3.add_trace(go.Scatter(x=timec, y=cseq,
                        mode='lines+markers',
                        name='Cmd'))
    fig3.add_trace(go.Scatter(x=timed, y=dseq,
                        mode='lines+markers',
                        name='ABS_Feedback'))
    fig3.add_trace(go.Scatter(x=timee, y=eseq,
                        mode='lines+markers',
                        name='Curr'))
    # ----------------------------------------------
    #-----------------------------actuator  -4
    fig4=go.Figure()
    fig4.add_trace(go.Scatter(x=timec, y=cseq,
                        mode='lines+markers',
                        name='Cmd'))
    fig4.add_trace(go.Scatter(x=timed, y=dseq,
                        mode='lines+markers',
                        name='ABS_Feedback'))
    fig4.add_trace(go.Scatter(x=timee, y=eseq,
                        mode='lines+markers',
                        name='Curr'))
    # ----------------------------------------------
    # ---------

    
    col1,col2 = st.columns([2,2])
    with col1:
        fig_upd(fig1,1)
    with col2:
        fig_upd(fig2,2)
    # ----------------------------------
    col1,col2 = st.columns([2,2])
    with col1:
        fig_upd(fig3,3)
    with col2:
        fig_upd(fig4,4)



    #
    #  For report generation---------------------
    fig1.write_image('img/act01.png')
    fig2.write_image('img/act02.png')
    fig3.write_image('img/act03.png')
    fig4.write_image('img/act04.png')

    # hello



