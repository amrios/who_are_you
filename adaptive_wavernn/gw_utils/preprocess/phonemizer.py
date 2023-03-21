# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (main, Aug 25 2022, 23:26:10) 
# [GCC 11.2.0]
# Embedded file name: /home/lvargas/researchProjects/guesswho18/code/preprocess/preprocess/phonemizer.py
# Compiled at: 2019-01-11 18:32:15
from __future__ import print_function
import requests, pandas as pd, glob

class phoneAligner:

    def __init__(self, audiofile, textfile, arpa_to_ipa_path='../../data/arpa-to-ipa-dict.txt'):
        self.audiofile = audiofile
        self.textfile = textfile
        self.arpa_to_ipa = eval(open(arpa_to_ipa_path, 'r').read())
        self.phonemized = None
        self.df = None
        return

    def phonemize(self):
        params = (('async', 'false'), )
        audio = (
         self.audiofile, open(self.audiofile, 'rb'))
        try:
            transcript = (
             self.textfile, open(self.textfile, 'rb'))
        except IOError:
            transcript = self.textfile

        files = {'audio': audio, 
           'transcript': transcript}
        response = requests.post('http://localhost:8765/transcriptions', params=params, files=files)
        self.phonemized = eval(response.text)

    def parse_results(self, verbose=False):

        def get_ipa(arpabet_phoneme, word):
            arpa = arpabet_phoneme.split('_')[0].upper()
            if arpa in self.arpa_to_ipa:
                IPA = self.arpa_to_ipa[arpa]['IPA']
                return IPA
            else:
                print('\tDEBUG: Error in IPA Tranlation:', arpa, word)
                return '-'

        rows = []
        errors = {'words': [], 'count': 0}
        text, phonemes = self.phonemized.items()
        for x in phonemes[1]:
            if verbose:
                print('Keys available:', x.keys())
                for key in ['case', 'word', 'startOffset', 'endOffset']:
                    print(key, ':', x[key])

            if x['case'] == 'not-found-in-audio':
                print('\tDEBUG: Error word not found in audio:', x['word'])
                errors['words'].append(x['word'])
                errors['count'] += 1
                continue
            phoneme_start = float(x['start'])
            for phoneme in x['phones']:
                phoneme_end = phoneme_start + float(phoneme['duration'])
                row = [
                 x['alignedWord'],
                 x['case'],
                 x['start'],
                 x['end'],
                 x['endOffset'],
                 phoneme['duration'],
                 phoneme['phone'],
                 get_ipa(phoneme['phone'], x['alignedWord']),
                 phoneme_start,
                 phoneme_end,
                 self.audiofile.split('/')[-1]]
                phoneme_start = phoneme_end
                rows.append(row)

        columns = [
         'word', 
         'valid', 
         'word_starttime', 
         'word_endtime', 
         'offset', 
         'duration', 
         'arpabet', 
         'ipa', 
         'phoneme_start', 
         'phoneme_end', 
         'filename']
        self.df = pd.DataFrame(columns=columns, data=rows)
        if errors['count'] != 0:
            print('\tError phonimizing %d words: %s' % (
             errors['count'], (' ').join(errors['words'])))
            if verbose:
                print('Data is parsed as a dataframe')
# okay decompiling phonemizer.pyc
