from scipy.io.wavfile import read, write
import numpy
import aubio
import sys

rate, wave = read("work.wav")

tempo = float(sys.argv[1])
print(tempo)

out = []
wrap=0

for k in range(len(wave)):
    wrap = wrap -1
    if ((k/rate)*(tempo/60))%2>=1:
        out.append(wave[k])

out = numpy.asarray(out)

print (out == wave)

write("out.wav", rate, out)

