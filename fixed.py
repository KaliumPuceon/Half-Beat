from scipy.io.wavfile import read, write
import numpy
import sys

print("load file")
rate, wave = read("work.wav")
print("file loaded")

tempo = float(sys.argv[1])

out = []

print("halving things")
for k in range(len(wave)):

    if ((k/rate)*(tempo/60))%2>=1:
        out.append(wave[k])

print("halving done")

out = numpy.asarray(out)

print("save file")
write("out.wav", rate, out)
