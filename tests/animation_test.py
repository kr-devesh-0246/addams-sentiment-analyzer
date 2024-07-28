import streamlit as st
import streamlit_lottie as st_lottie
from animation import Animation

def main():
    test = Animation()
    json_data = test.animate('confusion.json')
    st_lottie(
        json_data,
        height=200,
        width=200,
        loop=True,
        speed=1,
        key='smile-emoji'
    )

    st.success('hey')

main()