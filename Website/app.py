from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import 
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/12e2d5e7-0727-4b84-b3cc-14ac204b96d9/shYR8ngqxh.json")
img_loading_png = Image.open("images/Loading.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, I am Robert Asumeng")
    left_column, right__column = st.columns(2)
    with left_column:
        st.title("About Me")
        st.write(""" 
                I am a freshman at the University of Texas at Arlington majoring in Computer Science.\n
                My goals for freshmen and sophmore year are to meet new poeple and network.\n
                Along with networking, I also intend to aquire an computer programing internshi, though I am open to other options.\n
                I am working on devloping various perosnal projects and plan to have this as my portfolio website.\n
                I am passonite about finding ways to use Python to be more efficient and effective in business settings.\n
                """)
    with right__column:
        st_lottie(lottie_coding, height=300, key="coding")  

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.write("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_loading_png, width=300)

    with text_column:
        st.subheader("Intergrate Lottie Animeations inside your Streamlit App")
        st.write(
            """
            Learn how to sue Lottie Files in StreamLit!\n
            Animations make our web app more engaigin and fun, and lottie Files are the easiest way to do it.\n
            In this tutorial, I'll Show you exactly how to do it
            """
        )
with st.container():
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        st.image(img_loading_png, width=300)

    with text_column:
        st.subheader("Place holder for upcoming projects...\n")
        st.write("Stay tuned for more :smile:")
# ---- CONTACT ME ----
with st.container():
    st.write("---")
    st.header("Get in Touch with Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/asumengrobert787@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
