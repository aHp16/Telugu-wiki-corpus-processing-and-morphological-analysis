from bs4 import BeautifulSoup
import os

# Path to downloaded wiki files
input_folder = "downloaded_site/te.wikipedia.org/wiki"
output_folder = "downloaded_text"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

def clean_text(text):
    """Remove unwanted sections and clean extracted text."""
    unwanted_sections = ["మరింత చదవండి", "ఇవి కూడా చూడండి", "పుస్తక సూచిక", "మూలాలు"]
    lines = text.split("\n")
    filtered_lines = []
    
    skip_section = False
    for line in lines:
        if any(section in line for section in unwanted_sections):
            skip_section = True
        if not skip_section:
            filtered_lines.append(line)
    return "\n".join(filtered_lines)

def extract_text_from_html(file_path):
    """Extract main text content from an HTML file."""
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Find main content div
    main_content = soup.find("div", class_="mw-parser-output")
    if not main_content:
        return ""

    # Extract text while skipping unwanted sections
    text = clean_text(main_content.get_text(separator="\n"))
    return text

# Process all HTML files in the wiki folder
for filename in os.listdir(input_folder):
    if filename.endswith(".html"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".html", ".txt"))

        text_content = extract_text_from_html(input_path)
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(text_content)

        print(f"Converted: {filename} -> {output_path}")

print("HTML to text conversion completed!")
#step2
