from PIL import Image
import streamlit as st



def app():
    myimage = 'app/static/cs.png'
    linkedin = 'app/static/vitesco.jpg'
    style_image2 = """
    width: auto;
    max-width: 900px;
    height: auto;
    max-height: 800px;
    display: block;
    justify-content: center;
    border-radius: 30%;
    """
    st.markdown(f'<img src="{myimage}" style="{style_image2}">',unsafe_allow_html=True)
    st.markdown(f'<img src="{linkedin}">',unsafe_allow_html=True)