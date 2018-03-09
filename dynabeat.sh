#! /bin/bash

echo "remove leftovers"
[ -e out.mp3 ] && rm out.mp3
echo "convert to wav"
ffmpeg -y -i $1 work.wav 2> /dev/null
echo "determine tempo"
aubio beat work.wav 2> /dev/null | awk '{$1=$1};1' > beatmap
echo "Half-beating in progress"
python dynamic.py
echo "Half-beating complete! Convert to mp3"
ffmpeg -y -i out.wav out.mp3 2> /dev/null
echo "Cleaning up"
rm *.wav
echo "Done!"

