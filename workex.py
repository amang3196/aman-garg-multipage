import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


def app():
        # --- WORK HISTORY ---
    st.write("***")
    st.write('\n')

    # Image paths
    aethereus = "app/static/aethereus.png"
    alphaai = "app/static/alpha-ai.jpeg"
    vitesco = "app/static/vitesco.jpg"
    
    
    # Image styles
    image_style1 = '''
    height: 100px;
    width: 300px;
    margin-top: 90px;
    '''
    
    image_style2 = '''
    height: 175px;
    width: 300px;
    margin-top: 100px;
    '''
    
    image_style3 = '''
    height: 175px;
    width: 300px;
    margin-top: 30px;
    '''
    
    left_col, right_col = st.columns([3,1])
    with left_col:
        # --- JOB 1
        st.write("💼", "**Intern - Data Science/AI** | *Aethereus Consulting*")
        st.write("🗓️ 05/2023 - 08/2023")
        st.write(
            """
        ✅ Built requirements for AI based solution for route optimization for field sales reps

        ✅ Built a connection to source data from Salesforce CDP into AWS
        
        ✅ Developed a pipeline to build and deploy ML model using Amazon Sagemaker
        
        ✅ Developed a VR Gallery using Unity and Oculus Quest 2 to market the companies products
        
        ✅ Tools: Python, Amazon S3, Amazon Sagemaker, Amazon API Gateway, AWS Lambda, Unity

        """
        )
    with right_col:
        # Insert company logo
        img = Image.open("./static/aethereus1.png")
        #st.image(img, width=275)
        st.markdown(f'<img src="{aethereus}" style="{image_style1}">',unsafe_allow_html=True)

    
    # --- JOB 2
    st.markdown("***")
    st.write('\n')
    
    left_col, right_col = st.columns([3,1])
    
    with left_col:
        st.write("💼", "**Data Science Intern | Alpha AI**")
        st.write("🗓️ 04/2022 - 07/2022")
        st.write(
            """
        ✅ Research and experiment with pre built AI models to solve existing business problems

        ✅ Built an AI generated animation with first order head motion, audio-video lip syncing algorithms
        
        ✅ Developed a streamlit API to combine first order head motion and lip syncing
        
        ✅ Containerize the streamlit API using Docker
        
        ✅ Parallelize machine learning model inference in order to serve multiple users
        
        ✅ Collaborate with other teams as an additional resource
        
        ✅ Tools: Generative AI, PyTorch, Tensorflow OpenCV, Streamlit, Docker, Blender, Omniverse.

        """
        )
    with right_col:
        # Insert company logo
        img = Image.open("./static/alpha-ai.jpeg")
        #st.image(img)
        st.markdown(f'<img src="{alphaai}" style="{image_style2}">',unsafe_allow_html=True)

    # --- JOB 3
    st.markdown("***")
    st.write('\n')
    
    left_col, right_col = st.columns([3,1])
    with left_col:
        st.write("💼", "**AI Intern | Vitesco Technologies India**")
        st.write("🗓️ 09/2020 - 07/2021")
        st.write(
            """
        ✅ Collaborate with a team of domain experts to understand the business problem
        
        ✅ Provide bridge between domain knowledge and Artificial Intelligence.

        ✅ Built a neural network to predict the value of axle torque in order to develop a digital twin.
        
        ✅ Tools: Pycharm, Python, Pandas, Keras, Numpy, asammdf.
        """
        )
    with right_col:
        # Insert company logo
        img = Image.open("./static/vitesco.jpg")
        #st.image(img)
        st.markdown(f'<img src="{vitesco}" style="{image_style3}">',unsafe_allow_html=True)
    st.markdown("***")