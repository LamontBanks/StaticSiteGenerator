# Static Site Generator

Render Markdown files into a static HTML files, written in Python.

Guided backend development project using [boot.dev](https://www.boot.dev/courses/build-static-site-generator-python).

## Demo

1. `content/index.md`:
![Markdown doc](/markdown.png)

1. `$ ./main.sh`

3. `public/index.html`
![HTML doc](/html.png)

# Requirements

- Python 3.12+

# Run Local Server

    $ ./main.sh

# Run Tests

    $ ./test.sh

    Run file individually:
    
    $ python3 src/<file name>.py    # No unittest in the commmand

# Limitations
- Markdown must be valid
    - Code blocks cannot have blank lines
    - No nested Markdown