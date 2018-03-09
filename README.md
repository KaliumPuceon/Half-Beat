# Half Beat
## The awful meme python script I pulled together in half an hour

Hey so there's this [meme going around on
tumblr](http://spudislander.tumblr.com/post/171620330836/every-second-beat-of-sail-by-awolnation-you)
and I wanted to get in on it but also I have no idea how to edit music, but I
can write python so this happened.

## DEPENDENCIES
You'll need to install:
* [ffmpeg](https://www.ffmpeg.org/)
* [numpy](https://github.com/aubio/aubio)
* [scipy](https://www.scipy.org/)
* [aubio](http://www.numpy.org/)

Assuming you're on linux that's probably available in your package manager, or
at least the last three will be in pip.

## USAGE
once you've cloned the repo into wherever you want to work, use `chmod +x` to
make `convert.sh` executable. To convert a file, run `./convert.sh $file`. This
might work if you supply a full path, I have no idea. Probably copy your file
into the working folder, and also make sure there's no spaces, this was one hell
of a rush job.

The thing will sit for a while and spit out some ffmpeg messages and then once
it's done your prompt will come back and the freshly created song will be in
`out.mp3`. I'll add the ability to specify... anything... in the future.

## Example output
Here's a few of the things I made earlier. It's on my [tumblr](https://www.andmaybegayer.tumblr.com/tagged/EverySecondBeat)

## How work?
I use ffmpeg to convert your file to wav. Aubio detects the tempo and passes it
to python, along with your file. Python uses scipy's wav tools to read the thing
in as a numpy array, it does a counter to cut out every second beat based on the
tempo and the sample rate, and then saves that to a file. Then ffmpeg converts
that back to an mp3 and removes all the junk files. This is very finnicky, and
it'll break a lot at the moment. When I don't have tests breathing down my neck
I might improve this.

## Testimonials
"The shittiest form of audio compression" - James Lacey, 2018

"Have you seen this monstrosity" - hopelesstiptoe, 2018

"You were doing this at one in the morning. Why" - Stefan Schroder, 2018

## License
There's a license in the LICENSE file but tl;dr you can share and modify for any
purpose as long as you maintain the copyright, which is ISC.
