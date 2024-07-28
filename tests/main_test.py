from models import WhisperModel, RoBERTaModel, Wav2Vec2Model
# from wav2vec2_model import 
# from roberta_model import 
import time


audio_path = "/home/anurag/Documents/AI-ML/practice/Audio-Recognition/recordings/recording_10.wav"

print('\n\n Audio to Text Processing...')
time.sleep(2)
audio_to_text = WhisperModel()
text = audio_to_text(audio_path)


print('\n\n Text to Sentiment Processing...')
time.sleep(2)
text_to_sentiment = RoBERTaModel()
sentiment = text_to_sentiment(text)
print('Context Sentiment: ', sentiment)

print('\n\n Audio Sentiment Processing...')
time.sleep(2)
# audio classification
audio_to_sentiment = Wav2Vec2Model()
sentiments = audio_to_sentiment(audio_path)
print("Audio Sentiments: ", sentiments)

