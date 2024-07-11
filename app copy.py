# Principal
import streamlit as st
import interpreter

# st components
from st_components.st_init import set_style
from st_components.st_session_states import init_session_states
from st_components.st_sidebar import st_sidebar
from st_components.st_main import st_main

#validation
from litellm import completion
from openai import Model

set_style()

#st.title("💬 scalenow-AI")
#st.image('http://www.scalenow.com.au/assets/img/scalenow/scalenowAi1.png', caption='Your Image Caption', use_column_width=True)
st.markdown('<h1 style="color: #E57254 ;">💬 scalenow-AI</h1>', unsafe_allow_html=True)
#st.markdown('<p style="color:#FFFFFF;">👉 Set your OpenAI api key, to be able to run code while you generate it 🚀</p>', unsafe_allow_html=True)

init_session_states()

st_sidebar()

st_main()

# made with streamlit and three lines hidden 
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


