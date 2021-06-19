#!/usr/bin/env python3
# coding: utf8
import pyopenjtalk
import numpy
import simpleaudio as sa
from scipy.io import wavfile

x, sr = pyopenjtalk.tts("おめでとうございます")
wavfile.write("test.wav", sr, x.astype(numpy.int16))

play_obj = sa.play_buffer(x.astype(numpy.int16), 1, 2, 44100)
play_obj.wait_done()
#if play_obj.is_playing(): play_obj.stop()

#wavfile.write("test.wav", sr, x.astype(np.int16))

#x = wave_file.readframes(wave_file.getnframes()) #frameの読み込み
#x = np.frombuffer(x, dtype= "int16") #numpy.arrayに変換

print(pyopenjtalk.g2p('こんにちは'))

