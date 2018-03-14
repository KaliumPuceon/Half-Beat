#! /bin/bash
set -e

if which python3 > /dev/null; then
    python=python3
else
    python=python
fi
echo "convert to wav"
ffmpeg -y -i "$1" work.wav 2> /dev/null
echo "determine tempo"
aubio beat work.wav 2> /dev/null | awk '{$1=$1};1' > beatmap
echo "Half-beating in progress"
$python dynamic.py
echo "Half-beating complete! Convert to output file"
ffmpeg -y -i out.wav "${2:-out.mp3}" 2> /dev/null
echo "Cleaning up"
rm out.wav work.wav
echo "Done!"

