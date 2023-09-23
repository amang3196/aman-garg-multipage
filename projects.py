from PIL import Image
import streamlit as st

def app():
    
    mrs_img = "app/static/mrs.jpeg"
    cs_img = "app/static/cs.png"
    
    image_style = '''
    height: 150px;
    width: 400px;
    margin: 5px;
    '''
    image_style2 = '''
    height: 150px;
    width: 400px;
    margin: 5px;
    '''
    
    
# ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        
        with image_column:
            st.markdown(f'<img src="{mrs_img}" style="{image_style}">',unsafe_allow_html=True)
            
            
        with text_column:
            st.subheader("Movie Recommender System")
            st.write(
                """
                Developed a recommender system for a pre-built movie dataset using collaborative filtering. Similar users were identified using k-nearest neighbours.
                """)
            st.markdown("[Link](https://github.com/amang3196/collaborative-filtering-recommender-system)     [Demo]()")
            #st.markdown("[Demo]()")
    
    
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.markdown(f'<img src="{cs_img}" style="{image_style2}">',unsafe_allow_html=True)
        with text_column:
            st.subheader("Customer Segmentation using Unsupervised Learning")
            st.write(
                """
                Identified various segments of customers using k-means clustering based on age, gender,income and annual spending which in turn helped in developing marketing strategies.
                """
            )
            st.markdown("[Link](https://github.com/amang3196/Customer-Segmentation)")
            