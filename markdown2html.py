#!/usr/bin/env python3
"""
markdown2html.py: A script to convert a Markdown file to an HTML file.

Usage:
    ./markdown2html.py <input_markdown_file> <output_html_file>

Arguments:
    <input_markdown_file>  The path to the input Markdown file.
    <output_html_file>     The path to the output HTML file.

Requirements:
    - If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
    - If the Markdown file doesn’t exist: print in STDERR Missing <filename> and exit 1
    - Otherwise, print nothing and exit 0
"""

import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    """
    Convert a Markdown file to an HTML file.

    Args:
        input_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.
    """
    with open(input_file, 'r') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as f:
        f.write(html_content)

def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)

if __name__ == "__main__":
    main()



#!/usr/bin/env python3
"""
markdown2html.py: A script to convert a Markdown file to an HTML file.

Usage:
    ./markdown2html.py <input_markdown_file> <output_html_file>

Arguments:
    <input_markdown_file>  The path to the input Markdown file.
    <output_html_file>     The path to the output HTML file.

Requirements:
    - If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
    - If the Markdown file doesn’t exist: print in STDERR Missing <filename> and exit 1
    - Otherwise, print nothing and exit 0
"""

import sys
import os

def parse_markdown(markdown_content):
    """
    Parse the Markdown content and convert it to HTML.

    Args:
        markdown_content (str): The content of the Markdown file.

    Returns:
        str: The HTML content generated from the Markdown content.
    """
    html_content = []
    lines = markdown_content.splitlines()

    for line in lines:
        if line.startswith('#'):
            # Count the number of leading '#' characters to determine the heading level
            heading_level = len(line.split(' ')[0])
            if heading_level > 6:
                heading_level = 6
            # Strip the leading '#' characters and any leading/trailing whitespace
            heading_text = line[heading_level:].strip()
            # Create the HTML heading tag
            html_content.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
        else:
            html_content.append(line)

    return '\n'.join(html_content)

def convert_markdown_to_html(input_file, output_file):
    """
    Convert a Markdown file to an HTML file.

    Args:
        input_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.
    """
    # Read the content of the Markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()

    # Parse Markdown to HTML
    html_content = parse_markdown(markdown_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get the filenames from the arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Convert the Markdown file to HTML
    convert_markdown_to_html(input_file, output_file)

    # Exit with code 0 (success)
    sys.exit(0)

if __name__ == "__main__":
    main()

