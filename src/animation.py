import streamlit as st
import json

class Animation:
    def __init__(self):
        self.folder = './animation/'
    
    def animate(self, file_name):
        path = self.folder + file_name
        with open(path, 'r') as animation_file:
            jason_data = json.load(animation_file)

        return jason_data 

        