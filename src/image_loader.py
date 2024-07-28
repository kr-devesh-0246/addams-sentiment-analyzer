import streamlit as st
from PIL import Image

def image_loader(filepath):
    image = Image.open(filepath)
    return image
