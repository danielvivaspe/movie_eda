import streamlit as st
from PIL import Image

def phase1():
    image = Image.open('presentation/img/eda.png')
    st.image(image, use_column_width='auto')
    st.markdown("""da
                <br/><div style="text-align: center; font-size: 90px">¿Por qué películas?</div>
            """, unsafe_allow_html=True)