.. image:: https://img.shields.io/pypi/v/SER.svg
        :target: https://pypi.python.org/pypi/SER

.. image:: https://img.shields.io/travis/hrithikwel8/SER.svg
        :target: https://travis-ci.com/hrithikwel8/SER

.. image:: https://readthedocs.org/projects/SER/badge/?version=latest
        :target: https://SER.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

==========================
Speech emotion Recognition
==========================
Speech Emotion Recognition (SER), is the act of attempting to recognize human emotion and affective states from speech.
Emotion recognition is the part of speech recognition which is gaining more popularity and need for it increases enormously.
It is used in call center for classifying calls according to emotions and can be used as the performance parameter for conversational analysis thus identifying the unsatisfied customer, customer satisfaction and so on for helping companies improving their services.
It can also be used in-car board system based on information of the mental state of the driver can be provided to the system to initiate his/her safety preventing accidents to happen.


Verbal Communication Quality Monitoring & Feedback System
--------------------------------------------------------------------------------
Verbal communication include sounds, words, language, and speech. Speaking is an effective way of communicating and helps in expressing our emotions in words.
Building a real-time demo of quality monitoring of verbal communication & feedback system with the help of speech emotion recognition(deep learning) & streamlit.
Speech is the most natural way of expressing ourselves as humans. It is only natural then to extend this communication medium to computer applications.
We define speech emotion recognition (SER) systems as a collection of methodologies that process and classify speech signals to detect the embedded emotions.

Datasets:
------------

1. Ryerson Audio-Visual Database of Emotional Speech (Ravdess):

This dataset includes around 1500 audio file input from 24 different actors.
12 male and 12 female where these actors record short audios in 8 different emotions i.e. 1 = neutral, 2 = calm, 3 = happy, 4 = sad, 5 = angry, 6 = fearful, 7 = disgust,
8 = surprised.
Each audio file is named in such a way that the 7th character is consistent with the different emotions that they represent.

2. Surrey Audio-Visual Expressed Emotion (Savee):

This dataset contains around 500 audio files recorded by 4 different male actors.
The first two characters of the file name correspond to the different emotions that the portray.


Emotions in Datasets:
----------------------------
● Neutral
● Happy
● Sad
● Angry
● Fear
● Disgust
● Surprise


Data Augmentation:
--------------------------
Data augmentation is the process by which we create new synthetic data samples by adding small perturbations on our initial training set.
It is a key ingredient of the state-of-the-art systems for speech recognition.
Some ways for data augmentation in sound data: -
● Noise injection 
● Stretching
● Shifting
● Pitching


Feature Extraction
------------------------
Extraction of features is a very important part in analyzing and finding relations between different things.
As we already know that the data provided of audio cannot be understood by the models directly so we need to convert them into an understandable format for which feature extraction is used.

Used just 3 main features [ZCR, RMS and MFCC] for this task after experimenting with many features like ZCR, RMS & MFCC after experimenting with many features like Zero crossing rate, Entropy of energy, Spectral centroid, Spectral entropy, Spectral flux, Spectral roll off, chroma_stft & Mel frequency cepstral coefficients.

1. The Zero-Crossing Rate (ZCR): An audio frame is the rate of sign changes of the signal during the frame.
In other words, it is the number of times the signal changes value, from positive to negative and vice versa, divided by the length of the frame.
It’s aims to study the rate in which a signal’s amplitude changes sign within each frame.

2. RMS: It extracts the Root Mean Square (RMS) from a set of samples.
RMS is calculated by adding the squares of each sample, dividing this by the total number of samples in the window, and finding the square root of the result.

3. MFCC: Mel-frequency Cepstral coefficients (MFCCs) are the signal coefficients that are collected to forms MFC.
The Mel-frequency cepstrum different from cepstrum in the frequency bands which are equally divided on the Mel scale.
MFCCs are rigorously used as features in speech recognition systems.
Mel Frequency Cepstral Coefficients form a cepstral representation where the frequency bands are not linear but distributed according to the Mel-scale.


Conclusion
---------------
Deep learning can be used in Verbal Communication Quality Monitoring & Feedback System to process audio data in real time.
With speech emotion recognition, It can identify or predict speech emotion after recording audio or drag & drop audio files.
Speech emotion recognition system can identify the mental state of user, conversational analysis to improve customer satisfaction.
Overall achieved 92% accuracy on test data but we can improve it more by adding more audio data, applying more augmentation techniques and using other feature extraction methods.



* Free software: MIT license
* Documentation: https://SER.readthedocs.io.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
