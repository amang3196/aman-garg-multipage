import streamlit as st

def app():
        # ---- CONTACT ----
    with st.container():
        st.write("---")
        
        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/amangarg3196@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
      
        """
        left_column, center_col, right_column = st.columns([0.5,1,0.5])
        with left_column:
            st.empty()
        with center_col:
            st.header("Get In Touch With Me!",)
            st.write("##")
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()