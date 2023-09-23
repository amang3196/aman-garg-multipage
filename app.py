import streamlit as st
from streamlit_option_menu import option_menu
import home,workex, projects, contact,test


st.set_page_config(page_title="Aman Garg", page_icon=":tada:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

selected = option_menu(
    menu_title=None,
    options = ["About Me", "Work Experience", "Projects", "Contact"],
    icons=["house", "book", "folder", "envelope"],
    default_index = 0,
    orientation = "horizontal",
    styles={
        "nav-link-selected": {"background-color": "#555555"}
    }
    
)
if selected == "About Me":
    home.app()
if selected == "Projects":
    projects.app()
if selected == "Work Experience":
    workex.app()
if selected == "Contact":
    contact.app()