# requires ffmpg

import click
import http.server
import socketserver
import os


@click.group()
def cli():
    click.echo('Starting')


@cli.command(help="stream a video")
@click.option('--port', default=8000, help="specify the port to serve the stream over")
@click.option('--mp4', default="default.mp4", help="specify the file to be streamed")
def stream(port, mp4):
    generateHlsPlaylist(mp4)
    serveStream(port, mp4)


# @cli.command(help="Generate and Stream a video")
# @click.option('--port', default=8000, help="Specify the port to serve the stream over")
# def streamGeneratedVideo(port):
#     generateMp4()
#     generateHlsPlaylist(mp4)
#     serveStream(port)


def generateHlsPlaylist(videoFile):
    os.system('cd hls_files/')
    os.system('rm -rfy *')
    os.system('cd ..')
    os.system(
        'ffmpeg -i '+videoFile+' -vn hls_files/'+videoFile.split('.')[0]+'.mp3 -c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 hls_files/'+videoFile.split('.')[0]+'.m3u8')


def serveStream(port, videoFile):
    os.chdir('hls_files')
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print("serving at port", port)
    print("Stream available at http://localhost:" +
          str(port)+"/"+videoFile.split('.')[0]+".m3u8")
    httpd.serve_forever()


if __name__ == '__main__':
    cli()
