==========================
Speech emotion Recognition
==========================


.. image:: https://img.shields.io/pypi/v/SER.svg
        :target: https://pypi.python.org/pypi/SER

.. image:: https://img.shields.io/travis/hrithikwel8/SER.svg
        :target: https://travis-ci.com/hrithikwel8/SER

.. image:: https://readthedocs.org/projects/SER/badge/?version=latest
        :target: https://SER.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Verbal Communication Quality Monitoring & Feedback System
--------------------------------------------------------------------------------


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


Feature Extraction
--------
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


* Free software: MIT license
* Documentation: https://SER.readthedocs.io.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
