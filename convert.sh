#! /bin/bash

rm out.mp3
ffmpeg -i $1 work.wav
TEMPO=`aubio tempo work.wav 2> /dev/null`
echo $TEMPO
python run.py $TEMPO
ffmpeg -i out.wav out.mp3
rm *.wav

