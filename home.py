from pathlib import Path
# import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import base64


def app():
    
    # linkedin = '''                        
    # <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><i class="fa-brands fa-linkedin-in"></i>&nbsp; LinkedIN
    # '''
    
    # email = '''
    # <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><i class="fa-regular fa-envelope"></i>&nbsp; Email
    # '''
    
    # github = '''
    # <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><i class="fa-brands fa-github"></i>&nbsp; Github 
    # '''
    
    resume_file = "./static/Aman_Garg_Resume.pdf"         # Resume file
    profile_pic = "./static/profile-pic.png"              # Profile Picture
    
    NAME = "Aman Garg"
    DESCRIPTION = """
    I am an MBA graduate specializing in Data Sciences and Data Analytics. Possessing this degree showcases my interest and skills in Data Science and Data Analytics along with how it can be leveraged into developing businesses.
    """

    SOCIAL_MEDIA = {
        "LinkedIn" : "https://www.linkedin.com/in/aman-garg-b2ba4a120/",
        "Email" : "mailto:amangarg3196@gmail.com",
        "Github" : "https://github.com/amang3196"
    }
    
    # READING RESUME AND PROFILE PIC
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)
    
    # ---- HEADER SECTION ----
    st.markdown("***")
    with st.container():
        left_col, center_col, right_col = st.columns([3,0.5,2])
        with left_col:
            st.subheader(f"Hi, I am {NAME} :wave:")
            st.title("A Data Scientist")
            st.write(DESCRIPTION)
            st.download_button(
                label=" 📄 Download Resume",
                data=PDFbyte,
                file_name=resume_file,
                mime="application/octet-stream",
            )
            
            
            # --- SOCIAL LINKS ---
            st.markdown("***")
            cols = st.columns(len(SOCIAL_MEDIA))
            for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
                cols[index].write(f'[{platform}]({link})',unsafe_allow_html=True)
            
        with right_col:
            st.image(profile_pic, width=350, use_column_width='never')
        st.markdown("***")

    # EDUCATION
    with st.container():
        left_col, right_col = st.columns(2)
        with left_col:
            education_img = "app/static/education.png"
            style = """
            height:55%;
            width:55%;
            margin-left: 25px;
            """
            st.markdown(f"""
                        <img src="{education_img}" style="{style}">
                        """, unsafe_allow_html=True)
            
            
        with right_col:
            st.title("My Education")
            # Education 1
            st.write("📚", "**MBA (Data Sciences & Data Analytics)** | *Symbiosis International University*")
            st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗓️ 2021 - 2023")

            # Education 2
            st.write('\n')
            st.write("📚", "**B.C.A** | *Symbiosis International University*")
            st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗓️ 2018 - 2021")
