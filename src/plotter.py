import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from audio_to_text_map import text_sentiments
from pandas import DataFrame 

# def plot_text_sentiment(text_sentiment):
#     fig, ax = plt.subplots()
#     d = zip(*text_sentiment)
#     ax = plt.scatter(*d)
#     return fig


# for text sentiment
# def plot_text_sentiment(text_sentiment_scores, audio_file_list):
#     tuples_list = zip(*text_sentiment_scores)
#     audio_file_list = [10*i for i in range(len(audio_file_list))]
#     list_of_sentiment_scores = [list(tuppy) for tuppy in tuples_list]
#     print(list_of_sentiment_scores)
#     list_of_sentiment_labels = list_of_sentiment_scores[0]
#     print(list_of_sentiment_scores)
#     fig = plt.figure(figsize=(10, 4))
#     sns.lineplot(, x=audio_file_list, y=text_sentiments)
#     st.pyplot(fig)


def plot_text_sentiment(text_sentiment_scores, audio_file_list):
    tuples_list = zip(*text_sentiment_scores)
    audio_file_list = [10*i for i in range(len(audio_file_list))]
    list_of_sentiment_labels = [list(tuppy) for tuppy in tuples_list][0]
    df = DataFrame(list(zip(audio_file_list, list_of_sentiment_labels)), columns=['x_labels', 'y_labels'])
    fig = plt.figure(figsize=(10, 4))
    sns.set_style('whitegrid')
    sns.lineplot(x='x_labels', y='y_labels', data=df)
    plt.xlabel("Recording Clips")
    plt.ylabel("Sentiments")
    plt.title("Sentiment Trends throughout the audio")
    st.pyplot(fig)

# def plot_audio_sentiment(audio_sentiment):
    
    