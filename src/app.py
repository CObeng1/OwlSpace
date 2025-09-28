import streamlit as st
from PIL import Image

# Loading the image
onboarding_img = Image.open("assets/images/onboarding.png")

# Display it
st.image(onboarding_img, use_column_width=True)