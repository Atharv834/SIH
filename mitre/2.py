import requests
from bs4 import BeautifulSoup

# Specify the correct file path
input_file_path = r"C:\Users\Atharv\Desktop\Chatgpt\SIH\mitre\mitre.html"
output_file_path = r"C:\Users\Atharv\Desktop\Chatgpt\SIH\mitre\x.html"

# Read the HTML content from the input file
with open(input_file_path, "r", encoding='utf-8') as f:
    html_doc = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_doc, 'html.parser')

# Find the specific div by ID
div_with_id = soup.find(id="TableWithRules")

# Write the output to a new file
with open(output_file_path, "w", encoding='utf-8') as output_file:
    if div_with_id:
        for child in div_with_id.children:
            output_file.write(str(child) + "\n")
        print("Output successfully saved to x.html.")
    else:
        print("Element with id 'TableWithRules' not found.")
        output_file.write("Element with id 'TableWithRules' not found.")
