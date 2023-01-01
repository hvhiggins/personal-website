import os
import glob
from jinja2 import Environment, FileSystemLoader

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

# Find all files with the j2 extension in the current directory
templates = glob.glob('*.j2') 

nav = [
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
            }
        ]

def render_template(filename):
    return env.get_template(filename).render(
        navigation = nav,
        page_heading = 'About',
        page_content = 'My name is Holden Higgins, I like writing code and \
                        reading everything from Twilight to Epictetus. Currently \
                        I\'m pursuing a Computational and Applied Math degree at \
                        The University of Chicago. This website is a home for \
                        things I make.'
    )

if __name__ == "__main__":
    for f in templates:
        rendered_string = render_template(f)
        with open('../test_output.html', 'w') as outfile:
            outfile.write(rendered_string)