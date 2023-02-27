import os
import glob
import json
from jinja2 import Environment, FileSystemLoader

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

# Find all files with the j2 extension in the current directory
templates = glob.glob('*.j2') 

nav = [
            {
                'href': "index.html",
                'caption': 'About'
            },
            {
                'href': "mandelbrot/index.html",
                'caption': 'Mandelbrot set'
            },
            {
                'href': "julia/index.html",
                'caption': 'Julia sets'
            },
            {
                'href': "epicycloid-vanillajs/index.html",
                'caption': "Epicycloids",
            },
            {
                'href': "svg-clock/index.html",
                'caption': 'Tick tock, svg clock'
            },
            {
                'href': "js_wordle/index.html",
                'caption': 'Like wordle, but jankier'
            },
            {
                'href': "art/Beach.html",
                'caption': 'Art 1'
            },
            {
                'href': "art/Centerline.html",
                'caption': 'Art 2'
            },
            {
                'href': "art/Gold River.html",
                'caption': 'Art 3'
            },
            {
                'href': "art/Penrose tiles.html",
                'caption': 'Art 4'
            },

        ]

    
code_pages = [
    'js_wordle',
    'svg-clock',
    'epicycloid-vanillajs',
    'julia',
    'mandelbrot',
]
homepage_content = {
    'page_title': 'Holden Higgins',
    'page_heading': 'About',
    'page_content': 'My name is Holden Higgins, I like writing code and '
                        'reading everything from Stephanie Meyer to Suetonius. Currently '
                        'I\'m pursuing a Math degree at the University of Chicago. '
                        'This website is a home for things I make.'
}

art_pages = [
    {
        'page_title': 'Beach',
        'page_heading': 'Beach, spackle on wood',
        'page_content': "<img src='/art/beach.jpg' alt='beach' width=100%>"
    },
    {
        'page_title': 'Centerline',
        'page_heading': 'Centerline, spackle on canvas, aided by a fork',
        'page_content': "<img src='/art/centerline.jpg' alt='centerline' width=100%>"
    },
    {
        'page_title': 'Gold River',
        'page_heading': 'Gold River, spackle on cardboard',
        'page_content': "<img src='/art/gold-river.jpg' alt='gold river' width=100%>"
    },
    {
        'page_title': 'Penrose tiles',
        'page_heading': 'Penrose tiles, 3d printed',
        'page_content': "<img src='/art/penrose-tiles.jpg' alt='penrose tiles' width=100%>"
    }
]


def render_template(template, page):
    return env.get_template(template).render(
        navigation = nav,
        **page
    )

if __name__ == "__main__":
    for template in templates:
        rendered_string = render_template(template, homepage_content)
        with open('../index.html', 'w') as outfile:
            outfile.write(rendered_string)
        for page in code_pages:
            with open(f'../{page}/content.json', 'r') as infile:
                page_content = json.load(infile)
            rendered_string = render_template(template, page_content)
            with open(f'../{page}/index.html', 'w') as outfile:
                outfile.write(rendered_string)

        for page in art_pages:
            rendered_string = render_template(template, page)
            with open(f'../art/{page["page_title"]}.html', 'w') as outfile:
                outfile.write(rendered_string)