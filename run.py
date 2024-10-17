import argparse
import os
import sys
from bs4 import BeautifulSoup


def convert_html_to_markdown(input_file_path, output_file_path):
    """
    Convert an HTML file with kindle citations to a Markdown file.
    """

    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            markdown_lines = extract_citations_markdown(input_file)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write("\n".join(markdown_lines))
    except FileNotFoundError as e:
        print(f"Error: {e.strerror}: '{e.filename}'")
        sys.exit(1)
    except AttributeError:
        print("Error: Failed to parse HTML structure.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def extract_citations_markdown(input_file):
    """
    Extract the book title, authors, and citations from the HTML file
    and return as a list of Markdown lines.
    """

    soup = BeautifulSoup(input_file, 'html.parser')

    book_title = soup.find('div', class_="bookTitle").get_text(strip=True)
    authors = soup.find('div', class_="authors").get_text(strip=True)
    citation = soup.find('div', class_="citation").get_text(strip=True)

    markdown_lines = [
        f"# {book_title}",
        "",
        f"**Authors:** {authors}",
        "\n"
        f"**Citation:** {citation}",
        "\n"
    ]

    # Each chapter is a section with its own citation notes
    for section in soup.find_all('div', class_='sectionHeading'):
        markdown_lines.append(f"## {section.get_text(strip=True)}\n")

        node = section.find_next_sibling()
        while node and node.name == 'div':
            if 'noteHeading' in node.get('class', []):
                markdown_lines.append(f"**{node.get_text(strip=True)}:**\n")
            elif 'noteText' in node.get('class', []):
                markdown_lines.append(f"> {node.get_text(strip=True)}\n")
            else:
                break
            node = node.find_next_sibling()

    return markdown_lines


def main():
    parser = argparse.ArgumentParser(description='Convert an HTML citation file to Markdown format.')
    parser.add_argument('input_file', help='Path to the input HTML file.')
    parser.add_argument('output_file', nargs='?', help=(
        'Path to the output Markdown file. If not specified, '
        'the output filename will be the same as the input but with a .md extension.')
    )
    args = parser.parse_args()

    input_file_path = os.path.abspath(args.input_file)
    output_file_path = args.output_file or os.path.splitext(input_file_path)[0] + ".md"

    convert_html_to_markdown(input_file_path, output_file_path)
    print(f"Markdown file written to: {output_file_path}")


if __name__ == '__main__':
    main()
