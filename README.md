# Half Beat
## The awful meme python script I pulled together in half an hour

Hey so there's this [meme going around on
tumblr](http://spudislander.tumblr.com/post/171620330836/every-second-beat-of-sail-by-awolnation-you)
and I wanted to get in on it but also I have no idea how to edit music, but I
can write python so this happened. I've added a few things in the past few days,
including a completely different way of doing the beat splits. Read on for more
information.

## DEPENDENCIES
You'll need to install:
* [ffmpeg](https://www.ffmpeg.org/)
* [numpy](http://www.numpy.org/)
* [scipy](https://www.scipy.org/)
* [aubio](https://github.com/aubio/aubio)

Assuming you're on linux that's probably available in your package manager, or
at least the last three will be in pip.

## USAGE
There are two options for converting a file. Using `dynabeat.sh` will try and
match every single beat of the song, however the detection is sketchy at best
and while this might give you a clearer change, it'll be less consistent and
more jerky.

The other option is to use `fixedbeat.sh`. This uses a fixed tempo with zero
offset, so ideally your song should start with a beat on or near the first
sample of the file. I'll try and accommodate others... later.

To use these, run `./fixedbeat.sh $file` or `./dynabeat.sh $file` to convert
$file, or run `./fixedbeat.sh $file $outfile` or `./dynabeat.sh $file $outfile`
to output to $outfile instead of `out.mp3`.

The thing will sit for a while and spit out some messages and then once it's
done your prompt will come back and the freshly created song will be in
`out.mp3` or the location you asked for. I'll add the ability to specify...
anything... in the future.

## Example output
Here's a few of the things I made earlier. It's on my [tumblr](https://andmaybegayer.tumblr.com/tagged/everysecondbeat)

## How work?
I use ffmpeg to convert your file to wav. Aubio detects the tempo and passes it
to python, along with your file. Python uses scipy's wav tools to read the thing
in as a numpy array, it does a counter to cut out every second beat based on the
tempo and the sample rate, and then saves that to a file. Then ffmpeg converts
that back to an mp3 and removes all the junk files. This is very finnicky, and
it'll break a lot at the moment. When I don't have tests breathing down my neck
I might improve this.

## Testimonials
"The shittiest form of audio compression" - Victoria Longez, 2018

"Have you seen this monstrosity" - hopelesstiptoe, 2018

"You were doing this at one in the morning. Why" - Stefan Schröder, 2018

"Please stop doing the music crimes" - Vulpes, 2018

"Kalium, this is a very bad thing and I want to pin a medal on your face" - Barometz, 2018

"Ye gods, this is horrific" - Multiplexd, 2018

## License
There's a license in the LICENSE file but tl;dr you can share and modify for any
purpose as long as you maintain the copyright, which is ISC.
