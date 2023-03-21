# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.13 (main, Aug 25 2022, 23:26:10) 
# [GCC 11.2.0]
# Embedded file name: /home/logan/SynologyDrive/Research/guesswho_new/guesswho18/code/adaptive_wavernn/utils/preprocess/praatformant.py
# Compiled at: 2021-10-08 00:22:25
# Size of source mod 2**32: 1864 bytes
from praatio import praat_scripts
import sys, os, pandas as pd

def formant_finder(audio_file, sex, output='output.txt', remove_output=False):
    praatscript = '/home/lvargas/researchProjects/guesswho18/code/preprocess/preprocess/get_formants.praat'
    praatEXE = '/usr/bin/praat'
    if sys.platform == 'darwin':
        praatEXE = '/Applications/Praat.app/Contents/MacOS/Praat'
    inputWavFN = os.path.abspath(audio_file)
    outputTxtFN = os.path.abspath(output)
    maxFormant = 5500
    if sex == 'm':
        maxFormant = 5000
    arr = praat_scripts.getFormants(praatEXE=praatEXE, inputWavFN=inputWavFN,
      outputTxtFN=outputTxtFN,
      stepSize=0.001,
      maxFormant=maxFormant,
      scriptFN=praatscript)
    if remove_output:
        os.remove(outputTxtFN)
    return (
     arr, 0.01)


def make_dataframe(results):
    return pd.DataFrame(results, columns=["'time'", "'f1'", "'f2'", "'f3'", "'f4'", "'f5'"])
# okay decompiling __pycache__/praatformant.cpython-37.pyc
