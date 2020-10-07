import time

import moviepy.editor as mpy
import gizeh as gz
import click

from math import pi

BLUE = (59/255, 89/255, 152/255)
WHITE = (255, 255, 255)
VIDEO_SIZE = (640, 480)


def render_text(t):
    surface = gz.Surface(640, 60, bg_color=(1, 1, 1))
    text = gz.text("Text", fontfamily="Charter",
                   fontsize=30, fontweight='bold', fill=BLUE, xy=(320, 40))

    text.draw(surface)
    return surface.get_npimage()


def draw_stars(t):
    surface = gz.Surface(640, 120, bg_color=(1, 1, 1))
    for i in range(5):
        star = gz.star(nbranches=5, radius=120*0.2,
                       xy=[100*(i+1), 50], fill=(0, 1, 0),
                       angle=t*pi)
        star.draw(surface)
    return surface.get_npimage()


@click.group()
def cli():
    click.echo('Starting')


@cli.command(help="Generate Video and Stream")
def gvas():

    text = mpy.VideoClip(render_text, duration=10)
    stars = mpy.VideoClip(draw_stars, duration=10)
    video = mpy.CompositeVideoClip(
        [
            text.set_position(
                ('center')),
            stars.set_position(
                ('center', text.size[1])
            )
        ],
        size=VIDEO_SIZE).\
        on_color(
        color=WHITE,
        col_opacity=1).set_duration(10)

    video.write_videofile('video_with_python.mp4', fps=10)


if __name__ == '__main__':
    cli()
