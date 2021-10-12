import time, os
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image
from keras import models
from tensorflow.python import tf2

# from tensorflow.keras.models import load_model
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from scipy.io import wavfile
# import scipy
# from sklearn.preprocessing import normalize
# from scipy.io.wavfile import read, write
import base64
# import pyaudio
# import wave

#load models
model = load_model("finalmodel.hdf5")

# constants
starttime = datetime.now()


def zcr(data, frame_length=2048, hop_length=512):
    zcr = librosa.feature.zero_crossing_rate(y=data, frame_length=frame_length, hop_length=hop_length)
    return np.squeeze(zcr)
def rmse(data, frame_length=2048, hop_length=512):
    rmse = librosa.feature.rms(y=data, frame_length=frame_length, hop_length=hop_length)
    return np.squeeze(rmse)
def mfcc(data, sr, frame_length=2048, hop_length=512, flatten: bool = True):
    mfcc_feature = librosa.feature.mfcc(y=data, sr=sr)
    return np.squeeze(mfcc_feature.T) if not flatten else np.ravel(mfcc_feature.T)
def extract_features(data, sr, frame_length=2048, hop_length=512):
    result = np.array([])
    result = np.hstack((result,
                        zcr(data, frame_length, hop_length),
                        # np.mean(energy(data, frame_length, hop_length),axis=0),
                        # np.mean(entropy_of_energy(data, frame_length, hop_length), axis=0),
                        rmse(data, frame_length, hop_length),
                        # spc(data, sr, frame_length, hop_length),
                        # spc_entropy(data, sr),
                        # spc_flux(data),
                        # spc_rollof(data, sr, frame_length, hop_length),
                        # chroma_stft(data, sr, frame_length, hop_length),
                        # mel_spc(data, sr, frame_length, hop_length, flatten=True)
                        mfcc(data, sr, frame_length, hop_length)
                                    ))
    return result

def noise(data, random=False, rate=0.035, threshold=0.075):
    """Add some noise to sound sample. Use random if you want to add random noise with some threshold.
    Or use rate Random=False and rate for always adding fixed noise."""
    if random:
        rate = np.random.random() * threshold
    noise_amp = rate*np.random.uniform()*np.amax(data)
    data = data + noise_amp*np.random.normal(size=data.shape[0])
    return data

def pitch(data, sampling_rate, pitch_factor=0.7, random=False):
    """"Add some pitch to sound sample. Use random if you want to add random pitch with some threshold.
    Or use pitch_factor Random=False and rate for always adding fixed pitch."""
    if random:
        pitch_factor=np.random.random() * pitch_factor
    return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

def get_features(path, duration=2.5, offset=0.6):
    # duration and offset are used to take care of the no audio in start and the ending of each audio files as seen above.
    data, sample_rate = librosa.load(path, duration=duration, offset=offset)

     # without augmentation
    res1 = extract_features(data, sample_rate)
    result = np.array(res1)

    # data with noise
    noise_data = noise(data, random=True)
    res2 = extract_features(noise_data, sample_rate)
    result = np.vstack((result, res2)) # stacking vertically

    # data with pitching
    pitched_data = pitch(data, sample_rate, random=True)
    res3 = extract_features(pitched_data, sample_rate)
    result = np.vstack((result, res3)) # stacking vertically

    # data with pitching and white_noise
    new_data = pitch(data, sample_rate, random=True)
    data_noise_pitch = noise(new_data, random=True)
    res3 = extract_features(data_noise_pitch, sample_rate)
    result = np.vstack((result, res3)) # stacking vertically

    return result

# @st.cache
def log_file(txt=None):
    with open("log.txt", "a") as f:
        datetoday = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"{txt} - {datetoday};\n")

# @st.cache
def save_audio(file):
    if file.size > 4000000:
        return 1
    folder = "audio"
    datetoday = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # clear the folder to avoid storage overload
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    try:
        with open("log0.txt", "a") as f:
            f.write(f"{file.name} - {file.size} - {datetoday};\n")
    except:
        pass

    with open(os.path.join(folder, file.name), "wb") as f:
        f.write(file.getbuffer())
    return 0

#emotion list
emotion_list = ['Angry😡', 'Disgust😖', 'Fear😱', 'Happy😊', 'Neutral😐', 'Sad😥', 'Surprise😮']

# page settings
st.set_page_config(page_title="SER WEB APP", page_icon=":speaker:", layout="wide")


def main():
    st.title('Verbal Communication Quality Monitoring & Feedback System')
    file_ = open("/Users/user/SER/speech_emotionn.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )

    audio_file = st.file_uploader("Upload audio file for Emotion Prediction", type=['wav'])
    if audio_file is not None:
        if not os.path.exists("audio"):
            os.makedirs("audio")
        path = os.path.join("audio", audio_file.name)
        if_save_audio = save_audio(audio_file)
        if if_save_audio == 1:
            st.warning("File size is too large. Try another file.")
        elif if_save_audio == 0:
            # extract features
            # display audio
            st.audio(audio_file, format='audio/wav', start_time=0)
        else:
            st.warning("File size is too small. Try another file.")
    
    st.sidebar.title("Speech Emotion Recognition(SER)")
    side_img = Image.open("e.jpg")
    with st.sidebar:
        st.image(side_img, width=300)


    if audio_file is not None:
        st.markdown("## Analyzing...")
        if not audio_file == "test":
            st.sidebar.subheader("Audio File")
            file_details = {"Filename": audio_file.name, "FileSize": audio_file.size}
            st.sidebar.write(file_details)

        result = get_features(audio_file)
        extracted_df = pd.read_csv("features.csv")
        extracted_df = extracted_df.fillna(0)
        X = extracted_df.drop(labels="labels", axis=1)

        # Standardize data
        scaler = StandardScaler()
        scaler.fit_transform(X)
        result = scaler.transform(result)
        result = result[...,np.newaxis]
        predictions = model.predict(result)
        average_score = predictions.mean(axis=0)
        emotion_index = average_score.argmax(axis=0)
        st.write("Speech Emotion: ", emotion_list[emotion_index])
    st.write("\n")

    if st.button("Start Recording for Emotion Prediction"):
        CHUNK = 1024 
        FORMAT = pyaudio.paInt16 #paInt8
        CHANNELS = 2 
        RATE = 44100 #sample rate
        RECORD_SECONDS = 4
        WAVE_OUTPUT_FILENAME = "Recorded Audio.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) #buffer

        st.write("Recording...")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data) # 2 bytes(16 bits) per channel

        st.write("Done Recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()


        result = get_features(WAVE_OUTPUT_FILENAME)
        extracted_df = pd.read_csv("features.csv")
        extracted_df = extracted_df.fillna(0)
        X = extracted_df.drop(labels="labels", axis=1)

        # Standardize data
        scaler = StandardScaler()
        scaler.fit_transform(X)
        result = scaler.transform(result)
        result = result[...,np.newaxis]
        predictions = model.predict(result)
        average_score = predictions.mean(axis=0)
        emotion_index = average_score.argmax(axis=0)
        st.write("Emotion Prediction: ", emotion_list[emotion_index])
    


    st.sidebar.subheader("List of Emotions:")
    st.sidebar.subheader(" 1. Angry😡 ")
    st.sidebar.subheader(" 2. Disgust😖 ")
    st.sidebar.subheader(" 3. Fear😱 ")
    st.sidebar.subheader(" 4. Happy😊 ")
    st.sidebar.subheader(" 5. Neutral😐 ")
    st.sidebar.subheader(" 6. Sad😥 ")
    st.sidebar.subheader(" 7. Surprise😮 ")



if __name__ == '__main__':
    main()