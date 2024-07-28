import pyaudio


THRESHOLD = 30
SHORT_NORMALIZE = (1.0/32768.0)
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
SWIDTH = 2
INTERVAL = 10
INPUT_INDEX = 9
TIMEOUT_LENGTH = 5
MAX_TIME = 120 # seconds


recording_directory  = r'./output/recordings/wav_files/'
flac_files_directory = r'./output/recordings/flac_files/' 