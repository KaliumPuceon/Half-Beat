from scipy.io.wavfile import read, write
import numpy
import sys
import math

print("load beatmap")
beatmap = open("beatmap","r")
print("beatmap loaded")

beattimes = beatmap.read()
beattimes = beattimes.strip()
beattimes = beattimes.split("\n")[:-1]

print("load file")
rate, wave = read("work.wav")
print("file loaded")

out = []

print("halving things")

keep = True

leadin=1000

for k in range(len(beattimes[:-1])):

    if keep:
        out.extend(int(rate/leadin)-wave[math.floor(rate*float(beattimes[k])):int(rate/leadin)+math.floor(rate*float(beattimes[k+1]))])

    keep = not(keep)

print("halving done")

out = numpy.asarray(out)

print("save file")
write("out.wav", rate, out)
