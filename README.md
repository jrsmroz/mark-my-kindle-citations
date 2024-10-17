# HTML to Markdown Converter

This tool converts HTML citation files generated by Kindle iOS app to a Markdown format. It extracts book titles, authors, citations, and section highlights, and formats them in markdown file.

## Requirements
- Python 3.6+
- `BeautifulSoup` library (part of `beautifulsoup4` package)

## Installation

1. Clone the repository or download the script:
    ```bash
    git clone https://github.com/jrsmroz/mark-my-kindle-citations.git
    ```

2. Make the script executable:
    ```bash
    chmod +x mark-my-kindle-citations
    ```

3. Make sure you have Python 3 installed on your system.

## Usage

You can run the script from the command line. The tool requires an input HTML file and optionally takes an output file path.

### Command:
```bash
mark-my-kindle-citations <input_file> [output_file]
```

### Arguments:
- `<input_file>`: Path to the HTML file to be converted.
- `[output_file]` (optional): Path to the output markdown file. If not specified, the tool will create an output file with the same name as the input file but with a `.md` extension.


### Example:
```bash
mark-my-kindle-citations my_highlights.html my_highlights.md
```

This will generate a markdown file named `output.md` in the specified location.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
