# hls-stream-cli

A cli tool to create a hls stream on a local port for use in application testing

## To run install:

- [ffmpeg](https://www.google.com)
- [click](https://pypi.org/project/click/)

## help

### Usage:

python3 main.py stream [OPTIONS]

Stream a video

### Options:

-port --- INTEGER --- Specify the port to serve the stream over

-mp4 --- TEXT --- Specify the file to be streamed

-help --- Show this message and exit.
