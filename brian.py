from PIL import Image
import requests

import streamlit as st
#from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.set_page_config(
    page_title="Multipage App",
    page_icon="wave"
)

st.title("Brian Blog")


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/pic.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("Hi, I'm Brian P. Alingco :wave:")
    st.subheader("A BSCpE Student from Surigao del Norte State University")
    st.write("Hello, I'm a passionate computer engineering student with a keen interest in developing innovative solutions for real-world problems. ")
    st.write("Currently honing my skills in programming, hardware design, and problem-solving. Excited to contribute to the ever-evolving field of technology.")
    st.subheader("This is my socials feel free to visit them.")
    st.write(" ▶ Facebook: https://web.facebook.com/vjbrian.alingco")
    st.write(" ▶Email: brianalingco730@gmail.com")
    st.write(" ▶Contact Number:09674402363")
