# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version January 2023

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
# from plotter import plot_text_sentiment
from src.plotter import plot_text_sentiment as pts
from st_custom_components import st_audiorec
from src.utils import PlayWithWavAudio, save_audio, get_problem_statement# get_mentor_details
from src.models import WhisperModel, RoBERTaModel# Wav2Vec2Model
from src.animation import Animation
from src.audio_to_text_map import tone_to_text_sentiment_map
from src.image_loader import image_loader
# import time
# import pandas as pd
import os


st.set_page_config(
    page_title="aDDAMs",
    page_icon="./img/project_icon.png",
)

# DESIGN implement changes to the standard streamlit UI/UX
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # lightmode

class StreamlitApp:

    def __init__(self):
        # self.audio_to_text = WhisperModel()
        # self.text_to_sentiment = RoBERTaModel()
        # self.audio_to_sentiment = Wav2Vec2Model()

        self.animator = Animation()
        self.play_with_audio = PlayWithWavAudio('./output/recordings')

        # images and configs
        cv_raman_logo = image_loader('./img/cgu-logo.png')
        st.image(cv_raman_logo, width=250)
            
        sih_top_logos = image_loader('./img/sih_top_logos.png')
        st.image(sih_top_logos, use_column_width="auto")

        col1, col2, col3 = st.columns(3)
        with col1:
            pass
        with col2:
            sih_logo = image_loader('./img/SIH-Logo.png')
            st.image(sih_logo, caption="Smart India Hackathon 2023", width=400)
        with col3:
            pass

        with st.expander("Problem Statement"):
            st.table(get_problem_statement())
            

        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     pass
        # with col3:
        #     pass
        # with col2:
        # with st.expander("Mentor: Dr Tusar Kanti Dash"):
        #    st.table(get_mentor_details())


    def main(self):

        col1, smily, col3 = st.columns(3)
        with col1:
            pass
        with smily:
            json_data = self.animator.animate('logo.json')
            st_lottie(
                json_data,
                height=250,
                width=250,
                loop=True,
                speed=1,
                key='smile-emoji'
            )
        with col3:
            pass

        # TITLE and Creator information
        col1, col2, col3 = st.columns(3)
        with col1: 
            pass
        with col2:
            st.image(image_loader('./img/project_icon_updated.png'), width=250)
            # st.write("<h3><center>Audio Sentiment Analyser</center></h3>", unsafe_allow_html=True)
            st.header("Audio Sentiment Analyser")
        with col3:
            pass


        # TUTORIAL: How to use STREAMLIT AUDIO RECORDER?
        # by calling this function an instance of the audio recorder is created
        # once a recording is completed, audio data will be saved to wav_audio_data

        wav_audio_data = st_audiorec() # tadaaaa! yes, that's it! :D

        uploaded_file = st.file_uploader(
                    label="Choose Audio File",
                    type=['.mp3', '.wav', '.opus', '.flac'],
                    accept_multiple_files=False,
                    label_visibility='visible'
                )
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            save_audio(bytes_data, './output/recordings/wav_files/recording.wav')
            self.play_with_audio(filename='recording.wav')
            self.play_with_audio.multiple_split(sec_per_split=10)

        if wav_audio_data is not None:
            print('main audio running')
            # st.audio(wav_audio_data, format='wav')

            save_audio(wav_audio_data, './output/recordings/wav_files/recording.wav')
            self.play_with_audio(filename='recording.wav')
            self.play_with_audio.multiple_split(sec_per_split=10)
            # play_with_audio.multiple_wav2flac()
        
        # col1, col2 = st.columns(2)
        if st.button(label='Classify', help='Click this button to classify'):
            json_data = self.animator.animate('audio_scan.json')
            col1, col2, col3 = st.columns(3)
            with col1:
                pass
            with col2:
                with st_lottie_spinner(json_data,
                                    height=200,
                                    width=200,
                                    loop=True,
                                    speed=1,
                                    key='audio-scan'):
                    # time.sleep(2)

                    audio_clips = self.play_with_audio.get_split_files()
                    print('Audio files being processed')
                    print(audio_clips)
                    print("Audio to Text Processing...")
                    audio_to_text = WhisperModel()
                    obtained_text = audio_to_text(audio_clips)
                    print("Audio to Text Completed.\n Text obtained")
                    print(type(obtained_text))
                    print(obtained_text)

                    print("Text to Sentiment Processing...")
                    text_to_sentiment = RoBERTaModel()
                    text_sentiment = text_to_sentiment(obtained_text)
                    print("Text to Seniment Completed.\nSentiment obtained")
                    print(type(text_sentiment))
                    print(text_sentiment)
                    
                    # tone classifier (wave2vec2)
                    # print("Audio Classification Processing...")
                    # audio_to_sentiment = Wav2Vec2Model()
                    # audio_sentiments = audio_to_sentiment(audio_clips)
                    # print("Audio to Sentiment Completed.\nSentiment obtained")
                    # print(type(audio_sentiments))
                    # print(audio_sentiments)
                with col3:
                    pass

            print('Classification Completed Successfully')
            st.success('Sentiment Analysis Completed')

            text_col, sentiment_col, tone_col = st.columns(3)
            
            file_number = 1
            with text_col:
                with st.expander('Text Transcription'):
                    for text in obtained_text:
                        st.markdown(f'''
                            {file_number}. {text}
                        '''
                        )
                        file_number += 1
        
            file_number = 1
            with sentiment_col:
                with st.expander("Text Sentiment"):
                    i = 0
                    for sentiment in text_sentiment:
                        text, emoji = st.columns(2)
                        with text:
                            st.markdown(f'''
                                {file_number}. {sentiment[0]}
                            '''
                            )
                            file_number += 1

                        with emoji:
                            json_data = self.animator.animate(sentiment[0] + '.json')
                            st_lottie(
                                json_data,
                                height=80,
                                width=80,
                                loop=True,
                                speed=1,
                                key=sentiment[0] + str(i)
                            )
                        i += 1
            
            file_number = 1
            with tone_col:
                with st.expander("Tone Classification (\u03B1lpha)"):
                    st.header("This feature is in alpha stage right now.")
                    # tone classifier (wave2vec2)
                    
                    # for tone in audio_sentiments:
                    #     tone = tone[0]['label']
                        
                    #     text, emoji = st.columns(2)
                    #     with text:
                    #         st.markdown(f'''
                    #             {file_number}. {tone}
                    #         '''
                    #         )
                    #         file_number += 1
                    #     with emoji:
                    #         json_data = self.animator.animate(tone_to_text_sentiment_map[tone] + '.json')
                    #         st_lottie(
                    #             json_data,
                    #             height=80,
                    #             width=80,
                    #             loop=True,
                    #             speed=1,
                    #             key=tone + str(i)
                    #         )
                    #     i += 1
            

            # st.pyplot(pts(text_sentiment))
            # st.pyplot(pts(audio_sentiments))
            pts(text_sentiment, audio_clips)

            print('Process Completed')

        os.system('cp ./output/recordings/wav_files/* ./output/recordings/wav_files_backup')
        os.system('rm ./output/recordings/wav_files/*')

        # with col2:
        #     if st.button(label='Audio Classifier', help='Click this button to classify'):
        #         pass

if __name__ == '__main__':
    # call main function
    app = StreamlitApp()
    app.main()
