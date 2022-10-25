
import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="auto",
    page_title=" Seeker-Data",
    page_icon="-)"
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
# st.sidebar.success("EMA")
# st.sidebar.markdown("EMA") 

title = '🚀 Seeker ⚙️ Data 📈' 
st.markdown(f"<h1 style='text-align: center; color: orange;'>{title}</h1>", unsafe_allow_html=True)

def fig_upd(fig):
    fig.update_xaxes(minor=dict(showgrid=True),gridcolor='#333300')
    fig.update_yaxes(minor=dict(showgrid=True),gridcolor='#333300')
    fig.update_layout(plot_bgcolor='rgba(8,8,8,8)')
    st.plotly_chart(fig,use_container_width=True)

import plotly.graph_objects as go

timec = [0,1,2,3,4]
timed = timee = timec
cseq = [1,1,1,1,1]
dseq = [2,2,2,2,2]
eseq = [3,3,3,3,3]

#overplots of cde pkt seq no.'s
fig1=go.Figure()
fig1.add_trace(go.Scatter(x=timec, y=cseq,
                    mode='lines+markers',
                    name=''))
# fig1.add_trace(go.Scatter(x=timed, y=dseq,
#                     mode='markers',
#                     name='PKT_D'))
# fig1.add_trace(go.Scatter(x=timee, y=eseq,
#                     mode='markers',
#                     name='PKT_E'))


fig1.update_layout(
    xaxis_title="tmtime in seconds",
    xaxis_title_font_size=22,
    yaxis_title="",
    yaxis_title_font_size=22,
    legend_title="Legend Title",
    legend_title_font_size=22,
    title_text="title",
    title_font_size=22,
    title_y=0.9,
    title_x=0.5,
    # yaxis_range=[0,260],
    autosize=True,
    width=1000,
    height=700
)

fig_upd(fig1)