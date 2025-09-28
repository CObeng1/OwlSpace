import streamlit as st
from PIL import Image

# Load images
onboarding_img = Image.open("assets/onboarding.png")
home_img = Image.open("assets/Home.png")
affirmations_img = Image.open("assets/Affirmation.png")

st.set_page_config(page_title="OwlSpace", layout="centered")

st.title("📱 OwlSpace Preview")

st.subheader("Onboarding")
st.image(onboarding_img, use_container_width=True)

st.subheader("Home")
st.image(home_img, use_container_width=True)

st.subheader("Affirmations")
st.image(affirmations_img, use_container_width=True)

st.markdown("---")
st.caption("OwlSpace • A space to unruffle your feathers 🦉")
